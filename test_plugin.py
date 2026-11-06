"""Tests for the single-file plugin, on the oldest Python that Wox supports.

uvx --python 3.10 --with wox-plugin==0.0.92 pytest
"""

import asyncio
import json
import os
import re
import sys
import tempfile
import time
import unittest
from pathlib import Path
from types import ModuleType
from unittest import mock
from xml.sax.saxutils import quoteattr

from wox_plugin import PluginInitParams, Query, QueryEnv, QueryType, RegisterPluginToolResult, Selection

PLUGIN_FILE = Path(__file__).resolve().parent / "Wox.Plugin.JetBrainsProjects.py"


def load_module() -> ModuleType:
    """Load the plugin the way Wox's host does: exec its current source into a registered module."""
    module = ModuleType("wox_single_file_jetbrains_projects_test")
    module.__file__ = str(PLUGIN_FILE)
    sys.modules[module.__name__] = module
    exec(compile(PLUGIN_FILE.read_text(encoding="utf-8"), str(PLUGIN_FILE), "exec"), module.__dict__)
    return module


jb = load_module()


def read_metadata() -> dict:
    lines = []
    for line in PLUGIN_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("#"):
            break
        lines.append(line[1:])
    return json.loads("\n".join(lines))


def recents_xml(entries: dict, component="RecentProjectsManager") -> str:
    """Build a recents file in the IDE's format from {key: {option: value}, or attributes under "_attrs"}."""
    body = []
    for key, options in entries.items():
        attrs = "".join(f" {name}={quoteattr(value)}" for name, value in options.get("_attrs", {}).items())
        rows = "".join(
            f'<option name="{name}" value="{value}" />' for name, value in options.items() if name != "_attrs"
        )
        body.append(
            f"<entry key={quoteattr(key)}><value><RecentProjectMetaInfo{attrs}>"
            f'<option name="binFolder" value="$APPLICATION_HOME_DIR$/bin" />{rows}'
            '<option name="colorInfo"><RecentProjectColorInfo associatedIndex="1" /></option>'
            '<frame x="1" y="2" width="3" height="4" /></RecentProjectMetaInfo></value></entry>'
        )
    return (
        f'<application><component name="{component}"><option name="additionalInfo"><map>'
        f'{"".join(body)}</map></option><option name="lastOpenedProject" value="x" /></component></application>'
    )


class FakeApi:
    """Records what the plugin asks of Wox. Translations come from the plugin's own metadata."""

    def __init__(self, settings=None, cache_folder=""):
        self.settings = settings or {}
        self.cache_folder = str(cache_folder)
        self.translations = read_metadata()["I18n"]["en_US"]
        self.notified = []
        self.copied = []
        self.logged = []
        self.tools = {}
        self.setting_callback = None
        self.mru_callback = None

    async def get_setting(self, ctx, key):
        return self.settings.get(key, "")

    async def get_cache_folder(self, ctx):
        return self.cache_folder

    async def get_translation(self, ctx, key):
        return self.translations[key]

    async def on_setting_changed(self, ctx, callback):
        self.setting_callback = callback

    async def on_mru_restore(self, ctx, callback):
        self.mru_callback = callback

    async def register_plugin_tool(self, ctx, option):
        self.tools[option.tool.name] = option
        return RegisterPluginToolResult()

    async def notify(self, ctx, message):
        self.notified.append(message)

    async def copy(self, ctx, params):
        self.copied.append(params.text)

    async def log(self, ctx, level, message):
        self.logged.append((level, message))


def make_query(search, trigger="jb"):
    return Query(
        id="",
        type=QueryType.INPUT,
        raw_query=search,
        selection=Selection(),
        env=QueryEnv(),
        trigger_keyword=trigger,
        search=search,
    )


async def stuck_reload(_ctx):
    await asyncio.sleep(3600)


async def first_result(plugin, search):
    return (await plugin.query(None, make_query(search))).results[0]


class FakeHomeTest(unittest.IsolatedAsyncioTestCase):
    """Gives each test a fake home and a real launcher script that records how it was called."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.home = Path(self._tmp.name).resolve()
        env = {"HOME": str(self.home), "PATH": str(self.home / "empty-path")}
        patcher = mock.patch.dict(os.environ, env)
        patcher.start()
        self.addCleanup(patcher.stop)
        for name in ("XDG_CONFIG_HOME", "XDG_CACHE_HOME", "XDG_DATA_HOME"):
            os.environ.pop(name, None)
        self.calls_file = self.home / "launcher-calls.txt"

    def make_project(self, relative) -> Path:
        path = self.home / relative
        path.mkdir(parents=True, exist_ok=True)
        return path

    def write_recents(
        self, folder, entries, file="recentProjects.xml", component="RecentProjectsManager", vendor="JetBrains"
    ):
        options = self.home / ".config" / vendor / folder / "options"
        options.mkdir(parents=True, exist_ok=True)
        (options / file).write_text(recents_xml(entries, component), encoding="utf-8")

    def write_script(self, path: Path, exit_code=0) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'#!/bin/sh\necho "$0|$PWD|${{SHIV_ROOT:-}}|$*" >> "{self.calls_file}"\nexit {exit_code}\n')
        path.chmod(0o755)
        return path

    def install_ide(self, folder, launcher="idea", vendor="JetBrains", exit_code=0) -> Path:
        """Create an install folder, and the .home file the IDE leaves in its cache folder pointing to it."""
        install = self.home / "Apps" / folder
        self.write_script(install / "bin" / launcher, exit_code)
        cache = self.home / ".cache" / vendor / folder
        cache.mkdir(parents=True, exist_ok=True)
        (cache / ".home").write_text(f"{install}\n")
        return install

    async def wait_for_call(self) -> str:
        """Wait for the launcher script, which runs detached, to record its call."""
        for _ in range(100):
            if self.calls_file.exists() and self.calls_file.read_text().endswith("\n"):
                return self.calls_file.read_text()
            await asyncio.sleep(0.02)
        return self.fail("the launcher was not called")

    async def start_plugin(self, settings=None, cache_folder=""):
        plugin = jb.JetBrainsProjectsPlugin()
        api = FakeApi(settings, cache_folder)
        await plugin.init(None, PluginInitParams(api=api, plugin_directory=""))
        await plugin.refresh_task
        return plugin, api

    def machine(self):
        return jb.Machine("linux", dict(os.environ), self.home)


class MetadataTest(unittest.TestCase):
    def setUp(self):
        self.metadata = read_metadata()

    def test_declares_what_wox_and_the_store_need(self):
        assert self.metadata["Runtime"] == "PYTHON"
        assert self.metadata["MinWoxVersion"] == "2.4.9"  # The first Wox whose host SDK has Result.identity_key.
        assert self.metadata["TriggerKeywords"] == ["jb"]
        assert set(self.metadata["SupportedOS"]) == {"Windows", "Linux", "Macos"}
        assert self.metadata["Icon"] == "svg:" + jb.IDE_LOGOS["idea"]

    def test_every_translation_exists_in_every_language(self):
        english, chinese = self.metadata["I18n"]["en_US"], self.metadata["I18n"]["zh_CN"]
        assert set(english) == set(chinese)

    def test_every_i18n_key_used_is_defined(self):
        source = PLUGIN_FILE.read_text(encoding="utf-8")
        used = set(re.findall(r"i18n:([a-z_]+)", source)) | set(
            re.findall(r'get_translation\(ctx, "([a-z_]+)"\)', source)
        )
        assert used <= set(self.metadata["I18n"]["en_US"])

    def test_every_ide_has_a_logo(self):
        assert set(jb.IDE_LOGOS) == set(jb.IDE_BY_ID)
        assert all(logo.startswith("<svg") and logo.endswith("</svg>") for logo in jb.IDE_LOGOS.values())

    def test_store_entry_and_logo_file_match_the_plugin(self):
        root = PLUGIN_FILE.parent
        entry = json.loads((root / "store-plugin.json").read_text(encoding="utf-8"))
        for key in ("Id", "Name", "Author", "Version", "MinWoxVersion", "Description"):
            assert entry[key] == self.metadata[key]
        assert entry["Runtime"] == self.metadata["Runtime"].lower()
        assert entry["DownloadUrl"].endswith("/" + PLUGIN_FILE.name)
        assert (root / "icon.svg").read_text(encoding="utf-8").strip() == jb.IDE_LOGOS["idea"]

    def test_launcher_setting_offers_every_ide(self):
        table = next(item for item in self.metadata["SettingDefinitions"] if item["Type"] == "table")
        assert table["IsPlatformSpecific"]
        options = table["Value"]["Columns"][0]["SelectOptions"]
        assert {option["Value"] for option in options} == set(jb.IDE_BY_ID)
        assert {option["Label"] for option in options} == {ide.name for ide in jb.IDES}


class MatchingTest(unittest.TestCase):
    def project(self, name, path=None, aliases=(), last_opened=1):
        return jb.Project(path or f"/p/{name}", name, last_opened, (jb.IDE_BY_ID["idea"],), aliases)

    def titles(self, projects, search, **options):
        return [project.name for project, _ in jb.rank_projects(projects, search, **options)]

    def test_scores_order_exact_prefix_word_inside_fuzzy_none(self):
        scores = [jb.match_score("foo", text) for text in ("foo", "foobar", "my-foo", "afoob", "f-o-o", "bar")]
        assert scores == sorted(scores, reverse=True)
        assert scores[-1] == 0
        assert len(set(scores)) == len(scores)
        assert scores[4] < 50
        assert scores[3] >= jb.GLOBAL_MIN_SCORE

    def test_empty_search_keeps_recency_order(self):
        projects = [self.project("b", last_opened=2), self.project("a", last_opened=1)]
        assert self.titles(projects, "  ") == ["b", "a"]

    def test_better_match_beats_more_recent(self):
        projects = [self.project("my-wox-tool", last_opened=9), self.project("wox", last_opened=1)]
        assert self.titles(projects, "wox") == ["wox", "my-wox-tool"]

    def test_recency_breaks_ties(self):
        projects = [self.project("wox-old", last_opened=1), self.project("wox-new", last_opened=2)]
        assert self.titles(projects, "wox") == ["wox-new", "wox-old"]

    def test_all_terms_must_match_in_any_order(self):
        projects = [self.project("wox-plugin-jetbrains"), self.project("wox-plugin-youtube")]
        assert self.titles(projects, "jetbrains wox") == ["wox-plugin-jetbrains"]

    def test_ignores_case_and_accents(self):
        assert self.titles([self.project("Médiathèque")], "MEDIATHEQUE") == ["Médiathèque"]

    def test_fuzzy_match(self):
        assert self.titles([self.project("fynodoro"), self.project("abc")], "fyndr") == ["fynodoro"]

    def test_fuzzy_match_rejects_scattered_letters(self):
        assert self.titles([self.project("fynodoro"), self.project("classify_bank_transactions")], "fyno") == [
            "fynodoro"
        ]

    def test_fuzzy_match_measures_the_tightest_stretch(self):
        assert jb.fuzzy_score("fyd", "ftp-config-fynodoro") == 38
        assert jb.tightest_span("xyz", "abc") is None

    def test_path_match_ranks_below_a_fuzzy_name_match(self):
        by_path = self.project("alpha", path="/work/fyn/alpha", last_opened=9)
        by_fuzzy_name = self.project("fxyxn", last_opened=1)
        assert self.titles([by_path, by_fuzzy_name], "fyn", match_path=True) == ["fxyxn", "alpha"]

    def test_module_alias_matches(self):
        assert self.titles([self.project("dir", aliases=("backend-api",))], "backend") == ["dir"]

    def test_path_only_matches_when_enabled_and_ranks_below_names(self):
        by_path = self.project("alpha", path="/work/acme/alpha", last_opened=9)
        by_name = self.project("acme", path="/other/acme", last_opened=1)
        assert self.titles([by_path, by_name], "acme") == ["acme"]
        assert self.titles([by_path, by_name], "acme", match_path=True) == ["acme", "alpha"]

    def test_path_matching_is_not_fuzzy(self):
        assert self.titles([self.project("alpha", path="/work/acme/alpha")], "wrkm", match_path=True) == []

    def test_format_age(self):
        now = 10**13
        minute = 60000
        cases = [
            (0, ""),
            (now - 10, "now"),
            (now - 5 * minute, "5m"),
            (now - 120 * minute, "2h"),
            (now - 3 * 1440 * minute, "3d"),
            (now - 62 * 1440 * minute, "2mo"),
            (now - 800 * 1440 * minute, "2y"),
        ]
        for stamp, expected in cases:
            assert jb.format_age(stamp, now) == expected

    def test_display_path_shortens_only_the_home_folder(self):
        home = Path("/home/tom")
        assert jb.display_path("/home/tom/Dev/a", home) == "~/Dev/a"
        assert jb.display_path("/home/tommy/a", home) == "/home/tommy/a"

    def test_parse_overrides(self):
        raw = json.dumps([{"ide": "idea", "path": "~/x/idea"}, {"ide": "pycharm"}, {"path": "/y"}, "bad"])
        assert jb.parse_overrides(raw) == {"idea": str(Path("~/x/idea").expanduser())}
        assert jb.parse_overrides("") == {}
        assert jb.parse_overrides("not json") == {}
        unknown_user = json.dumps([{"ide": "idea", "path": "~no-such-user-here/idea"}])
        assert jb.parse_overrides(unknown_user) == {"idea": "~no-such-user-here/idea"}
        assert jb.parse_overrides('{"a": 1}') == {}


class PlatformPathsTest(unittest.TestCase):
    def test_linux_defaults_and_xdg(self):
        machine = jb.Machine("linux", {}, Path("/h"))
        assert machine.config_root == Path("/h/.config")
        assert machine.cache_root == Path("/h/.cache")
        assert machine.toolbox_scripts == Path("/h/.local/share/JetBrains/Toolbox/scripts")
        xdg = jb.Machine("linux", {"XDG_CONFIG_HOME": "/c", "XDG_CACHE_HOME": "/d", "XDG_DATA_HOME": "/e"}, Path("/h"))
        assert (xdg.config_root, xdg.cache_root, xdg.toolbox_scripts) == (
            Path("/c"),
            Path("/d"),
            Path("/e/JetBrains/Toolbox/scripts"),
        )

    def test_macos(self):
        machine = jb.Machine("darwin", {}, Path("/Users/t"))
        assert machine.config_root == Path("/Users/t/Library/Application Support")
        assert machine.cache_root == Path("/Users/t/Library/Caches")
        assert machine.toolbox_scripts == Path("/Users/t/Library/Application Support/JetBrains/Toolbox/scripts")

    def test_windows(self):
        machine = jb.Machine("win32", {"APPDATA": "/roaming", "LOCALAPPDATA": "/local"}, Path("/u"))
        assert machine.config_root == Path("/roaming")
        assert machine.cache_root == Path("/local")
        assert machine.toolbox_scripts == Path("/local/JetBrains/Toolbox/scripts")
        fallback = jb.Machine("win32", {}, Path("/u"))
        assert fallback.config_root == Path("/u/AppData/Roaming")
        assert fallback.cache_root == Path("/u/AppData/Local")


class RecentsTest(FakeHomeTest):
    def test_reads_projects_newest_first_and_expands_the_home_macro(self):
        self.make_project("a")
        self.make_project("b")
        self.write_recents(
            "IntelliJIdea2026.3",
            {
                "$USER_HOME$/a": {"activationTimestamp": 100, "projectOpenTimestamp": 50},
                "$USER_HOME$/b": {"projectOpenTimestamp": 200},
            },
        )
        projects = jb.load_snapshot(self.machine(), {}).projects
        assert [p.name for p in projects] == ["b", "a"]
        assert projects[0].path == str(self.home / "b")
        assert projects[1].last_opened == 100

    def test_skips_hidden_macro_missing_and_undated_entries(self):
        self.make_project("kept")
        self.make_project("undated")
        self.write_recents(
            "IntelliJIdea2026.3",
            {
                "$USER_HOME$/kept": {"projectOpenTimestamp": 1},
                "$USER_HOME$/undated": {},
                "$USER_HOME$/deleted": {"projectOpenTimestamp": 1},
                "$APPLICATION_CONFIG_DIR$/light-edit": {"projectOpenTimestamp": 1, "_attrs": {"hidden": "true"}},
                "$OTHER_MACRO$/x": {"projectOpenTimestamp": 1},
                "/$devcontainer.ij/abc@/IdeaProjects/x": {"projectOpenTimestamp": 1},
            },
        )
        assert [p.name for p in jb.load_snapshot(self.machine(), {}).projects] == ["kept"]

    def test_xml_special_characters_in_paths(self):
        self.make_project("R&D <1>")
        self.write_recents("IntelliJIdea2026.3", {"$USER_HOME$/R&D <1>": {"projectOpenTimestamp": 1}})
        assert [p.name for p in jb.load_snapshot(self.machine(), {}).projects] == ["R&D <1>"]

    def test_merges_versions_keeping_the_latest_use(self):
        self.make_project("both")
        self.make_project("old-only")
        self.write_recents(
            "IntelliJIdea2026.2",
            {"$USER_HOME$/both": {"projectOpenTimestamp": 900}, "$USER_HOME$/old-only": {"projectOpenTimestamp": 1}},
        )
        self.write_recents("IntelliJIdea2026.3", {"$USER_HOME$/both": {"projectOpenTimestamp": 100}})
        projects = jb.load_snapshot(self.machine(), {}).projects
        assert [(p.name, p.last_opened) for p in projects] == [("both", 900), ("old-only", 1)]

    def test_project_used_by_two_ides_appears_once_with_the_latest_ide_first(self):
        self.make_project("shared")
        self.write_recents("IntelliJIdea2026.3", {"$USER_HOME$/shared": {"projectOpenTimestamp": 1}})
        self.write_recents("PyCharm2026.3", {"$USER_HOME$/shared": {"projectOpenTimestamp": 2}})
        projects = jb.load_snapshot(self.machine(), {}).projects
        assert len(projects) == 1
        assert [ide.id for ide in projects[0].ides] == ["pycharm", "idea"]
        assert projects[0].last_opened == 2

    def test_rider_uses_its_own_file_and_component_and_hides_the_solution_suffix(self):
        self.make_project("Shop")
        (self.home / "Shop" / "Shop.sln").write_text("")
        self.write_recents(
            "Rider2026.3",
            {"$USER_HOME$/Shop/Shop.sln": {"projectOpenTimestamp": 1}},
            file="recentSolutions.xml",
            component="RiderRecentProjectsManager",
        )
        [project] = jb.load_snapshot(self.machine(), {}).projects
        assert (project.name, project.ides[0].id) == ("Shop", "rider")

    def test_finds_android_studio_and_editions(self):
        for name in ("a", "b", "c"):
            self.make_project(name)
        self.write_recents("AndroidStudio2024.1", {"$USER_HOME$/a": {"projectOpenTimestamp": 3}}, vendor="Google")
        self.write_recents("IdeaIC2024.1", {"$USER_HOME$/b": {"projectOpenTimestamp": 2}})
        self.write_recents("PyCharmCE2024.1", {"$USER_HOME$/c": {"projectOpenTimestamp": 1}})
        projects = jb.load_snapshot(self.machine(), {}).projects
        assert [p.ides[0].id for p in projects] == ["studio", "idea", "pycharm"]

    def test_ignores_other_jetbrains_folders(self):
        self.make_project("a")
        self.write_recents("IntelliJIdea2026.3-backup", {"$USER_HOME$/a": {"projectOpenTimestamp": 1}})
        self.write_recents("Toolbox", {"$USER_HOME$/a": {"projectOpenTimestamp": 1}})
        assert jb.load_snapshot(self.machine(), {}).projects == []

    def test_a_corrupt_file_is_reported_and_does_not_hide_other_ides(self):
        self.make_project("good")
        self.write_recents("PyCharm2026.3", {"$USER_HOME$/good": {"projectOpenTimestamp": 1}})
        broken = self.home / ".config" / "JetBrains" / "IntelliJIdea2026.3" / "options"
        broken.mkdir(parents=True)
        (broken / "recentProjects.xml").write_text("<application><comp")
        snapshot = jb.load_snapshot(self.machine(), {})
        assert [p.name for p in snapshot.projects] == ["good"]
        assert len(snapshot.errors) == 1
        assert "recentProjects.xml" in snapshot.errors[0]

    def test_finds_versions_with_three_numbers_and_sorts_them(self):
        (self.home / ".config" / "Google" / "AndroidStudio2024.3").mkdir(parents=True)
        newest = self.home / ".config" / "Google" / "AndroidStudio2025.1.2"
        newest.mkdir()
        assert jb.version_dirs(self.home / ".config", jb.IDE_BY_ID["studio"])[0] == newest

    def test_an_unreadable_project_does_not_hide_the_others(self):
        self.make_project("readable")
        locked = self.make_project("locked")
        self.make_project("locked/project")
        self.write_recents(
            "IntelliJIdea2026.3",
            {
                "$USER_HOME$/readable": {"projectOpenTimestamp": 1},
                "$USER_HOME$/locked/project": {"projectOpenTimestamp": 2},
            },
        )
        locked.chmod(0)
        self.addCleanup(locked.chmod, 0o700)
        assert [p.name for p in jb.load_snapshot(self.machine(), {}).projects] == ["readable"]

    def test_module_names_become_aliases(self):
        project = self.make_project("dir")
        (project / ".idea").mkdir()
        (project / ".idea" / "backend-api.iml").write_text("")
        (project / ".idea" / "dir.iml").write_text("")
        self.write_recents("IntelliJIdea2026.3", {"$USER_HOME$/dir": {"projectOpenTimestamp": 1}})
        assert jb.load_snapshot(self.machine(), {}).projects[0].aliases == ("backend-api",)


class LauncherTest(FakeHomeTest):
    idea = jb.IDE_BY_ID["idea"]

    def test_uses_the_install_recorded_by_the_ide(self):
        install = self.install_ide("IntelliJIdea2026.3")
        assert jb.find_launcher(self.idea, self.machine(), {}) == (str(install / "bin" / "idea"),)

    def test_falls_back_to_the_sh_launcher_of_older_installs(self):
        install = self.install_ide("IntelliJIdea2026.3", launcher="idea.sh")
        assert jb.find_launcher(self.idea, self.machine(), {}) == (str(install / "bin" / "idea.sh"),)

    def test_prefers_the_newest_install_and_skips_stale_ones(self):
        self.install_ide("IntelliJIdea2026.2")
        newest = self.install_ide("IntelliJIdea2026.10")
        assert jb.find_launcher(self.idea, self.machine(), {})[0] == str(newest / "bin" / "idea")
        (newest / "bin" / "idea").unlink()
        assert "2026.2" in jb.find_launcher(self.idea, self.machine(), {})[0]

    def test_override_wins(self):
        self.install_ide("IntelliJIdea2026.3")
        assert jb.find_launcher(self.idea, self.machine(), {"idea": "/custom/idea"}) == ("/custom/idea",)

    def test_install_beats_an_unrelated_command_on_the_path(self):
        install = self.install_ide("IntelliJIdea2026.3")
        os.environ["PATH"] = str(self.write_script(self.home / "other" / "idea").parent)
        assert jb.find_launcher(self.idea, self.machine(), {})[0] == str(install / "bin" / "idea")

    def test_falls_back_to_the_path(self):
        script = self.write_script(self.home / "path-bin" / "intellij-idea-ultimate-edition")
        os.environ["PATH"] = str(script.parent)
        assert jb.find_launcher(self.idea, self.machine(), {}) == (str(script),)

    def test_falls_back_to_toolbox_scripts_even_when_not_on_the_path(self):
        script = self.write_script(self.home / ".local" / "share" / "JetBrains" / "Toolbox" / "scripts" / "idea")
        assert jb.find_launcher(self.idea, self.machine(), {}) == (str(script),)

    def test_an_unreadable_install_falls_back_to_the_path(self):
        locked = self.install_ide("IntelliJIdea2026.3").parent
        script = self.write_script(self.home / "path-bin" / "idea")
        os.environ["PATH"] = str(script.parent)
        locked.chmod(0)
        self.addCleanup(locked.chmod, 0o700)
        assert jb.find_launcher(self.idea, self.machine(), {}) == (str(script),)

    def test_windows_batch_launchers_get_their_arguments_quoted(self):
        command = jb.windows_batch_command(("C:\\x\\idea.cmd", "C:\\R&D"))
        assert command == 'cmd.exe /d /s /c ""C:\\x\\idea.cmd" "C:\\R&D""'

    def test_returns_none_when_nothing_is_found(self):
        assert jb.find_launcher(self.idea, self.machine(), {}) is None

    def test_macos_opens_the_app_recorded_in_home_file(self):
        app = self.home / "Applications" / "IntelliJ IDEA.app"
        (app / "Contents").mkdir(parents=True)
        cache = self.home / "Library" / "Caches" / "JetBrains" / "IntelliJIdea2026.3"
        cache.mkdir(parents=True)
        (cache / ".home").write_text(str(app / "Contents"))
        machine = jb.Machine("darwin", {"PATH": ""}, self.home)
        assert jb.find_launcher(self.idea, machine, {}) == ("open", "-na", str(app), "--args")

    def test_macos_finds_the_app_in_usual_folders(self):
        app = self.home / "Applications" / "IntelliJ IDEA CE.app"
        app.mkdir(parents=True)
        machine = jb.Machine("darwin", {"PATH": ""}, self.home)
        assert jb.find_launcher(self.idea, machine, {}) == ("open", "-na", str(app), "--args")

    def test_macos_override_accepts_an_app(self):
        machine = jb.Machine("darwin", {"PATH": ""}, self.home)
        launcher = jb.find_launcher(self.idea, machine, {"idea": "/Applications/Foo.app"})
        assert launcher == ("open", "-na", "/Applications/Foo.app", "--args")

    def test_windows_finds_the_install_in_program_files(self):
        executable = self.home / "pf" / "JetBrains" / "IntelliJ IDEA 2026.3" / "bin" / "idea64.exe"
        executable.parent.mkdir(parents=True)
        executable.write_text("")
        machine = jb.Machine("win32", {"PATH": "", "ProgramFiles": str(self.home / "pf")}, self.home)
        assert jb.find_launcher(self.idea, machine, {}) == (str(executable),)


class PluginTest(FakeHomeTest):
    def setUp(self):
        super().setUp()
        self.project = self.make_project("Dev/fynodoro")
        self.other = self.make_project("Dev/wox-plugin")
        self.install = self.install_ide("IntelliJIdea2026.3")
        now = int(time.time() * 1000)
        self.write_recents(
            "IntelliJIdea2026.3",
            {
                "$USER_HOME$/Dev/fynodoro": {"activationTimestamp": now - 7200000},
                "$USER_HOME$/Dev/wox-plugin": {"activationTimestamp": now - 60000},
            },
        )

    async def test_trigger_with_no_search_lists_projects_by_recency(self):
        plugin, _ = await self.start_plugin()
        results = (await plugin.query(None, make_query(""))).results
        assert [r.title for r in results] == ["wox-plugin", "fynodoro"]
        assert results[0].score > results[1].score
        assert isinstance(results[0].score, int)  # Wox's core decodes the score as an integer.

    async def test_result_row_shows_the_project_and_its_ide_logo(self):
        plugin, _ = await self.start_plugin()
        result = await first_result(plugin, "fyno")
        assert result.title == "fynodoro"
        assert result.sub_title == "~/Dev/fynodoro"
        assert result.identity_key == str(self.project)
        assert (result.icon.image_type, result.icon.image_data) == ("svg", jb.IDE_LOGOS["idea"])
        assert [tail.text for tail in result.tails] == ["2h"]  # Only one IDE, so no IDE name.

    async def test_actions_are_open_copy_and_folder_with_open_as_default(self):
        plugin, _ = await self.start_plugin()
        actions = (await first_result(plugin, "fyno")).actions
        assert [action.name for action in actions] == [
            "Open in IntelliJ IDEA",
            "i18n:action_copy_path",
            "i18n:action_open_folder",
        ]
        assert [action.is_default for action in actions] == [True, False, False]
        assert actions[0].context_data["path"] == str(self.project)
        assert all(action.id == "" for action in actions)  # The host then generates unique ids.
        assert all("var(--wox-theme-icon-color)" in action.icon.image_data for action in actions)

    async def test_open_action_starts_the_launcher_detached_from_home_with_a_clean_env(self):
        plugin, _ = await self.start_plugin()
        os.environ["SHIV_ROOT"] = "/from/the/host"
        action = (await first_result(plugin, "fyno")).actions[0]
        await action.action(None, mock.Mock())
        launcher, cwd, shiv_root, args = (await self.wait_for_call()).strip().split("|")
        assert launcher == str(self.install / "bin" / "idea")
        assert cwd == str(self.home)
        assert shiv_root == ""
        assert args == str(self.project)

    async def test_open_handles_spaces_in_paths(self):
        project = self.make_project("Dev/with space")
        self.write_recents(
            "IntelliJIdea2026.3", {"$USER_HOME$/Dev/with space": {"projectOpenTimestamp": int(time.time() * 1000)}}
        )
        plugin, _ = await self.start_plugin()
        action = (await first_result(plugin, "with space")).actions[0]
        await action.action(None, mock.Mock())
        assert (await self.wait_for_call()).strip().split("|")[3] == str(project)

    async def test_a_second_ide_gets_its_own_open_action_and_a_name_on_the_row(self):
        self.install_ide("PyCharm2026.3", launcher="pycharm")
        self.write_recents(
            "PyCharm2026.3", {"$USER_HOME$/Dev/fynodoro": {"projectOpenTimestamp": int(time.time() * 1000)}}
        )
        plugin, _ = await self.start_plugin()
        result = await first_result(plugin, "fyno")
        assert [tail.text for tail in result.tails] == ["now", "PyCharm"]
        assert [action.name for action in result.actions[:2]] == ["Open in PyCharm", "Open in IntelliJ IDEA"]
        assert [action.is_default for action in result.actions[:2]] == [True, False]
        assert result.icon.image_data == jb.IDE_LOGOS["pycharm"]
        await result.actions[1].action(None, mock.Mock())
        assert str(self.install / "bin" / "idea") in await self.wait_for_call()

    async def test_copy_action(self):
        plugin, api = await self.start_plugin()
        action = (await first_result(plugin, "fyno")).actions[1]
        await action.action(None, mock.Mock())
        assert api.copied == [str(self.project)]

    async def test_open_folder_action(self):
        bin_dir = self.write_script(self.home / "path-bin" / "xdg-open").parent
        os.environ["PATH"] = str(bin_dir)
        plugin, _ = await self.start_plugin()
        action = (await first_result(plugin, "fyno")).actions[2]
        await action.action(None, mock.Mock())
        assert (await self.wait_for_call()).strip().split("|")[3] == str(self.project)

    async def test_open_folder_of_a_solution_file_shows_its_folder(self):
        solution = self.project / "Shop.sln"
        solution.write_text("")
        bin_dir = self.write_script(self.home / "path-bin" / "xdg-open").parent
        os.environ["PATH"] = str(bin_dir)
        await jb.open_folder(str(solution))
        assert (await self.wait_for_call()).strip().split("|")[3] == str(self.project)

    async def test_missing_launcher_warns_on_the_row_and_tells_the_user_where_to_fix_it(self):
        (self.install / "bin" / "idea").unlink()
        plugin, api = await self.start_plugin()
        result = await first_result(plugin, "fyno")
        assert result.tails[-1].text == "i18n:tail_no_launcher"
        await result.actions[0].action(None, mock.Mock())
        assert len(api.notified) == 1
        assert "IntelliJ IDEA" in api.notified[0]
        assert "plugin settings" in api.notified[0]

    async def test_a_launcher_that_fails_right_away_is_reported(self):
        self.write_script(self.install / "bin" / "idea", exit_code=3)
        plugin, api = await self.start_plugin()
        await (await first_result(plugin, "fyno")).actions[0].action(None, mock.Mock())
        assert len(api.notified) == 1
        assert "exited with code 3" in api.notified[0]
        assert len(api.logged) == 1

    async def test_a_launcher_that_cannot_run_is_reported(self):
        plugin, api = await self.start_plugin()
        api.settings = {}
        plugin._on_setting_changed(None, "launchers", json.dumps([{"ide": "idea", "path": "/does/not/exist"}]))
        result = await first_result(plugin, "fyno")
        await result.actions[0].action(None, mock.Mock())
        assert len(api.notified) == 1
        assert "/does/not/exist" in api.notified[0]

    async def test_launcher_that_keeps_running_is_a_success(self):
        script = self.install / "bin" / "idea"
        script.write_text(f'#!/bin/sh\necho "$*" >> "{self.calls_file}"\n/bin/sleep 1\n')
        plugin, api = await self.start_plugin()
        with mock.patch.object(jb, "LAUNCH_CHECK_SECONDS", 0.2):
            await (await first_result(plugin, "fyno")).actions[0].action(None, mock.Mock())
        assert api.notified == []

    async def test_no_match_shows_a_temporary_row_without_identity(self):
        plugin, _ = await self.start_plugin()
        [result] = (await plugin.query(None, make_query("zzzzzz"))).results
        assert result.title == "i18n:no_match_title"
        assert result.identity_key == ""
        assert result.actions == []

    async def test_no_match_only_suggests_path_matching_when_it_is_off(self):
        plugin, _ = await self.start_plugin()
        assert (await first_result(plugin, "zzzzzz")).sub_title == "i18n:no_match_subtitle"
        plugin.match_path = True
        assert (await first_result(plugin, "zzzzzz")).sub_title == ""

    async def test_no_projects_at_all_shows_a_hint(self):
        (self.home / ".config" / "JetBrains" / "IntelliJIdea2026.3" / "options" / "recentProjects.xml").unlink()
        plugin, _ = await self.start_plugin()
        [result] = (await plugin.query(None, make_query(""))).results
        assert result.title == "i18n:empty_title"

    async def test_global_query_matches_names_only_with_a_capped_score(self):
        plugin, _ = await self.start_plugin()
        [result] = (await plugin.query(None, make_query("fynodoro", trigger=""))).results
        assert result.title == "fynodoro"
        assert result.score == 100

    async def test_global_query_stays_quiet_on_noise(self):
        plugin, _ = await self.start_plugin()
        for search in ("", "f", "fyndr", "zzzz", "Dev"):
            assert (await plugin.query(None, make_query(search, trigger=""))).results == [], search

    async def test_global_query_does_not_wait_for_a_reload(self):
        plugin, _ = await self.start_plugin()
        plugin.loaded_at = time.monotonic() - jb.BACKGROUND_REFRESH_SECONDS - 1
        with mock.patch.object(plugin, "_refresh", side_effect=stuck_reload):
            started = time.monotonic()
            await plugin.query(None, make_query("fynodoro", trigger=""))
            assert time.monotonic() - started < 1
            assert plugin.refresh_task is not None
            plugin.refresh_task.cancel()

    async def test_new_projects_appear_once_the_data_is_stale(self):
        plugin, _ = await self.start_plugin()
        self.make_project("Dev/brand-new")
        self.write_recents(
            "PyCharm2026.3", {"$USER_HOME$/Dev/brand-new": {"projectOpenTimestamp": int(time.time() * 1000)}}
        )
        assert (await first_result(plugin, "brand")).title == "i18n:no_match_title"
        plugin.loaded_at = time.monotonic() - jb.FOREGROUND_REFRESH_SECONDS - 1
        assert (await first_result(plugin, "brand")).title == "brand-new"

    async def test_match_path_setting_is_read_and_follows_changes(self):
        plugin, api = await self.start_plugin({"match_path": "true"})
        assert (await first_result(plugin, "Dev")).title == "wox-plugin"
        api.setting_callback(None, "match_path", "false")
        assert (await first_result(plugin, "Dev")).title == "i18n:no_match_title"

    async def test_changing_the_launcher_setting_applies_to_the_next_query(self):
        custom = self.write_script(self.home / "custom" / "my-idea")
        plugin, api = await self.start_plugin()
        api.setting_callback(None, "launchers", json.dumps([{"ide": "idea", "path": str(custom)}]))
        action = (await first_result(plugin, "fyno")).actions[0]
        await action.action(None, mock.Mock())
        assert str(custom) in await self.wait_for_call()

    async def test_mru_restore_rebuilds_the_same_row_without_calling_wox(self):
        plugin, api = await self.start_plugin()
        original = await first_result(plugin, "fyno")
        context = original.actions[0].context_data
        restored = api.mru_callback(None, mock.Mock(context_data=context))
        assert (restored.title, restored.identity_key) == (original.title, original.identity_key)
        assert restored.actions[0].is_default

    async def test_mru_restore_drops_projects_that_are_gone(self):
        _, api = await self.start_plugin()
        data = mock.Mock(context_data={"path": "/gone", "name": "gone", "ide": "idea"})
        assert api.mru_callback(None, data) is None
        assert api.mru_callback(None, mock.Mock(context_data={})) is None

    async def test_mru_restore_before_the_first_load_trusts_its_data_and_can_open(self):
        plugin = jb.JetBrainsProjectsPlugin()
        plugin.api = FakeApi()
        data = mock.Mock(context_data={"path": str(self.project), "name": "fynodoro", "ide": "idea"})
        restored = plugin._on_mru_restore(None, data)
        assert (restored.title, restored.identity_key) == ("fynodoro", str(self.project))
        await restored.actions[0].action(None, mock.Mock())
        assert str(self.project) in await self.wait_for_call()

    async def test_search_tool(self):
        _, api = await self.start_plugin()
        handler = api.tools["search_projects"].handler
        everything = await handler(None, mock.Mock(arguments={}))
        assert [p["name"] for p in everything.output["projects"]] == ["wox-plugin", "fynodoro"]
        assert everything.output["projects"][0]["ides"] == ["idea"]
        found = await handler(None, mock.Mock(arguments={"query": "fyno", "limit": 5}))
        assert [p["path"] for p in found.output["projects"]] == [str(self.project)]
        limited = await handler(None, mock.Mock(arguments={"limit": 1}))
        assert len(limited.output["projects"]) == 1

    async def test_open_tool(self):
        _, api = await self.start_plugin()
        handler = api.tools["open_project"].handler
        result = await handler(None, mock.Mock(arguments={"path": str(self.project)}))
        assert result.output == {"path": str(self.project), "ide": "idea"}
        assert result.error is None
        assert str(self.project) in await self.wait_for_call()

    async def test_open_tool_refuses_unknown_projects_and_reports_missing_launchers(self):
        plugin, api = await self.start_plugin()
        handler = api.tools["open_project"].handler
        unknown = await handler(None, mock.Mock(arguments={"path": "/etc"}))
        assert unknown.error.code == "PROJECT_NOT_FOUND"
        (self.install / "bin" / "idea").unlink()
        plugin.loaded_at = 0.0
        missing = await handler(None, mock.Mock(arguments={"path": str(self.project)}))
        assert missing.error.code == "LAUNCHER_NOT_FOUND"

    async def test_open_tool_finds_an_installed_ide_that_has_no_recent_project(self):
        pycharm = self.install_ide("PyCharm2026.3", launcher="pycharm")
        _, api = await self.start_plugin()
        result = await api.tools["open_project"].handler(
            None, mock.Mock(arguments={"path": str(self.project), "ide": "pycharm"})
        )
        assert result.output == {"path": str(self.project), "ide": "pycharm"}
        assert str(pycharm / "bin" / "pycharm") in await self.wait_for_call()

    async def test_rows_point_to_cached_logos_when_the_cache_is_available(self):
        cache = self.make_project("wox-cache")
        plugin, _ = await self.start_plugin(cache_folder=cache)
        icon = (await first_result(plugin, "fyno")).icon
        assert (icon.image_type, icon.image_data) == ("absolute", str(cache / "idea.svg"))
        assert (cache / "idea.svg").read_text(encoding="utf-8") == jb.IDE_LOGOS["idea"]

    async def test_rows_carry_their_logo_when_the_cache_cannot_be_written(self):
        plugin, api = await self.start_plugin(cache_folder=self.home / "no-such-folder")
        assert (await first_result(plugin, "fyno")).icon.image_data == jb.IDE_LOGOS["idea"]
        assert "cannot cache the logos" in api.logged[0][1]

    async def test_a_failed_first_load_stays_unloaded_and_keeps_mru_rows(self):
        with mock.patch.object(jb, "load_snapshot", side_effect=RuntimeError("boom")):
            plugin, api = await self.start_plugin()
        assert plugin.loaded_at == 0.0
        assert not plugin.snapshot.loaded
        restored = api.mru_callback(None, mock.Mock(context_data={"path": str(self.project), "ide": "idea"}))
        assert restored.title == "fynodoro"
        assert restored.tails == []

    async def test_a_setting_changed_during_a_load_keeps_the_data_stale(self):
        plugin, _ = await self.start_plugin()
        plugin.loaded_at = 0.0

        def change_setting_while_loading(*_):
            plugin._on_setting_changed(None, "launchers", "[]")
            return jb.Snapshot(loaded=True)

        with mock.patch.object(jb, "load_snapshot", side_effect=change_setting_while_loading):
            await plugin._refresh(None)
        assert plugin.loaded_at == 0.0

    async def test_a_stuck_reload_does_not_hang_a_query(self):
        plugin, _ = await self.start_plugin()
        plugin.loaded_at = 0.0
        with (
            mock.patch.object(jb, "REFRESH_WAIT_SECONDS", 0.05),
            mock.patch.object(plugin, "_refresh", side_effect=stuck_reload),
        ):
            assert (await first_result(plugin, "fyno")).title == "fynodoro"
            assert not plugin.refresh_task.done()
            plugin.refresh_task.cancel()

    async def test_tools_declare_their_side_effects(self):
        _, api = await self.start_plugin()
        search = api.tools["search_projects"].tool.annotations
        assert search.read_only
        assert search.idempotent
        assert not search.requires_ui
        assert api.tools["open_project"].tool.annotations.requires_ui

    async def test_a_failing_reload_keeps_serving_the_last_good_data(self):
        plugin, api = await self.start_plugin()
        plugin.loaded_at = 0.0
        with mock.patch.object(jb, "load_snapshot", side_effect=RuntimeError("boom")):
            results = (await plugin.query(None, make_query("fyno"))).results
        assert results[0].title == "fynodoro"
        assert "boom" in api.logged[-1][1]


if __name__ == "__main__":
    unittest.main()
