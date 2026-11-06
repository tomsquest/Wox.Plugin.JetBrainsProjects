# {
#   "Id": "7a8cc425-3b7f-489c-8cac-1294cf61c19b",
#   "Name": "JetBrains Projects",
#   "Author": "tomsquest",
#   "Version": "1.0.0",
#   "MinWoxVersion": "2.4.5",
#   "Runtime": "PYTHON",
#   "Description": "Search the recent projects of your JetBrains IDEs and open them",
#   "Icon": "svg:<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"64\" height=\"64\" fill=\"none\" viewBox=\"0 0 64 64\"><defs><linearGradient id=\"a\" x1=\"-.390625\" x2=\"24.3925\" y1=\"7.67063\" y2=\"61.1256\" gradientUnits=\"userSpaceOnUse\"><stop offset=\".1\" stop-color=\"#FC801D\"/><stop offset=\".59\" stop-color=\"#FE2857\"/></linearGradient><linearGradient id=\"b\" x1=\"4.32509\" x2=\"62.9207\" y1=\"59.9325\" y2=\"1.33625\" gradientUnits=\"userSpaceOnUse\"><stop offset=\".21\" stop-color=\"#FE2857\"/><stop offset=\".7\" stop-color=\"#007EFF\"/></linearGradient></defs><path fill=\"#FF8100\" d=\"M16.4501 6H4.19132C1.88757 6 .03007 7.88688.066946 10.1906l.17625 11.0431C.261946 22.415.786321 23.5312 1.6832 24.3l38.1587 32.7069c.7475.6406 1.7.9931 2.6844.9931h11.3494c2.2781 0 4.125-1.8469 4.125-4.125V42.8719c0-1.1894-.5138-2.3213-1.4088-3.1044L19.1663 7.02063C18.4144 6.3625 17.4494 6 16.4501 6Z\"/><path fill=\"url(#a)\" d=\"M14.9875 6H4.125C1.84687 6 0 7.84687 0 10.125v12.5656c0 .2.014375.4.04375.5981l5.44813 37.1851c.29687 2.0256 2.03437 3.5268 4.08124 3.5268H24.9706c2.2788 0 4.1256-1.8475 4.125-4.1262L29.0912 41.37c0-.4256-.0662-.8488-.1956-1.2538L18.9169 8.87062c-.5463-1.70937-2.135-2.86999-3.9294-2.86999V6Z\"/><path fill=\"url(#b)\" d=\"M59.8757 0H25.7482c-1.6581 0-3.155.993125-3.8 2.52063L6.15071 39.9419c-.21875.5181-.32938 1.0756-.32438 1.6381l.15 18.3287C5.99508 62.1737 7.83633 64 10.1013 64H27.767c.8056 0 1.5931-.2356 2.2662-.6781l32.1094-21.1088c1.1606-.7625 1.8587-2.0581 1.8587-3.4468V4.125c0-2.27813-1.8468-4.125-4.125-4.125h-.0006Z\"/><path fill=\"#000\" d=\"M52 12H12v40h40V12Z\"/><path fill=\"#fff\" d=\"M33 44H17v3h16v-3Z\"/><path fill=\"#fff\" d=\"M17 29.3834h2.98v-9.7756H17v-2.6156h8.8431v2.6156h-2.98v9.7756h2.98v2.6157H17v-2.6157Z\"/><path fill=\"#fff\" d=\"M27.6426 29.2978h2.1544c.4356 0 .8237-.0925 1.1631-.2787.3394-.1857.6019-.4482.7881-.7882.1856-.3393.2788-.7268.2788-1.1631V16.9922h2.9262v10.2794c0 .9006-.2075 1.7093-.6219 2.4275-.4143.7181-.9862 1.2806-1.715 1.6881-.7287.4075-1.5468.6112-2.4543.6112h-2.5188v-2.7012l-.0006.0006Z\"/></svg>",
#   "TriggerKeywords": ["jb"],
#   "SupportedOS": ["Windows", "Linux", "Macos"],
#   "Features": [
#     { "Name": "ignoreAutoScore" },
#     { "Name": "mru", "Params": { "HashBy": "identityKey" } }
#   ],
#   "SettingDefinitions": [
#     {
#       "Type": "checkbox",
#       "Value": {
#         "Key": "match_path",
#         "Label": "i18n:setting_match_path",
#         "Tooltip": "i18n:setting_match_path_tip",
#         "DefaultValue": "false"
#       }
#     },
#     {
#       "Type": "table",
#       "IsPlatformSpecific": true,
#       "Value": {
#         "Key": "launchers",
#         "Title": "i18n:setting_launchers",
#         "Tooltip": "i18n:setting_launchers_tip",
#         "DefaultValue": "[]",
#         "Columns": [
#           {
#             "Key": "ide",
#             "Label": "i18n:setting_column_ide",
#             "Type": "select",
#             "Width": 160,
#             "Validators": [{ "Type": "not_empty", "Value": {} }],
#             "SelectOptions": [
#               { "Label": "Android Studio", "Value": "studio" },
#               { "Label": "Aqua", "Value": "aqua" },
#               { "Label": "CLion", "Value": "clion" },
#               { "Label": "DataGrip", "Value": "datagrip" },
#               { "Label": "DataSpell", "Value": "dataspell" },
#               { "Label": "GoLand", "Value": "goland" },
#               { "Label": "IntelliJ IDEA", "Value": "idea" },
#               { "Label": "PhpStorm", "Value": "phpstorm" },
#               { "Label": "PyCharm", "Value": "pycharm" },
#               { "Label": "Rider", "Value": "rider" },
#               { "Label": "RubyMine", "Value": "rubymine" },
#               { "Label": "RustRover", "Value": "rustrover" },
#               { "Label": "WebStorm", "Value": "webstorm" },
#               { "Label": "Writerside", "Value": "writerside" }
#             ]
#           },
#           {
#             "Key": "path",
#             "Label": "i18n:setting_column_path",
#             "Type": "filePath",
#             "Validators": [{ "Type": "not_empty", "Value": {} }]
#           }
#         ]
#       }
#     }
#   ],
#   "I18n": {
#     "en_US": {
#       "action_open_in": "Open in {ide}",
#       "action_copy_path": "Copy path",
#       "action_open_folder": "Open folder",
#       "empty_title": "No JetBrains projects found",
#       "empty_subtitle": "Open a project in a JetBrains IDE, then search again",
#       "no_match_title": "No matching project",
#       "no_match_subtitle": "Turn on path matching in the plugin settings to search folders too",
#       "tail_no_launcher": "No launcher",
#       "launcher_missing": "No launcher found for {ide}. Set its path in the JetBrains Projects plugin settings.",
#       "open_failed": "Could not open {target}: {error}",
#       "setting_match_path": "Match project paths",
#       "setting_match_path_tip": "In jb queries, search the project path as well as its name.",
#       "setting_launchers": "IDE launchers",
#       "setting_launchers_tip": "Only needed when the plugin cannot find an IDE by itself.",
#       "setting_column_ide": "IDE",
#       "setting_column_path": "Launcher path",
#       "tool_search": "Search recent JetBrains projects by name, most recent first. Read-only.",
#       "tool_open": "Open a recent JetBrains project in its IDE. Opens a window."
#     },
#     "zh_CN": {
#       "action_open_in": "在 {ide} 中打开",
#       "action_copy_path": "复制路径",
#       "action_open_folder": "打开文件夹",
#       "empty_title": "未找到 JetBrains 项目",
#       "empty_subtitle": "请先在 JetBrains IDE 中打开项目，然后重新搜索",
#       "no_match_title": "没有匹配的项目",
#       "no_match_subtitle": "可在插件设置中开启路径匹配，以同时搜索文件夹",
#       "tail_no_launcher": "无启动器",
#       "launcher_missing": "未找到 {ide} 的启动器。请在 JetBrains Projects 插件设置中填写其路径。",
#       "open_failed": "无法打开 {target}：{error}",
#       "setting_match_path": "匹配项目路径",
#       "setting_match_path_tip": "在 jb 查询中，除项目名称外也搜索项目路径。",
#       "setting_launchers": "IDE 启动器",
#       "setting_launchers_tip": "仅在插件无法自动找到 IDE 时需要设置。",
#       "setting_column_ide": "IDE",
#       "setting_column_path": "启动器路径",
#       "tool_search": "按名称搜索最近的 JetBrains 项目，最近使用的排在最前。只读。",
#       "tool_open": "在对应的 IDE 中打开最近的 JetBrains 项目。会打开窗口。"
#     }
#   }
# }

"""Search the recent projects of your JetBrains IDEs and open them.

Projects come from each IDE's recentProjects.xml. An IDE's launcher comes from,
in order: the plugin settings, the install folder the IDE records in its `.home`
file, the PATH and Toolbox scripts, then the usual macOS and Windows folders.

The IDE table, the IDE logos and the Rider file format come from albert-plugin-python-jetbrains-projects
(MIT, https://github.com/albertlauncher/albert-plugin-python-jetbrains-projects), Copyright (c) 2024 Manuel Schneider,
2018-2023 Thomas Queste, 2023 Valentin Maerten. The logos themselves belong to JetBrains and Google.
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from wox_plugin import (
    ActionContext,
    Context,
    CopyParams,
    InvokePluginToolHandlerOption,
    InvokePluginToolHandlerResult,
    LogLevel,
    MRUData,
    PluginInitParams,
    PluginToolAnnotations,
    PluginToolDescriptor,
    PluginToolError,
    Query,
    QueryResponse,
    RegisterPluginToolOption,
    Result,
    ResultAction,
    ResultTail,
    ResultTailTextCategory,
    WoxImage,
)

if TYPE_CHECKING:
    from collections.abc import Mapping

FOREGROUND_REFRESH_SECONDS = 5  # A jb query waits for fresh data when it is older than this.
BACKGROUND_REFRESH_SECONDS = 60  # A global query never waits: it refreshes behind the scenes.
LAUNCH_CHECK_SECONDS = 3  # A launcher still running after this long is assumed to have worked.

GLOBAL_MIN_SEARCH_LENGTH = 2
GLOBAL_MIN_SCORE = 60  # Keeps fuzzy matches out of global search, where they would be noise.
PATH_MATCH_SCORE = 40  # Below any match on the name, so names always rank first.
FUZZY_MAX_SPREAD = 3  # A fuzzy match may span at most this many characters per search character.

SOLUTION_SUFFIXES = {".sln", ".slnx"}
UNRESOLVED_MACRO = re.compile(r"\$\w+\$")

ICON_OPEN = WoxImage.new_svg(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
    'stroke="var(--wox-theme-icon-color)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M14 5h5v5M19 5l-9 9"/><path d="M13 7H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2v-7"/></svg>'
)
ICON_COPY = WoxImage.new_svg(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
    'stroke="var(--wox-theme-icon-color)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="8" y="8" width="12" height="12" rx="2"/>'
    '<path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/></svg>'
)
ICON_FOLDER = WoxImage.new_svg(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
    'stroke="var(--wox-theme-icon-color)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>'
)


@dataclass(frozen=True)
class Ide:
    """A JetBrains IDE, and where to find its recent projects and launcher."""

    id: str  # Stable id, and the launcher's base name inside the install's bin folder.
    name: str
    config_prefixes: tuple[str, ...]  # "<vendor>/<product>", followed on disk by a version.
    commands: tuple[str, ...]  # Names to look for on the PATH.
    recents_file: str = "recentProjects.xml"
    recents_component: str = "RecentProjectsManager"


def _jetbrains_ide(ide_id: str, name: str, **options: str) -> Ide:
    """Declare an IDE that follows the naming convention shared by most JetBrains products."""
    return Ide(ide_id, name, (f"JetBrains/{name.replace(' ', '')}",), (ide_id, f"{ide_id}-eap"), **options)


IDES = (
    Ide(
        "studio",
        "Android Studio",
        ("Google/AndroidStudio",),
        (
            "studio",
            "androidstudio",
            "android-studio",
            "android-studio-canary",
            "jdk-android-studio",
            "android-studio-system-jdk",
        ),
    ),
    _jetbrains_ide("aqua", "Aqua"),
    _jetbrains_ide("clion", "CLion"),
    _jetbrains_ide("datagrip", "DataGrip"),
    _jetbrains_ide("dataspell", "DataSpell"),
    _jetbrains_ide("goland", "GoLand"),
    Ide(
        "idea",
        "IntelliJ IDEA",
        ("JetBrains/IntelliJIdea", "JetBrains/Idea"),
        (
            "idea",
            "idea.sh",
            "idea-ultimate",
            "idea-ce-eap",
            "idea-ue-eap",
            "intellij-idea-ce",
            "intellij-idea-ce-eap",
            "intellij-idea-ue-bundled-jre",
            "intellij-idea-ultimate-edition",
            "intellij-idea-community-edition-jre",
            "intellij-idea-community-edition-no-jre",
        ),
    ),
    _jetbrains_ide("phpstorm", "PhpStorm"),
    Ide(
        "pycharm",
        "PyCharm",
        ("JetBrains/PyCharm",),
        ("pycharm", "charm", "pycharm-eap", "pycharm-professional"),
    ),
    # Rider keeps its recents in its own file, under its own component name.
    _jetbrains_ide(
        "rider", "Rider", recents_file="recentSolutions.xml", recents_component="RiderRecentProjectsManager"
    ),
    Ide(
        "rubymine",
        "RubyMine",
        ("JetBrains/RubyMine",),
        ("rubymine", "rubymine-eap", "jetbrains-rubymine", "jetbrains-rubymine-eap"),
    ),
    _jetbrains_ide("rustrover", "RustRover"),
    _jetbrains_ide("webstorm", "WebStorm"),
    _jetbrains_ide("writerside", "Writerside"),
)
IDE_BY_ID = {ide.id: ide for ide in IDES}

IDE_LOGOS = {
    "studio": '<svg width="128" height="128" fill="none" xmlns="http://www.w3.org/2000/svg"><path opacity=".2" d="M49.853 123.492c-1.978-.469-3.634-1.566-5.95-3.943-3.871-3.971-7.013-5.624-12.472-6.564-5.664-.975-8.18-3.08-9.694-8.108-1.867-6.206-3.82-9.178-8.108-12.346-4.866-3.594-6.114-6.764-4.927-12.507 1.1-5.32.679-9.101-1.555-13.964C4.48 60.26 4.81 57.16 8.597 52.405c3.47-4.357 4.56-7.238 5.079-13.431.524-6.25 2.263-8.815 7.385-10.89 4.274-1.732 7.93-4.739 9.958-8.188 2.344-3.99 2.686-4.447 4.139-5.53 2.344-1.749 4.239-2.233 7.848-2.007 6.27.393 9.63-.36 13.84-3.1 5.49-3.574 8.818-3.574 14.307 0 4.21 2.74 7.57 3.493 13.84 3.1 5.929-.372 8.396 1.184 12.01 7.577 1.79 3.167 5.451 6.25 9.458 7.965 5.706 2.442 7.364 4.67 7.785 10.463.456 6.273 1.742 9.78 5.149 14.041 3.794 4.745 4.125 7.848 1.457 13.655-2.233 4.863-2.655 8.645-1.555 13.964 1.188 5.743-.061 8.913-4.926 12.507-4.289 3.167-6.241 6.14-8.109 12.346-1.513 5.028-4.03 7.133-9.694 8.108-5.47.942-8.615 2.6-12.47 6.577-4.275 4.407-7.339 5.135-13.314 3.159-4.887-1.615-8.65-1.622-13.517-.024-3.41 1.119-5.227 1.314-7.414.795Z" fill="#000"/><path d="M49.853 122.321c-1.978-.47-3.634-1.567-5.95-3.944-3.871-3.97-7.013-5.624-12.472-6.563-5.664-.975-8.18-3.081-9.694-8.108-1.867-6.207-3.82-9.18-8.108-12.347-4.866-3.594-6.114-6.763-4.927-12.507 1.1-5.32.679-9.101-1.555-13.964-2.666-5.801-2.337-8.901 1.45-13.655 3.47-4.357 4.56-7.237 5.079-13.431.524-6.25 2.263-8.815 7.385-10.89 4.274-1.732 7.93-4.739 9.958-8.188 2.344-3.99 2.686-4.446 4.139-5.53 2.344-1.749 4.239-2.233 7.848-2.007 6.27.393 9.63-.36 13.84-3.1 5.49-3.574 8.818-3.574 14.307 0 4.21 2.74 7.57 3.493 13.84 3.1 5.929-.372 8.396 1.184 12.01 7.577 1.79 3.167 5.451 6.25 9.458 7.965 5.706 2.442 7.364 4.67 7.785 10.463.456 6.273 1.742 9.78 5.149 14.041 3.794 4.745 4.125 7.848 1.457 13.655-2.233 4.863-2.655 8.645-1.555 13.964 1.188 5.743-.061 8.913-4.926 12.507-4.289 3.168-6.241 6.14-8.109 12.347-1.513 5.027-4.03 7.133-9.694 8.108-5.47.941-8.615 2.6-12.47 6.576-4.275 4.408-7.339 5.135-13.314 3.16-4.887-1.616-8.65-1.623-13.517-.025-3.41 1.119-5.227 1.314-7.414.796Z" fill="#fff"/><path d="M90.847 99.018a1.462 1.462 0 0 1-2.68 1.137l-3.522-6.538a2.152 2.152 0 1 1 3.945-1.675l2.257 7.076Z" fill="#034ECA"/><path d="M90.847 99.018a1.462 1.462 0 0 1-2.68 1.137l-3.522-6.538a2.152 2.152 0 1 1 3.945-1.675l2.257 7.076Z" fill="url(#a)"/><mask id="b" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="78" y="51" width="21" height="26"><path d="M88.095 75.55a12.443 12.443 0 0 0 3.382-3.272 12.496 12.496 0 0 0 1.42-2.646c.234-.599.422-1.217.562-1.847l.028.005 1.478.278a2295.78 2295.78 0 0 0 2.48.467 1.146 1.146 0 0 0 1.32-1.41 1.156 1.156 0 0 0-.163-.358 1.144 1.144 0 0 0-.733-.478c-.345-.066-.691-.13-1.037-.195l-1.443-.272-1.478-.279-.162-.03.004-.122c.037-1.48-.19-2.992-.713-4.472l-.044-.12a12.483 12.483 0 0 0-2.274-3.881l.1-.117.975-1.143.953-1.116.685-.802a1.14 1.14 0 0 0-.139-1.62 1.14 1.14 0 0 0-1.604.137l-.684.802-.953 1.116-.976 1.143-.008.01a12.59 12.59 0 0 0-6.087-2.635 12.477 12.477 0 0 0-4.617.207l8.288 23.458a12.56 12.56 0 0 0 1.44-.809Z" fill="#fff"/></mask><g mask="url(#b)"><path d="m100.745 71.537-8.84-25.05-14.093 4.973 8.84 25.05 14.093-4.973Z" fill="#4FAF53"/><g opacity=".8" filter="url(#c)"><path d="M92.34 62.13c-.875 3.1-3.533-3.82-8.313-5.169-4.78-1.349-10.664 3.16-9.789.06 1.562-2.275 5.744-4.013 10.524-2.664 4.78 1.35 7.62 5.39 7.578 7.773Z" fill="url(#d)" fill-opacity=".3"/></g><g opacity=".7" filter="url(#e)"><path d="M91.738 60.426c-2.627-1.865-.354 5.19-3.228 9.24-2.875 4.05-10.286 4.233-7.659 6.097 2.644.791 6.99-.48 9.865-4.53 2.875-4.05 2.55-8.978 1.022-10.807Z" fill="url(#f)" fill-opacity=".4"/></g><g opacity=".6" filter="url(#g)"><path d="M81.522 51.431c-3.337.105-6.032.504-6.02.891.013.387 2.727.616 6.064.51 3.337-.104 7.996 2.675 7.984 2.288-.012-.387-4.691-3.793-8.028-3.689Z" fill="#8BD8A0"/></g><g opacity=".5" filter="url(#h)"><path d="M89.978 75.393c-2.663 2.013-5.012 3.394-5.245 3.085-.234-.31 1.736-2.191 4.4-4.204 2.664-2.012 4.547-7.1 4.78-6.791.234.309-1.271 5.898-3.935 7.91Z" fill="#8BD8A0"/></g><g opacity=".7" filter="url(#i)"><path d="M91.21 53.386c-1.219 1.492-1.812 2.166-1.944 2.058-.132-.107.248-.956 1.466-2.448.75-1.87 2.98-.96 3.113-.852.132.108-1.076-.887-2.636 1.242Z" fill="#0D652D"/></g><g opacity=".1" filter="url(#j)"><path d="M89.034 55.32c.113.086 1.015-.903 2.013-2.21 1-1.306 1.716-2.436 1.603-2.523-.114-.087-1.015.902-2.014 2.21-.999 1.306-1.716 2.436-1.602 2.522Z" fill="#000"/></g><g opacity=".3" filter="url(#k)"><path d="M92.414 54.285c-1.274 1.561-1.847 2.305-1.742 2.392.106.086.85-.519 2.124-2.08 1.831-1.717-.068-2.979-.245-2.726-.519.555 1.692.348-.137 2.414Z" fill="#fff"/></g><path opacity=".15" d="M91.83 50.843c-.553.395-.624 1.243-.158 1.894.465.65 1.29.857 1.844.462.552-.396.623-1.244.158-1.895-.465-.65-1.291-.857-1.844-.461Z" fill="url(#l)" fill-opacity=".9"/><path opacity=".15" d="M97.296 65.762c-.552.396-.623 1.244-.158 1.895.465.65 1.291.857 1.844.462.553-.396.624-1.244.158-1.895-.465-.65-1.29-.857-1.844-.462Z" fill="url(#m)" fill-opacity=".9"/><g opacity=".1" filter="url(#n)"><path d="M93.33 67.75c.03-.14 1.356.043 2.96.408 1.604.365 2.878.773 2.846.913-.031.14-1.357-.043-2.96-.408-1.604-.365-2.879-.773-2.847-.913Z" fill="#000"/></g><mask id="o" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="93" y="65" width="3" height="5"><path d="M93.37 67.938c.15-.678.298-2.157.353-2.812l1.453-.093-.18 4.167c-.605-.138-1.776-.584-1.626-1.262Z" fill="#000"/></mask><g mask="url(#o)"><g style="mix-blend-mode:multiply" opacity=".3" filter="url(#p)"><path d="M93.702 68.237c.07-1.142.01-2.076-.133-2.084-.142-.01-.225.868-.295 2.01-.07 1.143-.099 2.118.044 2.127.142.009.314-.91.384-2.053Z" fill="#0D652D"/></g><g style="mix-blend-mode:screen" opacity=".3" filter="url(#q)"><path d="M93.776 65.922c.039-.325.019-.594-.045-.602-.063-.007-.106.241-.144.566-.039.325-.058.604.005.611.064.008.146-.25.184-.575Z" fill="#81C995"/></g></g><mask id="r" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="88" y="53" width="4" height="5"><path d="M88.735 55.151c.552.422 1.617 1.46 2.08 1.926l1.172-.864-2.82-3.074c-.374.495-.983 1.59-.432 2.012Z" fill="#000"/></mask><g mask="url(#r)"><g style="mix-blend-mode:multiply" opacity=".3" filter="url(#s)"><path d="M88.797 54.71c.788.829 1.343 1.582 1.24 1.68-.104.099-.732-.52-1.52-1.35-.79-.83-1.44-1.556-1.336-1.655.104-.098.827.495 1.616 1.324Z" fill="#0D652D"/></g><g style="mix-blend-mode:screen" opacity=".3" filter="url(#t)"><path d="M90.344 56.432c.238.224.396.444.352.49-.044.047-.236-.116-.475-.34-.238-.224-.432-.425-.389-.471.044-.047.273.097.512.321Z" fill="#81C995"/></g></g><g opacity=".7" filter="url(#u)"><path d="M96.294 68.007c-1.894-.354-2.782-.485-2.813-.318-.032.168.806.57 2.7.924 1.78.943 2.896-1.192 2.927-1.36.031-.167-.249 1.372-2.814.754Z" fill="#0D652D"/></g><g opacity=".3" filter="url(#v)"><path d="M96.623 66.49c-1.927-.36-2.82-.555-2.794-.695.027-.14.962-.174 2.889.185 3.152.072 3.521 2.29 1.88 2.484-.72-.05.683-1.597-1.975-1.975Z" fill="#fff"/></g></g><path d="M85.353 57.695c-.158.386-.114.768.097.855.212.086.511-.156.669-.541.158-.385.114-.768-.097-.854-.212-.087-.511.155-.669.54Z" fill="url(#w)" fill-opacity=".7"/><path d="M89.055 68.227c-.365-.2-.57-.525-.46-.726.11-.2.494-.199.859.002.364.2.57.526.46.726-.11.2-.495.2-.86-.002Z" fill="url(#x)" fill-opacity=".7"/><g style="mix-blend-mode:multiply" opacity=".09" filter="url(#y)"><path d="M84.336 58.813c1 .044 1.414-.52 1.495-.807.585-.95-.365-1.62-.809-1.763-.443-.143-1.196-.312-1.91.364-.712.676-.026 2.15 1.224 2.206Z" fill="#011B04"/></g><g style="mix-blend-mode:multiply" opacity=".09" filter="url(#z)"><path d="M87.562 67.997c.747-.66 1.42-.48 1.662-.307 1.048.376.732 1.49.478 1.88-.253.39-.73.993-1.705.913-.975-.08-1.368-1.66-.435-2.486Z" fill="#011B04"/></g><path d="M87.718 70.192c.56.42 1.427.215 1.936-.46.508-.676.465-1.564-.096-1.986-.561-.42-1.428-.215-1.936.46-.508.676-.465 1.565.096 1.986Z" fill="#000"/><g filter="url(#A)"><path d="M84.263 58.605c.82.207 1.621-.163 1.79-.827.168-.664-.36-1.37-1.18-1.577-.82-.207-1.622.163-1.79.827-.168.664.36 1.37 1.18 1.577Z" fill="#000"/></g><g filter="url(#B)"><path d="M87.638 68.2c.508-.675 1.364-.889 1.912-.478.548.411.58 1.292.072 1.967-.507.675-1.363.889-1.911.478-.548-.412-.58-1.292-.073-1.967Z" fill="#000"/></g><mask id="C" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="83" y="56" width="4" height="3"><path d="M84.263 58.605c.82.207 1.621-.163 1.79-.827.168-.664-.36-1.37-1.18-1.577-.82-.207-1.621.163-1.79.827-.168.663.36 1.37 1.18 1.577Z" fill="#202124"/></mask><g mask="url(#C)"><g filter="url(#D)"><path d="M84.963 56.346c-.667-.24-1.287-.074-1.526.068.464-.283.969-.418 1.605-.183.35.13.622.419.783.643a.981.981 0 0 1 .067.1c.037.059.064.108.08.144-.025-.04-.047-.089-.08-.144a2.167 2.167 0 0 0-.067-.1c-.12-.154-.344-.342-.862-.528Z" fill="#D8D8D8" fill-opacity=".29"/></g><g opacity=".8" filter="url(#E)"><path d="M85.508 58.295c.67-.433.536-1.057.385-1.315.188.202.208.678.064.932-.115.204-.347.34-.449.383Z" fill="url(#F)"/></g></g><mask id="G" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="87" y="67" width="3" height="4"><path d="M87.64 68.2c.507-.675 1.363-.889 1.911-.478.548.411.58 1.292.073 1.967-.508.675-1.364.889-1.912.478-.548-.412-.58-1.292-.073-1.967Z" fill="#202124"/></mask><g mask="url(#G)"><path d="M89.72 68.247a.932.932 0 0 0-1.073-.587c.171.011.566.127.779.498.212.37-.057 1.057-.219 1.354l.29.12c.183-.206.484-.77.223-1.385Z" fill="url(#H)"/><g filter="url(#I)"><path d="M89.596 69.523c-.368.604-.955.865-1.23.904.539-.07 1.016-.283 1.364-.864.191-.32.22-.716.205-.992a.947.947 0 0 0-.01-.12 1.317 1.317 0 0 0-.028-.162c.006.046.019.098.028.162.004.036.008.077.01.12.004.195-.052.482-.339.952Z" fill="#D8D8D8" fill-opacity=".29"/></g></g><g opacity=".8" filter="url(#J)"><path d="M85.359 56.834c-.136-.228-.459-.321-.603-.34l-.141.188c.048.006.178.034.31.098.133.064.292.173.354.22l.08-.166Z" fill="#E2DCE1"/></g><g opacity=".8" filter="url(#K)"><path d="M89.603 68.904c.038.26-.145.529-.241.631l-.22-.059c.032-.034.112-.135.172-.265.06-.13.11-.312.128-.387l.16.08Z" fill="#E2DCE1"/></g><g opacity=".8" filter="url(#L)" fill="#E2DCE1"><path d="M84.386 58.31a5.615 5.615 0 0 1-.317-.312l-.237.001c.124.164.28.264.341.294l.213.018ZM85.445 58.35a1.21 1.21 0 0 0 .159-.138l-.083.03a.988.988 0 0 1-.204.154.27.27 0 0 0 .129-.045Z"/></g><g opacity=".8" filter="url(#M)" fill="#E2DCE1"><path d="M87.905 68.342a5.526 5.526 0 0 0-.05.443l-.186.148c-.007-.205.051-.38.081-.443l.155-.148ZM88.704 67.646c.064-.006.167.003.21.009l-.083.03a.97.97 0 0 0-.256.007.268.268 0 0 1 .129-.046Z"/></g><g opacity=".3" filter="url(#N)"><path d="M90.184 71.894c-3.038 1.072 1.085-5.089-.568-9.772-1.653-4.684-8.73-6.892-5.69-7.965 2.758-.035 6.589 2.381 8.242 7.065 1.652 4.683-.013 9.333-1.984 10.672Z" fill="url(#O)" fill-opacity=".4"/></g><g opacity=".2" filter="url(#P)"><path d="M90.184 71.894c-3.038 1.072 1.085-5.089-.568-9.772-1.653-4.684-8.73-6.892-5.69-7.965 2.758-.035 6.589 2.381 8.242 7.065 1.652 4.683-.013 9.333-1.984 10.672Z" fill="url(#Q)" fill-opacity=".4"/></g><path d="M39.433 59.174c-.651-1.15-1.766-1.975-3.099-2.294-1.333-.32-2.775-.106-4.009.593-1.234.699-2.159 1.825-2.571 3.133-.413 1.307-.166 2.885.485 4.035l4.755-2.454 4.439-3.013Z" fill="#4386F5"/><path fill-rule="evenodd" clip-rule="evenodd" d="M39.39 59.103c6.882 11.394 21.289 16.269 33.88 10.888l4.203 9.836c-17.563 7.505-37.638.7-47.239-15.193l9.155-5.53Z" fill="url(#R)"/><path d="M37.378 99.018a1.462 1.462 0 0 0 2.68 1.137l3.522-6.538a2.152 2.152 0 1 0-3.945-1.675l-2.257 7.076Z" fill="#034ECA"/><path d="M37.378 99.018a1.462 1.462 0 0 0 2.68 1.137l3.522-6.538a2.152 2.152 0 1 0-3.945-1.675l-2.257 7.076Z" fill="url(#S)"/><path d="M55.347 37.37a6.055 6.055 0 1 1 11.38 4.142l-17.77 48.82a6.055 6.055 0 1 1-11.379-4.141l17.769-48.82Z" fill="#4285F4"/><path d="M42.813 94.285a6.036 6.036 0 0 0 6.28-3.94l14.434-39.656a6.035 6.035 0 0 0-1.57-6.492L42.813 94.285Z" fill="url(#T)"/><path d="M67.924 26.35a3.809 3.809 0 1 0-7.617 0v7.227a3.809 3.809 0 1 0 7.617 0V26.35Z" fill="#4285F4"/><path d="M67.924 26.35a3.809 3.809 0 1 0-7.617 0v7.227a3.809 3.809 0 1 0 7.617 0V26.35Z" fill="url(#U)"/><g opacity=".5" filter="url(#V)"><path d="M71.662 81.487c-1.49.128.91-1.714.543-5.998-.247-2.89.76-5.335 2.249-5.462 1.489-.128 2.897 2.11 3.144 5 1.233 4.628-4.447 6.332-5.936 6.46Z" fill="#044FCB"/></g><path d="M61.382 41.456a5.986 5.986 0 0 1 11.24-4.12l17.922 48.912a5.986 5.986 0 1 1-11.24 4.118l-17.922-48.91Z" fill="url(#W)"/><path d="M59.33 35.432a7.034 7.034 0 0 0-4.882 4.415L37.603 86.106c-1.027 2.82 0 5.87 2.196 7.236l19.53-57.91Z" fill="url(#X)"/><path opacity=".3" d="M60.999 26.946c.853.854 2.392.699 3.437-.346 1.044-1.045 1.2-2.584.346-3.437-.854-.854-2.393-.699-3.437.346-1.045 1.045-1.2 2.584-.346 3.437Z" fill="url(#Y)" fill-opacity=".9"/><path opacity=".3" d="M53.014 53.113c2.552 1.474 6.486-.561 8.786-4.545s2.095-8.408-.457-9.882c-2.552-1.473-6.486.562-8.786 4.545-2.3 3.984-2.096 8.408.457 9.882Z" fill="url(#Z)" fill-opacity=".9"/><path d="M64.018 48.128a7.422 7.422 0 1 0 0-14.844 7.422 7.422 0 0 0 0 14.844Z" fill="#fff"/><path fill-rule="evenodd" clip-rule="evenodd" d="M64.018 35.237a5.469 5.469 0 1 0 0 10.938 5.469 5.469 0 0 0 0-10.938Zm-9.375 5.469a9.375 9.375 0 1 1 18.75 0 9.375 9.375 0 0 1-18.75 0Z" fill="#202124"/><defs><filter id="c" x="73.683" y="53.416" width="19.126" height="9.973" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".234" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="e" x="79.595" y="59.416" width="13.996" height="17.273" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".351" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="g" x="75.151" y="51.078" width="14.75" height="4.431" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".176" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="h" x="84.363" y="67.118" width="9.925" height="11.754" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".176" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="i" x="88.773" y="51.36" width="5.55" height="4.563" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".234" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="j" x="88.905" y="50.465" width="3.874" height="4.977" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".059" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="k" x="90.309" y="51.488" width="3.63" height="5.548" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".176" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="n" x="93.211" y="67.586" width="6.043" height="1.649" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".059" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="p" x="92.982" y="65.918" width=".983" height="4.606" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".117" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="q" x="93.41" y="65.18" width=".526" height="1.458" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".07" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="s" x="86.936" y="53.14" width="3.347" height="3.494" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".117" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="t" x="89.686" y="55.962" width="1.158" height="1.109" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".07" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="u" x="93.012" y="66.772" width="6.567" height="2.548" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".234" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="v" x="93.478" y="65.344" width="6.43" height="3.471" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".176" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="y" x="82.754" y="56.043" width="3.332" height="2.843" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".035" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="z" x="86.961" y="67.459" width="3.062" height="3.101" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".035" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="A" x="83.017" y="56.143" width="3.078" height="2.566" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/><feOffset dx="-.012" dy=".023"/><feGaussianBlur stdDeviation=".012"/><feComposite in2="hardAlpha" operator="out"/><feColorMatrix values="0 0 0 0 0.0156863 0 0 0 0 0.231373 0 0 0 0 0.0666667 0 0 0 0.7 0"/><feBlend in2="BackgroundImageFix" result="effect1_dropShadow_1081_1678"/><feBlend in="SourceGraphic" in2="effect1_dropShadow_1081_1678" result="shape"/></filter><filter id="B" x="87.242" y="67.513" width="2.752" height="2.91" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/><feOffset dx="-.012" dy=".023"/><feGaussianBlur stdDeviation=".012"/><feComposite in2="hardAlpha" operator="out"/><feColorMatrix values="0 0 0 0 0.0156863 0 0 0 0 0.231373 0 0 0 0 0.0666667 0 0 0 0.7 0"/><feBlend in2="BackgroundImageFix" result="effect1_dropShadow_1081_1678"/><feBlend in="SourceGraphic" in2="effect1_dropShadow_1081_1678" result="shape"/></filter><filter id="D" x="83.414" y="56.087" width="2.581" height="1.054" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".012" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="E" x="85.503" y="56.975" width=".555" height="1.327" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".003" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="I" x="88.343" y="68.266" width="1.62" height="2.185" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".012" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="J" x="84.591" y="56.471" width=".791" height=".553" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".012" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="K" x="89.119" y="68.801" width=".512" height=".758" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".012" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="L" x="83.82" y="57.987" width="1.795" height=".421" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".006" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="M" x="87.656" y="67.632" width="1.269" height="1.313" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".006" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="N" x="82.708" y="53.689" width="10.603" height="18.797" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".234" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="P" x="82.708" y="53.689" width="10.603" height="18.797" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".234" result="effect1_foregroundBlur_1081_1678"/></filter><filter id="V" x="70.583" y="69.436" width="7.775" height="12.643" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"/><feBlend in="SourceGraphic" in2="BackgroundImageFix" result="shape"/><feGaussianBlur stdDeviation=".293" result="effect1_foregroundBlur_1081_1678"/></filter><linearGradient id="a" x1="89.897" y1="100.561" x2="86.04" y2="98.374" gradientUnits="userSpaceOnUse"><stop stop-color="#4285F4"/><stop offset="1" stop-color="#034ECA"/></linearGradient><linearGradient id="d" x1="84.808" y1="54.191" x2="83.586" y2="58.523" gradientUnits="userSpaceOnUse"><stop stop-color="#A8F0B9"/><stop offset="1" stop-color="#ADEEBC" stop-opacity="0"/></linearGradient><linearGradient id="f" x1="90.857" y1="71.333" x2="87.186" y2="68.728" gradientUnits="userSpaceOnUse"><stop stop-color="#A8F0B9"/><stop offset="1" stop-color="#ADEEBC" stop-opacity="0"/></linearGradient><linearGradient id="F" x1="86.212" y1="56.951" x2="85.191" y2="57.364" gradientUnits="userSpaceOnUse"><stop stop-color="#E2DDE2"/><stop offset="1" stop-color="#E2DDE2" stop-opacity="0"/></linearGradient><linearGradient id="H" x1="89.776" y1="68.398" x2="88.921" y2="68.7" gradientUnits="userSpaceOnUse"><stop stop-color="#373637"/><stop offset="1" stop-color="#373637" stop-opacity="0"/></linearGradient><linearGradient id="O" x1="92.331" y1="61.164" x2="88.086" y2="62.662" gradientUnits="userSpaceOnUse"><stop stop-color="#A8F0B9"/><stop offset="1" stop-color="#ADEEBC" stop-opacity="0"/></linearGradient><linearGradient id="Q" x1="92.331" y1="61.164" x2="88.086" y2="62.662" gradientUnits="userSpaceOnUse"><stop stop-color="#A8F0B9"/><stop offset="1" stop-color="#ADEEBC" stop-opacity="0"/></linearGradient><linearGradient id="R" x1="60.209" y1="75.081" x2="78.764" y2="73.616" gradientUnits="userSpaceOnUse"><stop stop-color="#4285F4"/><stop offset=".703" stop-color="#044FCB"/></linearGradient><linearGradient id="S" x1="39.018" y1="99.585" x2="43.018" y2="97.223" gradientUnits="userSpaceOnUse"><stop stop-color="#4285F4"/><stop offset="1" stop-color="#034ECA"/></linearGradient><linearGradient id="T" x1="57.372" y1="65.999" x2="55.24" y2="65.26" gradientUnits="userSpaceOnUse"><stop stop-color="#73A7FF"/><stop offset="1" stop-color="#5893F6" stop-opacity="0"/></linearGradient><linearGradient id="U" x1="64.115" y1="26.802" x2="67.468" y2="29.818" gradientUnits="userSpaceOnUse"><stop stop-color="#4285F4"/><stop offset="1" stop-color="#034ECA"/></linearGradient><linearGradient id="W" x1="67.866" y1="46.531" x2="78.004" y2="67.72" gradientUnits="userSpaceOnUse"><stop stop-color="#034DC9"/><stop offset="1" stop-color="#4285F4"/></linearGradient><linearGradient id="X" x1="43.333" y1="63.99" x2="48.675" y2="65.823" gradientUnits="userSpaceOnUse"><stop stop-color="#9BC0FF"/><stop offset="1" stop-color="#5893F6" stop-opacity="0"/></linearGradient><radialGradient id="l" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-.53643 -.73571 .53314 -.38873 92.673 52.02)"><stop stop-color="#fff"/><stop offset=".948" stop-color="#fff" stop-opacity="0"/></radialGradient><radialGradient id="m" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="rotate(-126.097 66.088 8.52) scale(.91051 .65981)"><stop stop-color="#fff"/><stop offset=".948" stop-color="#fff" stop-opacity="0"/></radialGradient><radialGradient id="w" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-.32502 -.14335 .26108 -.59197 85.736 57.852)"><stop stop-color="#93E19F"/><stop offset="1" stop-color="#93E19F" stop-opacity="0"/></radialGradient><radialGradient id="x" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="rotate(117.327 23.966 61.105) scale(.35508 .64673)"><stop stop-color="#93E19F"/><stop offset="1" stop-color="#93E19F" stop-opacity="0"/></radialGradient><radialGradient id="Y" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-1.17874 1.19941 -.8356 -.8212 62.89 25.054)"><stop stop-color="#fff"/><stop offset=".948" stop-color="#fff" stop-opacity="0"/></radialGradient><radialGradient id="Z" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-2.58695 4.552 -2.48687 -1.41331 57.178 45.9)"><stop stop-color="#fff"/><stop offset=".948" stop-color="#fff" stop-opacity="0"/></radialGradient></defs></svg>',
    "aqua": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="59.9325" x2="1.33625" y1="59.6756" y2="1.07938" gradientUnits="userSpaceOnUse"><stop offset=".25" stop-color="#7256FF"/><stop offset=".73" stop-color="#007DFE"/></linearGradient><linearGradient id="b" x1="7.67063" x2="61.125" y1="64.3925" y2="39.6094" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#00D886"/><stop offset=".54" stop-color="#7256FF"/></linearGradient></defs><path fill="url(#a)" d="M0 4.125v34.1275c0 1.6581.993125 3.155 2.52063 3.8L39.9419 57.85c.5181.2187 1.0756.3294 1.6381.3244l18.3287-.15c2.265-.0188 4.0913-1.86 4.0913-4.125V36.2337c0-.8056-.2356-1.5931-.6781-2.2662L42.2131 1.85938C41.45.69875 40.155 0 38.7663 0H4.125C1.84687 0 0 1.84687 0 4.125Z"/><path fill="url(#b)" d="M6 49.015v10.8619c0 2.2781 1.84687 4.125 4.125 4.125h12.5656c.2 0 .4-.0144.5981-.0438L60.4738 58.51c2.0256-.2969 3.5268-2.0344 3.5268-4.0812V39.0312c0-2.2787-1.8475-4.1256-4.1262-4.1249l-18.5044.0043c-.4256 0-.8488.0663-1.2538.1957L8.87062 45.085c-1.70937.5463-2.86999 2.135-2.86999 3.9294L6 49.015Z"/><path fill="#00D886" d="M6 47.55v12.2588c0 2.3037 1.88688 4.1612 4.1906 4.1243L21 64c1.1812-.0188 2.5312-.7862 3.3-1.6831l32.7069-38.1581c.6406-.7475.9931-1.7001.9931-2.6844V10.125C58 7.84687 56.1531 6 53.875 6H42.8719c-1.1894 0-2.3213.51375-3.1044 1.40875L7.02063 44.8338C6.3625 45.5856 6 46.5506 6 47.55Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M20.7458 31.2425c-1.1681-.675-2.0869-1.6044-2.755-2.7869-.6681-1.1825-1.0025-2.5025-1.0025-3.9606s.3337-2.7781 1.0025-3.9606c.6681-1.1825 1.5862-2.1119 2.755-2.7869 1.1681-.675 2.4744-1.0131 3.9175-1.0131 1.4431 0 2.7387.3375 3.9069 1.0131 1.1681.675 2.085 1.6044 2.7493 2.7869.6644 1.1825.9969 2.5025.9969 3.9606s-.3325 2.7781-.9969 3.9606c-.6643 1.1825-1.5812 2.1119-2.7493 2.7869-1.1682.675-2.4707 1.0131-3.9069 1.0131-1.4363 0-2.7494-.3375-3.9175-1.0131Zm6.3081-2.2294c.7075-.4462 1.2613-1.065 1.6613-1.8543.4-.7894.6-1.6775.6-2.6638 0-.9862-.2-1.8738-.6-2.6638-.4-.7893-.9538-1.4074-1.6613-1.8543-.7075-.4463-1.5044-.67-2.39-.67-.8856 0-1.6844.2231-2.3956.67-.7113.4469-1.2688 1.065-1.6719 1.8543-.4037.7894-.6056 1.6776-.6056 2.6638 0 .9863.2019 1.8744.6056 2.6638.4038.7893.9613 1.4081 1.6719 1.8543.7112.4469 1.5094.67 2.3956.67.8863 0 1.6831-.2231 2.39-.67Zm-2.16 6.0344c-.4894-.2538-.865-.6131-1.1256-1.0775-.2613-.4644-.3913-1.0113-.3913-1.64l-.0106-1.94h2.7438v1.8113c0 .2212.0431.4124.1287.5731.0856.1606.2088.2825.37.3644.1606.0818.3519.1231.5738.1231h1.8331v2.165h-2.4119c-.6506 0-1.22-.1269-1.7094-.3806l-.0006.0012Z"/><path fill="#fff" d="M38.2334 16.9922h3.1725l5.5632 15.0062h-2.9475l-1.2113-3.4837h-5.8419l-1.1362 3.4837h-3.0119l5.4131-15.0062Zm3.805 9.2612-2.0256-5.7237-.225-.9538-.2144.9538-1.9081 5.7237h4.3731Z"/></svg>',
    "clion": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="4.0675" x2="62.6637" y1="4.32704" y2="62.9233" gradientUnits="userSpaceOnUse"><stop offset=".29" stop-color="#009AE5"/><stop offset=".7" stop-color="#00D980"/></linearGradient><linearGradient id="b" x1="56.3294" x2="2.87437" y1="-.390627" y2="24.3931" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#FF2D90"/><stop offset=".54" stop-color="#009AE5"/></linearGradient></defs><path fill="url(#a)" d="M64 59.8777V25.7502c0-1.6582-.9931-3.155-2.5206-3.8L24.0581 6.15266c-.5181-.21875-1.0756-.32937-1.6381-.32437l-18.32875.15C1.82625 5.99641 0 7.83766 0 10.1027v17.6656c0 .8056.235625 1.5931.678125 2.2662L21.7869 62.1439c.7625 1.1606 2.0581 1.8588 3.4468 1.8588H59.875c2.2781 0 4.125-1.8469 4.125-4.125Z"/><path fill="url(#b)" d="M58 14.9875V4.125C58 1.84687 56.1531 0 53.875 0H41.3094c-.2 0-.4.014375-.5981.04375L3.52688 5.49188C1.50125 5.78875 0 7.52625 0 9.57312V24.9706c0 2.2788 1.8475 4.1256 4.12625 4.125l18.50435-.0044c.4256 0 .8488-.0662 1.2538-.1956L55.13 18.9169c1.7094-.5463 2.87-2.135 2.87-3.9294Z"/><path fill="#FF2D90" d="M58 16.4528V4.19406C58 1.89031 56.1131.032813 53.8094.069687L43.0044.007813C41.8231.026562 40.4688.789061 39.7 1.68594L6.99312 39.8441C6.3525 40.5916 6 41.5441 6 42.5284v11.3494c0 2.2781 1.84687 4.125 4.125 4.125h11.0031c1.1894 0 2.3213-.5137 3.1044-1.4087l32.7469-37.425C57.6375 18.4172 58 17.4522 58 16.4528Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M20.7465 31.2425c-1.165-.675-2.0794-1.6044-2.7438-2.7869-.6643-1.1825-.9968-2.5025-.9968-3.9606s.3325-2.7781.9968-3.9606c.6644-1.1825 1.5794-2.1119 2.7438-2.7869 1.1644-.675 2.4656-1.0131 3.9019-1.0131 1.215 0 2.3293.225 3.3443.675 1.0144.45 1.86 1.0806 2.535 1.8919.675.8112 1.1269 1.7418 1.3557 2.7925h-3.0657c-.2-.5432-.4981-1.02-.895-1.4313-.3968-.4106-.8737-.7269-1.4312-.9487-.5575-.2213-1.165-.3325-1.8219-.3325-.8862 0-1.6862.2212-2.4012.6643-.7144.4432-1.2738 1.0525-1.6775 1.8275-.4038.7757-.6057 1.6488-.6057 2.6206 0 .9719.2019 1.8457.6057 2.6207.4037.7756.9631 1.3844 1.6775 1.8275.7143.4431 1.515.6644 2.4012.6644.6575 0 1.265-.1107 1.8219-.3325.5575-.2213 1.0344-.5375 1.4312-.9488.3969-.4106.695-.8881.895-1.4313h3.0657c-.2288 1.0507-.6807 1.9813-1.3557 2.7926-.675.8112-1.5206 1.4418-2.535 1.8918-1.015.45-2.1293.675-3.3443.675-1.4363 0-2.7369-.3375-3.9019-1.0131v.0025Z"/><path fill="#fff" d="M37.3291 16.9922v12.3694h7.1175v2.6368H34.4141V16.9922h2.9156-.0006Z"/></svg>',
    "datagrip": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="59.6762" x2="1.08" y1="4.06688" y2="62.6631" gradientUnits="userSpaceOnUse"><stop offset=".28" stop-color="#7256FF"/><stop offset=".66" stop-color="#00D980"/></linearGradient><linearGradient id="b" x1="64.3912" x2="39.6074" y1="56.3294" y2="2.87437" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#FF43F2"/><stop offset=".54" stop-color="#7256FF"/></linearGradient></defs><path fill="url(#a)" d="M4.125 64h34.1275c1.6581 0 3.155-.9931 3.8-2.5206L57.85 24.0581c.2187-.5181.3294-1.0756.3244-1.6381l-.15-18.32875C58.0056 1.82625 56.1644 0 53.8994 0H36.2337c-.8056 0-1.5931.235625-2.2662.678125L1.85938 21.7869C.69875 22.55 0 23.845 0 25.2337V59.875C0 62.1531 1.84687 64 4.125 64Z"/><path fill="url(#b)" d="M49.0131 58h10.8618c2.2781 0 4.125-1.8469 4.125-4.125V41.3094c0-.2-.0144-.4-.0437-.5981L58.508 3.52688C58.2112 1.50125 56.4737 0 54.4268 0H39.0293c-2.2788 0-4.1256 1.8475-4.125 4.12625l.0044 18.50435c0 .4256.0662.8488.1956 1.2538L45.083 55.13c.5463 1.7094 2.135 2.87 3.9294 2.87h.0007Z"/><path fill="#FF43F2" d="M47.55 58h12.2588c2.3037 0 4.1612-1.8869 4.1243-4.1906L63.9994 43c-.0188-1.1812-.7856-2.5312-1.6825-3.3L24.1588 6.99312C23.4113 6.3525 22.4587 6 21.4744 6H10.125C7.84687 6 6 7.84687 6 10.125v11.0031c0 1.1894.51375 2.3213 1.40875 3.1044L44.8338 56.9794C45.5856 57.6375 46.5506 58 47.55 58Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M17.0117 16.9922h5.7131c1.4219 0 2.6957.3212 3.8213.9644 1.1256.6431 2.0062 1.5343 2.6419 2.6743.6362 1.14.9537 2.4275.9537 3.8644 0 1.4369-.3181 2.7244-.9537 3.8644-.6363 1.14-1.5169 2.0312-2.6419 2.6744-1.1256.6431-2.3994.9643-3.8213.9643h-5.7131V16.9922Zm8.0281 11.8762c.6719-.4 1.19-.9737 1.5544-1.7206.3644-.7469.5469-1.6306.5469-2.6531 0-1.0225-.1825-1.9063-.5469-2.6531-.3644-.7469-.8825-1.32-1.5544-1.7207-.6718-.4-1.4543-.6-2.3475-.6h-2.755v9.9469h2.755c.8932 0 1.6757-.2 2.3475-.6v.0006Z"/><path fill="#fff" d="M35.4262 31.2425c-1.165-.675-2.0794-1.6044-2.7438-2.7869-.6644-1.1825-.9969-2.5025-.9969-3.9606s.3325-2.7781.9969-3.9606 1.5794-2.1119 2.7438-2.7869c1.1643-.675 2.4656-1.0131 3.9018-1.0131 1.1644 0 2.2382.2075 3.2213.6219.9825.4143 1.8112.9968 2.4869 1.7468.6756.75 1.1487 1.615 1.42 2.5938h-3.13c-.2288-.4719-.5375-.8806-.9269-1.2275-.3894-.3463-.845-.6144-1.3669-.8038s-1.0825-.2837-1.6831-.2837c-.8863 0-1.6863.2212-2.4013.6643-.7143.4432-1.2737 1.0526-1.6775 1.8276-.4037.7756-.6056 1.6487-.6056 2.6206s.2019 1.8456.6056 2.6206c.4038.7756.9632 1.3844 1.6775 1.8275.7144.4431 1.515.6644 2.4013.6644.8219 0 1.5669-.1538 2.235-.4613.6681-.3069 1.1987-.7325 1.5919-1.2756.3931-.5431.6037-1.1538.6325-1.8331l.0106.3106H40.293v-2.3044h6.3563v1.1794c0 1.3219-.32 2.5175-.9594 3.5856-.6394 1.0681-1.515 1.91-2.6262 2.5244-1.1113.6144-2.3563.9219-3.7357.9219-1.3793 0-2.7368-.3375-3.9018-1.0131v.0012Z"/></svg>',
    "dataspell": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="4.0675" x2="62.6637" y1="4.32704" y2="62.9233" gradientUnits="userSpaceOnUse"><stop offset=".28" stop-color="#007DFE"/><stop offset=".73" stop-color="#00D980"/></linearGradient><linearGradient id="b" x1="56.3294" x2="2.875" y1="-.390625" y2="24.3925" gradientUnits="userSpaceOnUse"><stop offset=".32" stop-color="#F0EB18"/><stop offset=".55" stop-color="#007DFE"/></linearGradient></defs><path fill="url(#a)" d="M64 59.8777V25.7502c0-1.6582-.9931-3.155-2.5206-3.8L24.0581 6.15266c-.5181-.21875-1.0756-.32937-1.6381-.32437l-18.32875.15C1.82625 5.99641 0 7.83766 0 10.1027v17.6656c0 .8056.235625 1.5931.678125 2.2662L21.7869 62.1439c.7625 1.1606 2.0581 1.8588 3.4468 1.8588H59.875c2.2781 0 4.125-1.8469 4.125-4.125Z"/><path fill="url(#b)" d="M58 14.9875V4.125C58 1.84687 56.1531 0 53.875 0H41.3094c-.2 0-.4.014375-.5981.04375L3.52688 5.49188C1.50125 5.78875 0 7.52625 0 9.57312V24.9706c0 2.2788 1.8475 4.1256 4.12625 4.125l18.50435-.0044c.4256 0 .8488-.0662 1.2538-.1956L55.13 18.9169c1.7094-.5463 2.87-2.135 2.87-3.9294Z"/><path fill="#F0EB18" d="M58 16.45V4.19125C58 1.8875 56.1131.03 53.8094.066875L43 0c-1.1812.01875-2.5312.785625-3.3 1.6825L6.99312 39.8413C6.3525 40.5888 6 41.5412 6 42.5256V53.875C6 56.1531 7.84687 58 10.125 58h11.0031c1.1894 0 2.3213-.5137 3.1044-1.4087l32.7469-37.425C57.6375 18.4144 58 17.4494 58 16.45Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M17.0117 16.9922h5.7131c1.4219 0 2.6957.3212 3.8213.9644 1.1256.6431 2.0062 1.5343 2.6419 2.6743.6356 1.14.9537 2.4275.9537 3.8644 0 1.4369-.3181 2.7244-.9537 3.8644-.6363 1.14-1.5169 2.0312-2.6419 2.6744-1.125.6431-2.3994.9643-3.8213.9643h-5.7131V16.9922Zm8.0281 11.8762c.6719-.4 1.19-.9737 1.5544-1.7206.3644-.7469.5469-1.6306.5469-2.6531 0-1.0225-.1825-1.9063-.5469-2.6531-.3644-.7469-.8825-1.32-1.5544-1.7207-.6718-.4-1.4543-.6-2.3475-.6h-2.755v9.9469h2.755c.8932 0 1.6757-.2 2.3475-.6v.0006Z"/><path fill="#fff" d="M34.7127 31.6644c-.84-.3931-1.4968-.9431-1.9725-1.6506-.475-.7075-.72-1.5219-.7343-2.4438h2.9368c0 .4356.1144.8181.3432 1.1469.2287.3287.5468.5862.9537.7719.4075.1856.875.2787 1.4044.2787.5294 0 .9519-.0837 1.3344-.2519.3818-.1681.6787-.4019.8893-.7019.2107-.3.3163-.6431.3163-1.0287 0-.4788-.145-.875-.4344-1.19-.2894-.3144-.6881-.5325-1.195-.6538l-2.6475-.5893c-.7144-.1569-1.3362-.4269-1.865-.8094-.5287-.3825-.94-.8556-1.2325-1.42-.2931-.5644-.4394-1.2006-.4394-1.9081 0-.8575.2213-1.6275.6644-2.31.4431-.6825 1.0613-1.215 1.8544-1.5969.7931-.3825 1.6937-.5731 2.7012-.5731s1.9332.1856 2.7332.5575 1.4237.8881 1.8706 1.5487c.4462.6613.6737 1.42.6806 2.2775h-2.9262c0-.3643-.0963-.6912-.2894-.9806s-.4663-.5144-.82-.675c-.3538-.1606-.7594-.2412-1.2169-.2412-.4575 0-.8594.0768-1.2056.2306-.3469.1537-.6163.3681-.8094.6431-.1931.275-.2894.595-.2894.9594 0 .4143.1338.7575.4019 1.0287.2681.2719.6344.4644 1.0988.5788l2.5512.5575c.7356.15 1.3919.4344 1.9669.8519.575.4181 1.0237.9324 1.345 1.5437.3212.6112.4825 1.2775.4825 1.9988 0 .8862-.2344 1.6812-.7019 2.385-.4681.7037-1.1237 1.2556-1.9669 1.6562-.8431.4-1.8081.6-2.8943.6-1.0863 0-2.0494-.1969-2.8888-.5894l.0006-.0012Z"/></svg>',
    "goland": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="64.3912" x2="39.6074" y1="56.3294" y2="2.87437" gradientUnits="userSpaceOnUse"><stop offset=".24" stop-color="#00D886"/><stop offset=".51" stop-color="#007DFE"/></linearGradient><linearGradient id="b" x1="59.6762" x2="1.08" y1="4.06688" y2="62.6631" gradientUnits="userSpaceOnUse"><stop offset=".27" stop-color="#007DFE"/><stop offset=".7" stop-color="#D249FC"/></linearGradient></defs><path fill="#00D886" d="M47.55 58h12.2588c2.3037 0 4.1612-1.8869 4.1243-4.1906l-.1762-11.0431c-.0188-1.1813-.5431-2.2975-1.44-3.0663L24.1588 6.99312C23.4113 6.3525 22.4587 6 21.4744 6H10.125C7.84687 6 6 7.84687 6 10.125v11.0031c0 1.1894.51375 2.3213 1.40875 3.1044L44.8338 56.9794C45.5856 57.6375 46.5506 58 47.55 58Z"/><path fill="url(#a)" d="M49.0131 58h10.8618c2.2781 0 4.125-1.8469 4.125-4.125V41.3094c0-.2-.0144-.4-.0437-.5981L58.508 3.52688C58.2118 1.50125 56.4743 0 54.4268 0H39.0293c-2.2788 0-4.1256 1.8475-4.125 4.12625l.0044 18.50435c0 .4256.0662.8488.1956 1.2538L45.083 55.13c.5463 1.7094 2.135 2.87 3.9294 2.87h.0007Z"/><path fill="url(#b)" d="M4.125 64h34.1275c1.6581 0 3.155-.9931 3.8-2.5206L57.85 24.0581c.2187-.5181.3294-1.0756.3244-1.6381l-.15-18.32875C58.0063 1.82625 56.165 0 53.9 0H36.2344c-.8057 0-1.5932.235625-2.2663.678125L1.85938 21.7869C.69875 22.55 0 23.845 0 25.2337V59.875C0 62.1531 1.84687 64 4.125 64Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M19.7484 31.2425c-1.165-.675-2.0793-1.6044-2.7437-2.7869-.6644-1.1825-.9969-2.5025-.9969-3.9606s.3325-2.7781.9969-3.9606 1.5794-2.1119 2.7437-2.7869c1.1644-.675 2.465-1.0131 3.9019-1.0131 1.1644 0 2.2381.2075 3.2213.6219.9825.4143 1.8112.9968 2.4868 1.7468.675.75 1.1488 1.615 1.42 2.5938h-3.13c-.2287-.4719-.5375-.8806-.9268-1.2275-.3894-.3463-.845-.6144-1.3669-.8038s-1.0825-.2837-1.6831-.2837c-.8863 0-1.6863.2212-2.4013.6643-.7144.4432-1.2737 1.0526-1.6775 1.8276-.4037.7756-.6056 1.6487-.6056 2.6206s.2019 1.8456.6056 2.6206c.4038.7756.9631 1.3844 1.6775 1.8275.7144.4431 1.515.6644 2.4013.6644.8218 0 1.5668-.1538 2.235-.4613.6681-.3069 1.1987-.7325 1.5918-1.2756.3932-.5431.6038-1.1538.6325-1.8331l.0107.3106h-3.5263v-2.3044h6.3563v1.1794c0 1.3219-.32 2.5175-.9594 3.5856-.6394 1.0681-1.515 1.91-2.6263 2.5244-1.1112.6144-2.3562.9219-3.7356.9219s-2.7369-.3375-3.9019-1.0131v.0012Z"/><path fill="#fff" d="M36.2712 31.2425c-1.1681-.675-2.0869-1.6044-2.755-2.7869-.6682-1.1825-1.0025-2.5025-1.0025-3.9606s.3337-2.7781 1.0025-3.9606c.6681-1.1825 1.5862-2.1119 2.755-2.7869 1.1681-.675 2.4743-1.0131 3.9175-1.0131 1.4431 0 2.7387.3375 3.9069 1.0131 1.1681.675 2.0849 1.6044 2.7493 2.7869.6644 1.1825.9969 2.5025.9969 3.9606s-.3325 2.7781-.9969 3.9606-1.5812 2.1119-2.7493 2.7869c-1.1682.675-2.4707 1.0131-3.9069 1.0131-1.4363 0-2.7494-.3375-3.9175-1.0131Zm6.3081-2.2294c.7075-.4462 1.2612-1.065 1.6612-1.8543.4-.7894.6-1.6775.6-2.6638 0-.9862-.2-1.8738-.6-2.6638-.4-.7893-.9537-1.4074-1.6612-1.8543-.7075-.4463-1.5044-.67-2.39-.67-.8856 0-1.685.2231-2.3956.67-.7113.4469-1.2688 1.065-1.6719 1.8543-.4038.7894-.6056 1.6776-.6056 2.6638 0 .9863.2018 1.8744.6056 2.6638.4037.7893.9612 1.4081 1.6719 1.8543.7112.4469 1.5094.67 2.3956.67.8863 0 1.6825-.2231 2.39-.67Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/></svg>',
    "idea": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="-.390625" x2="24.3925" y1="7.67063" y2="61.1256" gradientUnits="userSpaceOnUse"><stop offset=".1" stop-color="#FC801D"/><stop offset=".59" stop-color="#FE2857"/></linearGradient><linearGradient id="b" x1="4.32509" x2="62.9207" y1="59.9325" y2="1.33625" gradientUnits="userSpaceOnUse"><stop offset=".21" stop-color="#FE2857"/><stop offset=".7" stop-color="#007EFF"/></linearGradient></defs><path fill="#FF8100" d="M16.4501 6H4.19132C1.88757 6 .03007 7.88688.066946 10.1906l.17625 11.0431C.261946 22.415.786321 23.5312 1.6832 24.3l38.1587 32.7069c.7475.6406 1.7.9931 2.6844.9931h11.3494c2.2781 0 4.125-1.8469 4.125-4.125V42.8719c0-1.1894-.5138-2.3213-1.4088-3.1044L19.1663 7.02063C18.4144 6.3625 17.4494 6 16.4501 6Z"/><path fill="url(#a)" d="M14.9875 6H4.125C1.84687 6 0 7.84687 0 10.125v12.5656c0 .2.014375.4.04375.5981l5.44813 37.1851c.29687 2.0256 2.03437 3.5268 4.08124 3.5268H24.9706c2.2788 0 4.1256-1.8475 4.125-4.1262L29.0912 41.37c0-.4256-.0662-.8488-.1956-1.2538L18.9169 8.87062c-.5463-1.70937-2.135-2.86999-3.9294-2.86999V6Z"/><path fill="url(#b)" d="M59.8757 0H25.7482c-1.6581 0-3.155.993125-3.8 2.52063L6.15071 39.9419c-.21875.5181-.32938 1.0756-.32438 1.6381l.15 18.3287C5.99508 62.1737 7.83633 64 10.1013 64H27.767c.8056 0 1.5931-.2356 2.2662-.6781l32.1094-21.1088c1.1606-.7625 1.8587-2.0581 1.8587-3.4468V4.125c0-2.27813-1.8468-4.125-4.125-4.125h-.0006Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M17 29.3834h2.98v-9.7756H17v-2.6156h8.8431v2.6156h-2.98v9.7756h2.98v2.6157H17v-2.6157Z"/><path fill="#fff" d="M27.6426 29.2978h2.1544c.4356 0 .8237-.0925 1.1631-.2787.3394-.1857.6019-.4482.7881-.7882.1856-.3393.2788-.7268.2788-1.1631V16.9922h2.9262v10.2794c0 .9006-.2075 1.7093-.6219 2.4275-.4143.7181-.9862 1.2806-1.715 1.6881-.7287.4075-1.5468.6112-2.4543.6112h-2.5188v-2.7012l-.0006.0006Z"/></svg>',
    "phpstorm": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="56.3294" x2="2.87438" y1="-.391251" y2="24.3925" gradientUnits="userSpaceOnUse"><stop offset=".16" stop-color="#D249FC"/><stop offset=".55" stop-color="#FF2D90"/></linearGradient><linearGradient id="b" x1="4.0675" x2="62.6638" y1="4.32641" y2="62.9227" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#FF2D90"/><stop offset=".7" stop-color="#7256FF"/></linearGradient></defs><path fill="#D249FC" d="M58 16.4462V4.18741C58 1.88366 56.1131.026165 53.8094.06304L42.7663.23929c-1.1813.01875-2.2975.543125-3.0663 1.44L6.99312 39.8374C6.3525 40.5849 6 41.5374 6 42.5218v11.3494c0 2.2781 1.84687 4.125 4.125 4.125h11.0031c1.1894 0 2.3213-.5138 3.1044-1.4088l32.7469-37.425C57.6375 18.4105 58 17.4455 58 16.4462Z"/><path fill="url(#a)" d="M58 14.9875V4.125C58 1.84687 56.1531 0 53.875 0H41.3094c-.2 0-.4.014375-.5981.04375L3.52688 5.49188C1.50125 5.78875 0 7.52625 0 9.57312V24.9706c0 2.2788 1.8475 4.1256 4.12625 4.125l18.50435-.0044c.4256 0 .8488-.0662 1.2538-.1956L55.13 18.9169c1.7094-.5463 2.87-2.135 2.87-3.9294Z"/><path fill="url(#b)" d="M64 59.8777V25.7502c0-1.6582-.9931-3.155-2.5206-3.8L24.0581 6.15266c-.5181-.21875-1.0756-.32937-1.6381-.32437l-18.32875.15C1.82625 5.99641 0 7.83766 0 10.1027v17.6656c0 .8056.235625 1.5931.678125 2.2662L21.7869 62.1439c.7625 1.1606 2.0581 1.8588 3.4468 1.8588H59.875c2.2781 0 4.125-1.8469 4.125-4.125Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M16.9928 16.9922h6.4419c1.0575 0 1.9844.1931 2.7812.5787.7969.3857 1.4113.9288 1.8438 1.6294.4325.7006.6487 1.5113.6487 2.4331 0 .9219-.22 1.7582-.6593 2.4657-.4394.7075-1.0632 1.2556-1.8707 1.6456-.8075.3894-1.7506.5844-2.83.5844h-3.43v5.67h-2.9262V16.9928l.0006-.0006Zm7.5406 6.63c.3682-.1825.6519-.4431.8519-.7825.2-.3394.3-.7375.3-1.195s-.1-.8413-.3-1.1738c-.2-.3325-.4844-.5893-.8519-.7718-.3681-.1825-.7987-.2732-1.2918-.2732h-3.3225v4.47h3.3225c.4931 0 .9237-.0912 1.2918-.2731v-.0006Z"/><path fill="#fff" d="M32.5721 31.6644c-.84-.3931-1.4969-.9431-1.9725-1.6506-.475-.7075-.72-1.5219-.7344-2.4438h2.9369c0 .4356.1144.8181.3431 1.1469.2288.3287.5469.5862.9538.7719.4075.1856.875.2787 1.4044.2787.5293 0 .9518-.0837 1.3343-.2519.3825-.1681.6788-.4019.8894-.7019s.3163-.6431.3163-1.0287c0-.4788-.145-.875-.4344-1.19-.2894-.3144-.6881-.5325-1.195-.6538l-2.6475-.5893c-.7144-.1569-1.3363-.4269-1.865-.8094-.5288-.3825-.94-.8556-1.2325-1.42-.2931-.5644-.4394-1.2006-.4394-1.9081 0-.8575.2213-1.6275.6644-2.31.4431-.6825 1.0612-1.215 1.8544-1.5969.7931-.3825 1.6937-.5731 2.7012-.5731s1.9331.1856 2.7331.5575c.8.3719 1.4238.8881 1.8707 1.5487.4462.6613.6731 1.42.6806 2.2775h-2.9263c0-.3643-.0962-.6912-.2893-.9806-.1932-.2894-.4663-.5144-.82-.675-.3538-.1606-.7594-.2412-1.2169-.2412-.4575 0-.8594.0768-1.2056.2306-.3469.1537-.6163.3681-.8094.6431-.1931.275-.2894.595-.2894.9594 0 .4143.1338.7575.4019 1.0287.2681.2719.6344.4644 1.0987.5788l2.5513.5575c.7356.15 1.3919.4344 1.9669.8519.575.4181 1.0237.9324 1.345 1.5437.3212.6112.4825 1.2775.4825 1.9988 0 .8862-.2344 1.6812-.7019 2.385-.4681.7037-1.1238 1.2556-1.9669 1.6562-.8431.4-1.8081.6-2.8944.6-1.0862 0-2.0493-.1969-2.8887-.5894l.0006-.0012Z"/></svg>',
    "pycharm": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="7.67063" x2="61.1256" y1="64.3931" y2="39.6094" gradientUnits="userSpaceOnUse"><stop offset=".1" stop-color="#00D886"/><stop offset=".59" stop-color="#F0EB18"/></linearGradient><linearGradient id="b" x1="59.9331" x2="1.33687" y1="59.6762" y2="1.08" gradientUnits="userSpaceOnUse"><stop offset=".3" stop-color="#F0EB18"/><stop offset=".7" stop-color="#00C4F4"/></linearGradient></defs><path fill="#00D886" d="M6 47.55v12.2588c0 2.3037 1.88688 4.1612 4.1906 4.1243l11.0431-.1762c1.1813-.0188 2.2975-.5431 3.0663-1.44l32.7069-38.1581c.6406-.7475.9931-1.7001.9931-2.6844V10.125C58 7.84687 56.1531 6 53.875 6H42.8719c-1.1894 0-2.3213.51375-3.1044 1.40875L7.02063 44.8338C6.3625 45.5856 6 46.5506 6 47.55Z"/><path fill="url(#a)" d="M6 49.015v10.8619c0 2.2781 1.84687 4.125 4.125 4.125h12.5656c.2 0 .4-.0144.5981-.0438L60.4738 58.51c2.0256-.2969 3.5268-2.0344 3.5268-4.0812V39.0312c0-2.2787-1.8475-4.1256-4.1262-4.1249l-18.5044.0043c-.4256 0-.8488.0663-1.2538.1957L8.87062 45.085c-1.70937.5463-2.86999 2.135-2.86999 3.9294L6 49.015Z"/><path fill="url(#b)" d="M0 4.125v34.1275c0 1.6581.993125 3.155 2.52063 3.8L39.9419 57.85c.5181.2187 1.0756.3294 1.6381.3244l18.3287-.15c2.265-.0188 4.0913-1.86 4.0913-4.125V36.2337c0-.8056-.2356-1.5931-.6781-2.2662L42.2131 1.85938C41.45.69875 40.155 0 38.7663 0H4.125C1.84687 0 0 1.84687 0 4.125Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M16.9928 16.9922h6.4419c1.0575 0 1.9844.1931 2.7812.5787.7969.3857 1.4113.9288 1.8438 1.6294.4325.7006.6487 1.5113.6487 2.4331 0 .9219-.22 1.7582-.6593 2.4657-.4394.7075-1.0632 1.2556-1.8707 1.6456-.8075.3894-1.7506.5844-2.83.5844h-3.43v5.67h-2.9262V16.9928l.0006-.0006Zm7.5406 6.63c.3682-.1825.6519-.4431.8519-.7825.2-.3394.3-.7375.3-1.195s-.1-.8413-.3-1.1738c-.2-.3325-.4844-.5893-.8519-.7718-.3681-.1825-.7987-.2732-1.2918-.2732h-3.3232v4.47h3.3232c.4931 0 .9237-.0912 1.2918-.2731v-.0006Z"/><path fill="#fff" d="M33.7133 31.2425c-1.165-.675-2.0794-1.6044-2.7438-2.7869-.6643-1.1825-.9968-2.5025-.9968-3.9606s.3325-2.7781.9968-3.9606c.6644-1.1825 1.5794-2.1119 2.7438-2.7869 1.1644-.675 2.4656-1.0131 3.9019-1.0131 1.215 0 2.3293.225 3.3443.675 1.0144.45 1.86 1.0806 2.535 1.8919.675.8112 1.1269 1.7418 1.3557 2.7925h-3.0657c-.2-.5432-.4981-1.02-.895-1.4313-.3968-.4106-.8737-.7269-1.4312-.9487-.5575-.2213-1.165-.3325-1.8225-.3325-.8863 0-1.6863.2212-2.4013.6643-.7143.4432-1.2737 1.0525-1.6775 1.8275-.4037.7757-.6056 1.6488-.6056 2.6206 0 .9719.2019 1.8457.6056 2.6207.4038.7756.9632 1.3844 1.6775 1.8275.7144.4431 1.515.6644 2.4013.6644.6575 0 1.265-.1107 1.8225-.3325.5575-.2213 1.0344-.5375 1.4312-.9488.3969-.4106.695-.8881.895-1.4313h3.0657c-.2288 1.0507-.6807 1.9813-1.3557 2.7926-.675.8112-1.5206 1.4418-2.535 1.8918-1.015.45-2.1293.675-3.3443.675-1.4363 0-2.7369-.3375-3.9019-1.0131v.0025Z"/></svg>',
    "rider": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="64.3905" x2="39.6074" y1="56.3294" y2="2.87438" gradientUnits="userSpaceOnUse"><stop offset=".21" stop-color="#007DFE"/><stop offset=".55" stop-color="#FFB700"/></linearGradient><linearGradient id="b" x1="59.6756" x2="1.08" y1="4.06688" y2="62.6631" gradientUnits="userSpaceOnUse"><stop offset=".23" stop-color="#FFB700"/><stop offset=".73" stop-color="#FF0A67"/></linearGradient></defs><path fill="#007DFE" d="M47.5494 58h12.2587c2.3038 0 4.1613-1.8869 4.1244-4.1906l-.1763-11.0431c-.0187-1.1813-.5431-2.2975-1.44-3.0663L24.1581 6.99312C23.4106 6.3525 22.4581 6 21.4737 6H10.125C7.84687 6 6 7.84687 6 10.125v11.0031c0 1.1894.51375 2.3213 1.40875 3.1044L44.8337 56.9794C45.5856 57.6375 46.5506 58 47.55 58h-.0006Z"/><path fill="url(#a)" d="M49.0131 58h10.8618c2.2781 0 4.125-1.8469 4.125-4.125V41.3094c0-.2-.0144-.4-.0437-.5981L58.508 3.52688C58.2112 1.50125 56.4737 0 54.4268 0H39.0293c-2.2788 0-4.1256 1.8475-4.125 4.12625l.0044 18.50435c0 .4256.0662.8488.1956 1.2538L45.083 55.13c.5463 1.7094 2.135 2.87 3.9294 2.87h.0007Z"/><path fill="url(#b)" d="M4.125 64h34.1275c1.6581 0 3.155-.9931 3.8-2.5206L57.85 24.0581c.2187-.5181.3294-1.0756.3244-1.6381l-.15-18.32875C58.0063 1.82625 56.165 0 53.9 0H36.2344c-.8057 0-1.5932.235625-2.2663.678125L1.85938 21.7869C.69875 22.55 0 23.845 0 25.2337V59.875C0 62.1531 1.84687 64 4.125 64Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M16.9922 16.9922h6.4419c1.0506 0 1.9756.1931 2.7762.5787.8.3857 1.4169.9288 1.8488 1.6294.4325.7006.6487 1.5113.6487 2.4331 0 .9219-.22 1.7488-.6594 2.46-.4393.7113-1.065 1.2613-1.8756 1.6507-.8112.3893-1.7525.5843-2.8244.5843h-3.43v5.67h-2.9262V16.9922Zm7.5406 6.6294c.3681-.1825.6519-.4432.8519-.7825.2-.3394.3-.7344.3-1.1844 0-.45-.1-.8519-.3-1.1844-.2-.3325-.4844-.5894-.8519-.7719-.3681-.1825-.7987-.2731-1.2919-.2731h-3.3231v4.47h3.3231c.4932 0 .9238-.0912 1.2919-.2731v-.0006Zm-2.6312 1.7637h3.1943l3.9338 6.6138h-3.355l-3.7731-6.6138Z"/><path fill="#fff" d="M31.6133 16.9922h5.7131c1.4219 0 2.6956.3212 3.8213.9644 1.1256.6431 2.0062 1.5343 2.6418 2.6743.6357 1.14.9538 2.4275.9538 3.8644 0 1.4369-.3181 2.7244-.9538 3.8644-.6362 1.14-1.5168 2.0312-2.6418 2.6744-1.125.6431-2.3994.9643-3.8213.9643h-5.7131V16.9922Zm8.0281 11.8762c.6719-.4 1.19-.9737 1.5544-1.7206.3644-.7469.5469-1.6306.5469-2.6531 0-1.0225-.1825-1.9063-.5469-2.6531-.3644-.7469-.8825-1.32-1.5544-1.7207-.6719-.4-1.4544-.6-2.3475-.6h-2.755v9.9469h2.755c.8931 0 1.6756-.2 2.3475-.6v.0006Z"/></svg>',
    "rubymine": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="4.32511" x2="62.9208" y1="59.9325" y2="1.33743" gradientUnits="userSpaceOnUse"><stop offset=".29" stop-color="#FF2358"/><stop offset=".75" stop-color="#7256FF"/></linearGradient><linearGradient id="b" x1="-.390618" x2="24.393" y1="7.67061" y2="61.1249" gradientUnits="userSpaceOnUse"><stop offset=".29" stop-color="#FF8100"/><stop offset=".56" stop-color="#FF2358"/></linearGradient></defs><path fill="url(#a)" d="M59.8753 0H25.7484c-1.658 0-3.1549.993115-3.7999 2.5206L6.1507 39.9415c-.21874.5181-.32937 1.0756-.32437 1.6381l.15 18.3286c.01875 2.2649 1.85996 4.0912 4.12497 4.0912h17.6652c.8056 0 1.5931-.2357 2.2662-.6782l32.1088-21.1085c1.1606-.7625 1.8587-2.0581 1.8587-3.4468V4.12496C64.0002 1.84686 62.1534 0 59.8753 0Z"/><path fill="url(#b)" d="M14.9872 6H4.12554C1.84684 6 0 7.84686 0 10.125v12.5655c0 .2.014375.4.04375.5981l5.44802 37.1846C5.78864 62.4988 7.5261 64 9.57294 64H24.9701c2.2787 0 4.1256-1.8474 4.125-4.1262l-.0044-18.5042c0-.4256-.0663-.8487-.1956-1.2537L18.9165 8.8706c-.5462-1.70936-2.135-2.86997-3.9293-2.86997V6Z"/><path fill="#FF8100" d="M16.4497 6H4.19117C1.88746 6 .03 7.88686.066874 10.1906L0 20.9999c.01875 1.1812.786234 2.5312 1.68309 3.2999L39.8411 57.0064c.7475.6406 1.7.9931 2.6843.9931h11.3492c2.278 0 4.1249-1.8469 4.1249-4.125v-11.003c0-1.1894-.5138-2.3212-1.4087-3.1043L19.1659 7.02062C18.414 6.3625 17.449 6 16.4497 6Z"/><path fill="#000" d="M51.9996 12H12v40h39.9996V12Z"/><path fill="#fff" d="M32.9998 44H17v3h15.9998v-3Z"/><path fill="#fff" d="M17.0117 16.9922h6.4418c1.0506 0 1.9756.1931 2.7763.5787.7999.3857 1.4162.9288 1.8487 1.6294.4325.7006.6487 1.5113.6487 2.4331 0 .9219-.22 1.7488-.6593 2.46-.4394.7113-1.065 1.2613-1.8756 1.6507-.8113.3893-1.7525.5843-2.8244.5843h-3.43v5.67h-2.9262V16.9922Zm7.5406 6.6294c.3681-.1825.6518-.4432.8518-.7825.2-.3394.3-.7344.3-1.1844 0-.45-.1-.8519-.3-1.1844-.2-.3325-.4843-.5894-.8518-.7719-.3682-.1825-.7988-.2731-1.2919-.2731h-3.3231v4.47h3.3231c.4931 0 .9237-.0912 1.2919-.2731v-.0006Zm-2.6313 1.7637h3.1944l3.9337 6.6138h-3.355l-3.7731-6.6138Z"/><path fill="#fff" d="M31.6328 16.9922h4.0731l3.0868 9.8506.2575 1.2863.225-1.2863 2.98-9.8506h4.1375v15.0062h-2.8938V21.2903l.0432-.7825-3.4944 11.4906h-2.1224L34.474 20.5828l.0432.7075v10.7081h-2.8831V16.9922h-.0013Z"/></svg>',
    "rustrover": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="7.67063" x2="61.125" y1="64.3931" y2="39.6094" gradientUnits="userSpaceOnUse"><stop offset=".08" stop-color="#00D886"/><stop offset=".46" stop-color="#FFAB00"/></linearGradient><linearGradient id="b" x1="59.9325" x2="1.33625" y1="59.6763" y2="1.08" gradientUnits="userSpaceOnUse"><stop offset=".19" stop-color="#FFAB00"/><stop offset=".83" stop-color="#FF004C"/></linearGradient></defs><path fill="#00D886" d="M6 47.5494v12.2587c0 2.3038 1.88688 4.1613 4.1906 4.1244l11.0431-.1763c1.1813-.0187 2.2975-.5431 3.0663-1.44l32.7069-38.1581c.6406-.7475.9931-1.7.9931-2.6844V10.125C58 7.84687 56.1531 6 53.875 6H42.8719c-1.1894 0-2.3213.51375-3.1044 1.40875L7.02063 44.8331C6.3625 45.585 6 46.55 6 47.5494Z"/><path fill="url(#a)" d="M6 49.015v10.8619c0 2.2781 1.84687 4.125 4.125 4.125h12.5656c.2 0 .4-.0144.5981-.0438L60.4738 58.51c2.0256-.2969 3.5268-2.0344 3.5268-4.0812V39.0312c0-2.2787-1.8475-4.1256-4.1262-4.1249l-18.5044.0043c-.4256 0-.8488.0663-1.2538.1957L8.87062 45.085c-1.70937.5463-2.86999 2.135-2.86999 3.9294L6 49.015Z"/><path fill="url(#b)" d="M0 4.125v34.1275c0 1.6581.993125 3.155 2.52063 3.8L39.9419 57.85c.5181.2187 1.0756.3294 1.6381.3244l18.3287-.15c2.265-.0188 4.0913-1.86 4.0913-4.125V36.2337c0-.8056-.2356-1.5931-.6781-2.2662L42.2131 1.85938C41.45.69875 40.155 0 38.7663 0H4.125C1.84687 0 0 1.84687 0 4.125Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="M16.9922 16.9922h6.4419c1.0506 0 1.9756.1931 2.7762.5787.8.3857 1.4163.9288 1.8488 1.6294.4325.7006.6487 1.5113.6487 2.4331 0 .9219-.22 1.7488-.6594 2.46-.4393.7113-1.065 1.2613-1.8756 1.6507-.8112.3893-1.7525.5843-2.8244.5843h-3.43v5.67h-2.9262V16.9922Zm7.5406 6.6294c.3681-.1825.6519-.4432.8519-.7825.2-.3394.3-.7344.3-1.1844 0-.45-.1-.8519-.3-1.1844-.2-.3325-.4844-.5894-.8519-.7719-.3681-.1825-.7987-.2731-1.2919-.2731h-3.3231v4.47h3.3231c.4932 0 .9238-.0912 1.2919-.2731v-.0006Zm-2.6312 1.7637h3.1943l3.9338 6.6138h-3.355l-3.7731-6.6138Z"/><path fill="#fff" d="M31.6133 16.9922h6.4419c1.0506 0 1.9756.1931 2.7762.5787.8.3857 1.4169.9288 1.8488 1.6294.4325.7006.6487 1.5113.6487 2.4331 0 .9219-.22 1.7488-.6594 2.46-.4393.7113-1.065 1.2613-1.8756 1.6507-.8112.3893-1.7525.5843-2.8244.5843h-3.43v5.67h-2.9262V16.9922Zm7.5406 6.6294c.3681-.1825.6519-.4432.8519-.7825.2-.3394.3-.7344.3-1.1844 0-.45-.1-.8519-.3-1.1844-.2-.3325-.4844-.5894-.8519-.7719-.3681-.1825-.7987-.2731-1.2919-.2731h-3.3231v4.47h3.3231c.4932 0 .9238-.0912 1.2919-.2731v-.0006Zm-2.6312 1.7637h3.1943l3.9338 6.6138h-3.355l-3.7731-6.6138Z"/></svg>',
    "webstorm": '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 64 64"><defs><linearGradient id="a" x1="7.67063" x2="61.1256" y1="64.3925" y2="39.6094" gradientUnits="userSpaceOnUse"><stop offset=".22" stop-color="#F0EB18"/><stop offset=".59" stop-color="#00C4F4"/></linearGradient><linearGradient id="b" x1="59.9325" x2="1.33687" y1="59.6756" y2="1.07937" gradientUnits="userSpaceOnUse"><stop offset=".19" stop-color="#00C4F4"/><stop offset=".83" stop-color="#007DFE"/></linearGradient></defs><path fill="#F0EB18" d="M6 47.5494v12.2587c0 2.3038 1.88688 4.1613 4.1906 4.1244l11.0431-.1763c1.1813-.0187 2.2975-.5431 3.0663-1.44l32.7069-38.1581c.6406-.7475.9931-1.7.9931-2.6844V10.125C58 7.84687 56.1531 6 53.875 6H42.8719c-1.1894 0-2.3213.51375-3.1044 1.40875L7.02063 44.8331C6.3625 45.585 6 46.55 6 47.5494Z"/><path fill="url(#a)" d="M6 49.015v10.8619c0 2.2781 1.84687 4.125 4.125 4.125h12.5656c.2 0 .4-.0144.5981-.0438L60.4738 58.51c2.0256-.2969 3.5268-2.0344 3.5268-4.0812V39.0312c0-2.2787-1.8475-4.1256-4.1262-4.1249l-18.5044.0043c-.4256 0-.8488.0663-1.2538.1957L8.87062 45.085c-1.70937.5463-2.86999 2.135-2.86999 3.9294L6 49.015Z"/><path fill="url(#b)" d="M0 4.125v34.1275c0 1.6581.993125 3.155 2.52063 3.8L39.9419 57.85c.5181.2187 1.0756.3294 1.6381.3244l18.3287-.15c2.265-.0188 4.0913-1.86 4.0913-4.125V36.2337c0-.8056-.2356-1.5931-.6781-2.2662L42.2131 1.85938C41.45.69875 40.155 0 38.7663 0H4.125C1.84687 0 0 1.84687 0 4.125Z"/><path fill="#000" d="M52 12H12v40h40V12Z"/><path fill="#fff" d="M33 44H17v3h16v-3Z"/><path fill="#fff" d="m19.0513 16.9922 2.4225 10.9544 2.5832-10.9544h2.9581l2.7012 10.9544 2.3475-10.9544h2.9694l-3.6444 15.0062h-3.3337l-2.5294-10.9012-2.5619 10.9012h-3.3231l-3.6231-15.0062h3.0337Z"/><path fill="#fff" d="M38.662 31.6644c-.84-.3931-1.4969-.9431-1.9725-1.6506-.475-.7075-.72-1.5219-.7344-2.4438h2.9369c0 .4356.1143.8181.3431 1.1469.2287.3287.5469.5862.9537.7719.4075.1856.875.2787 1.4044.2787.5294 0 .9519-.0837 1.3344-.2519.3819-.1681.6787-.4018.8894-.7018.2106-.3.3162-.6432.3162-1.0288 0-.4788-.145-.875-.4344-1.19-.2893-.3144-.6875-.5325-1.195-.6538l-2.6475-.5893c-.7143-.1569-1.3362-.4269-1.865-.8094-.5287-.3825-.94-.8556-1.2325-1.42-.2931-.5644-.4393-1.2006-.4393-1.9081 0-.8575.2212-1.6275.6643-2.31.4432-.6825 1.0613-1.215 1.8544-1.5969.7931-.3825 1.6938-.5731 2.7013-.5731 1.0075 0 1.9331.1856 2.7331.5575.8.3719 1.4237.8881 1.8706 1.5487.4463.6613.6731 1.42.6806 2.2775h-2.9262c0-.3643-.0963-.6912-.2894-.9806s-.4662-.5144-.82-.675c-.3537-.1606-.7594-.2412-1.2169-.2412-.4575 0-.8593.0768-1.2056.2306-.3469.1537-.6162.3681-.8094.6431-.1931.275-.2893.595-.2893.9594 0 .4144.1337.7575.4018 1.0287.2682.2719.6338.4644 1.0988.5788l2.5512.5575c.7357.15 1.3913.4344 1.9669.8519.575.4181 1.0238.9325 1.345 1.5437.3213.6113.4825 1.2775.4825 1.9988 0 .8862-.2344 1.6812-.7019 2.385-.4681.7037-1.1237 1.2556-1.9668 1.6562-.8432.4-1.8082.6-2.8938.6-1.0856 0-2.0494-.1969-2.8887-.5894v-.0012Z"/></svg>',
    "writerside": '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="none" viewBox="0 0 48 48"><defs><linearGradient id="a" x1="0" x2="35.1" y1="12.3" y2="40.8" gradientUnits="userSpaceOnUse"><stop stop-color="#FF318C"/><stop offset="1" stop-color="#AF1DF5"/></linearGradient></defs><path fill="url(#a)" d="M5.992 0H48v41.9922h-6.016V5.97617H5.992V0Zm30.016 11.9602V48H0V11.9602h36.008ZM22 39H5.976v3.0398L22 41.9922V39Z"/></svg>',
}
ICON_PLUGIN = WoxImage.new_svg(IDE_LOGOS["idea"])


@dataclass(frozen=True)
class Machine:
    """Where this machine keeps things. A parameter so each OS's rules can be tested on any OS."""

    platform: str
    env: Mapping[str, str]
    home: Path

    @classmethod
    def current(cls) -> Machine:
        """Describe the machine this code runs on."""
        return cls(sys.platform, os.environ, Path.home())

    @property
    def config_root(self) -> Path:
        """Return the folder that holds the IDE vendors' settings."""
        if self.platform == "darwin":
            return self.home / "Library" / "Application Support"
        if self.platform == "win32":
            return Path(self.env.get("APPDATA") or self.home / "AppData" / "Roaming")
        return Path(self.env.get("XDG_CONFIG_HOME") or self.home / ".config")

    @property
    def cache_root(self) -> Path:
        """Return the folder that holds the IDE vendors' caches."""
        if self.platform == "darwin":
            return self.home / "Library" / "Caches"
        if self.platform == "win32":
            return Path(self.env.get("LOCALAPPDATA") or self.home / "AppData" / "Local")
        return Path(self.env.get("XDG_CACHE_HOME") or self.home / ".cache")

    @property
    def toolbox_scripts(self) -> Path:
        """Return the folder where JetBrains Toolbox puts its launchers."""
        if self.platform == "darwin":
            return self.config_root / "JetBrains" / "Toolbox" / "scripts"
        if self.platform == "win32":
            return self.cache_root / "JetBrains" / "Toolbox" / "scripts"
        data_root = Path(self.env.get("XDG_DATA_HOME") or self.home / ".local" / "share")
        return data_root / "JetBrains" / "Toolbox" / "scripts"


@dataclass(frozen=True)
class Project:
    """A recent project, merged across every IDE and IDE version that used it."""

    path: str
    name: str
    last_opened: int  # Epoch milliseconds.
    ides: tuple[Ide, ...]  # Most recently used first.
    aliases: tuple[str, ...] = ()  # Module names that differ from the folder name.


@dataclass
class Snapshot:
    """Everything read from disk in one load."""

    projects: list[Project] = field(default_factory=list)  # Most recently used first.
    launchers: dict[str, tuple[str, ...] | None] = field(default_factory=dict)  # For each IDE seen in recents.
    errors: list[str] = field(default_factory=list)

    def find(self, path: str) -> Project | None:
        """Return the project at path, if it is a recent project."""
        return next((project for project in self.projects if project.path == path), None)


class LauncherNotFoundError(Exception):
    """No way to start an IDE was found."""


def version_dirs(root: Path, ide: Ide) -> list[Path]:
    """List the IDE's per-version folders under root, newest version first."""
    found = []
    for prefix in ide.config_prefixes:
        vendor, product = prefix.split("/")
        # The letters cover editions such as IdeaIC2024.1, PyCharmCE2024.1 or AndroidStudioPreview2024.2.
        pattern = re.compile(rf"{product}[A-Za-z]*(\d+)\.(\d+)")
        try:
            children = list((root / vendor).iterdir())
        except OSError:
            continue
        for child in children:
            match = pattern.fullmatch(child.name)
            if match:
                found.append(((int(match[1]), int(match[2])), child))
    return [folder for _, folder in sorted(found, key=lambda item: item[0], reverse=True)]


def read_recent_entries(recents_file: Path, ide: Ide, home: Path) -> dict[str, int]:
    """Map each usable project path in a recents file to when it was last used, in epoch milliseconds."""
    root = ET.parse(recents_file).getroot()  # noqa: S314 - The user's own IDE wrote this file; defusedxml isn't stdlib.
    entries = {}
    for entry in root.findall(f".//component[@name='{ide.recents_component}']//entry[@key]"):
        info = entry.find(".//RecentProjectMetaInfo")
        if info is not None and info.get("hidden") == "true":
            continue  # IDE internals such as the LightEdit pseudo-project.
        path = entry.attrib["key"].replace("$USER_HOME$", str(home))
        if UNRESOLVED_MACRO.search(path):
            continue
        stamps = [
            int(option.attrib["value"])
            for option in entry.iter("option")
            if option.get("name") in ("activationTimestamp", "projectOpenTimestamp")
            and option.get("value", "").isdigit()
        ]
        if stamps:
            entries[os.path.normpath(path)] = max(stamps)
    return entries


def project_name(path: str) -> str:
    """Name a project after its folder, or its solution for Rider."""
    project = Path(path)
    return project.stem if project.suffix in SOLUTION_SUFFIXES else project.name


def module_names(path: str, name: str) -> tuple[str, ...]:
    """Read the project's module names, so a project can also be found by them."""
    try:
        return tuple(module.stem for module in Path(path, ".idea").glob("*.iml") if module.stem != name)
    except OSError:
        return ()


def launcher_in_install(ide: Ide, install: Path, machine: Machine) -> tuple[str, ...] | None:
    """Build the command that starts an install folder (a macOS .app or its Contents, elsewhere the IDE's root)."""
    if machine.platform == "darwin":
        app = install.parent if install.name == "Contents" else install
        return ("open", "-na", str(app), "--args") if app.suffix == ".app" and app.is_dir() else None
    if machine.platform == "win32":
        executable = install / "bin" / f"{ide.id}64.exe"
        return (str(executable),) if executable.is_file() else None
    for name in (ide.id, f"{ide.id}.sh"):
        script = install / "bin" / name
        if script.is_file() and os.access(script, os.X_OK):
            return (str(script),)
    return None


def launcher_in_known_folders(ide: Ide, machine: Machine) -> tuple[str, ...] | None:
    """Look where macOS and Windows installers usually put an IDE, newest folder first."""
    if machine.platform == "darwin":
        parents = (
            Path("/Applications"),
            machine.home / "Applications",
            machine.home / "Applications" / "JetBrains Toolbox",
        )
        pattern = f"{ide.name}*.app"
    elif machine.platform == "win32":
        program_files = Path(machine.env.get("ProgramFiles") or r"C:\Program Files")
        parents = (program_files / "JetBrains", program_files / "Android", machine.cache_root / "Programs")
        pattern = f"{ide.name}*"
    else:
        return None
    for parent in parents:
        for install in sorted(parent.glob(pattern), reverse=True):
            launcher = launcher_in_install(ide, install, machine)
            if launcher:
                return launcher
    return None


def find_launcher(ide: Ide, machine: Machine, overrides: Mapping[str, str]) -> tuple[str, ...] | None:
    """Find the command that starts an IDE. Names on the PATH can be unrelated tools, so the install comes first."""
    override = overrides.get(ide.id)
    if override:
        is_app = machine.platform == "darwin" and override.endswith(".app")
        return ("open", "-na", override, "--args") if is_app else (override,)

    for folder in version_dirs(machine.cache_root, ide):
        try:
            install = Path((folder / ".home").read_text(encoding="utf-8").strip())
        except OSError:
            continue
        launcher = launcher_in_install(ide, install, machine)
        if launcher:
            return launcher

    search_path = os.pathsep.join((machine.env.get("PATH", ""), str(machine.toolbox_scripts)))
    for command in ide.commands:
        found = shutil.which(command, path=search_path)
        if found:
            return (found,)
    return launcher_in_known_folders(ide, machine)


def load_snapshot(machine: Machine, overrides: Mapping[str, str]) -> Snapshot:
    """Read every IDE's recents, across all its installed versions, and find the launchers they need."""
    snapshot = Snapshot()
    uses: dict[str, dict[Ide, int]] = {}
    for ide in IDES:
        for folder in version_dirs(machine.config_root, ide):
            recents_file = folder / "options" / ide.recents_file
            try:
                entries = read_recent_entries(recents_file, ide, machine.home)
            except FileNotFoundError:
                continue
            except (OSError, ET.ParseError) as error:
                snapshot.errors.append(f"cannot read {recents_file}: {error}")
                continue
            for path, stamp in entries.items():
                project_uses = uses.setdefault(path, {})
                project_uses[ide] = max(stamp, project_uses.get(ide, 0))

    for path, project_uses in uses.items():
        if not Path(path).exists():
            continue
        ides = sorted(project_uses, key=lambda ide: project_uses[ide], reverse=True)
        name = project_name(path)
        snapshot.projects.append(Project(path, name, project_uses[ides[0]], tuple(ides), module_names(path, name)))
    snapshot.projects.sort(key=lambda project: project.last_opened, reverse=True)

    seen_ides = {ide for project in snapshot.projects for ide in project.ides}
    snapshot.launchers = {ide.id: find_launcher(ide, machine, overrides) for ide in seen_ides}
    return snapshot


def parse_overrides(raw: str) -> dict[str, str]:
    """Read the launchers setting, a JSON list of {"ide", "path"} rows, into a map of IDE id to path."""
    try:
        rows = json.loads(raw or "[]")
    except ValueError:
        return {}
    if not isinstance(rows, list):
        return {}
    overrides = {}
    for row in rows:
        if isinstance(row, dict) and row.get("ide") and row.get("path"):
            overrides[str(row["ide"])] = str(Path(str(row["path"])).expanduser())
    return overrides


def fold(text: str) -> str:
    """Normalize text for matching: ignore case and accents."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char)).casefold()


def substring_score(term: str, text: str, position: int) -> int:
    """Score a term found inside text at position, preferring the start of a word."""
    while position != -1:
        if not text[position - 1].isalnum():
            return 80
        position = text.find(term, position + 1)
    return 60


def fuzzy_score(term: str, text: str) -> int:
    """Score a term whose characters appear in order: the tighter they sit together, the better."""
    start = None
    position = -1
    for char in term:
        position = text.find(char, position + 1)
        if position == -1:
            return 0
        if start is None:
            start = position
    span = position - start + 1
    if span > FUZZY_MAX_SPREAD * len(term):
        return 0  # Letters scattered this far apart are a coincidence, not a match.
    return 20 + 30 * len(term) // span


def match_score(term: str, text: str) -> int:
    """Score how well a folded term matches folded text: 0 is no match, 100 is exact, under 50 is fuzzy."""
    if term == text:
        return 100
    position = text.find(term)
    if position == 0:
        return 90
    return substring_score(term, text, position) if position > 0 else fuzzy_score(term, text)


def project_score(terms: list[str], project: Project, *, match_path: bool) -> int:
    """Score a project on its weakest search term, so that every term has to match."""
    names = [fold(name) for name in (project.name, *project.aliases)]
    path = fold(project.path) if match_path else ""
    weakest = 100
    for term in terms:
        best = max(match_score(term, name) for name in names)
        if path and match_score(term, path) >= GLOBAL_MIN_SCORE:  # Fuzzy matching a long path would match anything.
            best = max(best, PATH_MATCH_SCORE)
        if best == 0:
            return 0
        weakest = min(weakest, best)
    return weakest


def rank_projects(
    projects: list[Project], search: str, *, match_path: bool = False, min_score: int = 1
) -> list[tuple[Project, int]]:
    """Filter projects by search, best match first and most recent first among equals."""
    terms = fold(search).split()
    if not terms:
        return [(project, 0) for project in projects]
    scored = ((project, project_score(terms, project, match_path=match_path)) for project in projects)
    ranked = [pair for pair in scored if pair[1] >= min_score]
    ranked.sort(key=lambda pair: (-pair[1], -pair[0].last_opened))
    return ranked


def format_age(last_opened: int, now: int | None = None) -> str:
    """Format how long ago an epoch-millisecond time was, in a short form that needs no translation."""
    if last_opened <= 0:
        return ""
    now = int(time.time() * 1000) if now is None else now
    minutes = (now - last_opened) // 60000
    if minutes < 1:
        return "now"
    for limit, divisor, unit in ((60, 1, "m"), (1440, 60, "h"), (43200, 1440, "d"), (525600, 43200, "mo")):
        if minutes < limit:
            return f"{minutes // divisor}{unit}"
    return f"{minutes // 525600}y"


def display_path(path: str, home: Path) -> str:
    """Shorten the home folder to ~."""
    return "~" + path[len(str(home)) :] if path == str(home) or path.startswith(f"{home}{os.sep}") else path


def spawn_detached(argv: tuple[str, ...]) -> subprocess.Popen:
    """Start a process that outlives Wox, without passing on what Wox's plugin host set for itself."""
    env = {key: value for key, value in os.environ.items() if not key.startswith("WOX_") and key != "SHIV_ROOT"}
    options: dict = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if sys.platform == "win32":
        options["creationflags"] = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        options["start_new_session"] = True
    return subprocess.Popen(list(argv), cwd=Path.home(), env=env, **options)  # noqa: S603 - No shell, and the command is the user's own IDE.


async def run_detached(argv: tuple[str, ...]) -> None:
    """Start argv and raise OSError if it cannot start or fails right away."""
    process = await asyncio.to_thread(spawn_detached, argv)
    try:
        code = await asyncio.to_thread(process.wait, LAUNCH_CHECK_SECONDS)
    except subprocess.TimeoutExpired:
        # On a first launch the launcher is the IDE itself, so keep it from becoming a zombie when it exits.
        threading.Thread(target=process.wait, daemon=True).start()
        return
    if code != 0:
        message = f"{argv[0]} exited with code {code}"
        raise OSError(message)


def project_folder(path: str) -> str:
    """Return a project's folder. A Rider project is a file, so that is the folder it sits in."""
    project = Path(path)
    return str(project if project.is_dir() else project.parent)


async def open_folder(path: str) -> None:
    """Show a project in the file manager."""
    folder = await asyncio.to_thread(project_folder, path)
    if sys.platform == "win32":
        # explorer.exe reports failure even when it succeeds, so it can't go through run_detached.
        os.startfile(folder)  # noqa: S606 - Opens the project's own folder.
    else:
        await run_detached(("open" if sys.platform == "darwin" else "xdg-open", folder))


class JetBrainsProjectPlugin:
    """The plugin that Wox loads."""

    def __init__(self) -> None:
        """Start with no data: init() triggers the first load."""
        self.api = None
        self.snapshot = Snapshot()
        self.loaded_at = 0.0  # time.monotonic() of the last load, 0 when the snapshot needs loading.
        self.refresh_task: asyncio.Task | None = None
        self.match_path = False
        self.overrides: dict[str, str] = {}
        self.open_in_label = "Open in {ide}"

    async def init(self, ctx: Context, params: PluginInitParams) -> None:
        """Read the settings, register the callbacks and tools, and start loading projects."""
        self.api = params.api
        self.match_path = await self.api.get_setting(ctx, "match_path") == "true"
        self.overrides = parse_overrides(await self.api.get_setting(ctx, "launchers"))
        self.open_in_label = await self.api.get_translation(ctx, "action_open_in")
        await self.api.on_setting_changed(ctx, self._on_setting_changed)
        await self.api.on_mru_restore(ctx, self._on_mru_restore)
        await self._register_tools(ctx)
        self._start_refresh(ctx)  # Global queries and MRU restores need data but never wait for it.

    async def query(self, ctx: Context, query: Query) -> QueryResponse:
        """Answer a jb query or, if the user added the * keyword, a global query."""
        search = query.search.strip()
        is_global = not query.trigger_keyword
        if is_global and len(search) < GLOBAL_MIN_SEARCH_LENGTH:
            return QueryResponse(results=[])

        await self._ensure_fresh(ctx, wait=not is_global)
        if is_global:
            # Global search matches names only, and keeps Wox's shared score scale so it can mix with other plugins.
            ranked = rank_projects(self.snapshot.projects, search, min_score=GLOBAL_MIN_SCORE)
            return QueryResponse(results=[self._build_result(project, score) for project, score in ranked])

        ranked = rank_projects(self.snapshot.projects, search, match_path=self.match_path)
        if not ranked:
            return QueryResponse(results=[self._build_empty_state()])
        # Wox sorts by score, so turn the order decided above into scores.
        total = len(ranked)
        return QueryResponse(
            results=[self._build_result(project, total - index) for index, (project, _) in enumerate(ranked)]
        )

    def _start_refresh(self, ctx: Context) -> asyncio.Task:
        """Start reloading the snapshot unless a reload is already running."""
        if self.refresh_task is None:
            self.refresh_task = asyncio.create_task(self._refresh(ctx))
        return self.refresh_task

    async def _refresh(self, ctx: Context) -> None:
        try:
            self.snapshot = await asyncio.to_thread(load_snapshot, Machine.current(), self.overrides)
            for error in self.snapshot.errors:
                await self.api.log(ctx, LogLevel.WARNING, error)
        except Exception as error:  # noqa: BLE001 - Keep serving the last good data: a reload must not fail a query.
            await self.api.log(ctx, LogLevel.ERROR, f"cannot load JetBrains projects: {error!r}")
        finally:
            self.loaded_at = time.monotonic()
            self.refresh_task = None

    async def _ensure_fresh(self, ctx: Context, *, wait: bool) -> None:
        max_age = FOREGROUND_REFRESH_SECONDS if wait else BACKGROUND_REFRESH_SECONDS
        if self.loaded_at and time.monotonic() - self.loaded_at < max_age:
            return
        task = self._start_refresh(ctx)
        if wait:
            await task

    def _on_setting_changed(self, _ctx: Context, key: str, value: str) -> None:
        if key == "match_path":
            self.match_path = value == "true"
        elif key == "launchers":
            self.overrides = parse_overrides(value)
            self.loaded_at = 0.0

    def _on_mru_restore(self, _ctx: Context, mru_data: MRUData) -> Result | None:
        """Rebuild a start-page row from memory only: Wox drops the row if this takes over 300 ms."""
        data = mru_data.context_data or {}
        path = data.get("path", "")
        project = self.snapshot.find(path)
        if project is None:
            ide = IDE_BY_ID.get(data.get("ide", ""))
            if self.loaded_at or not path or ide is None:
                return None  # The project is gone, or the row's data is unusable.
            project = Project(path, data.get("name") or project_name(path), 0, (ide,))
        return self._build_result(project)

    def _build_result(self, project: Project, score: int = 0) -> Result:
        tails = []
        age = format_age(project.last_opened)
        if age:
            tails.append(ResultTail(text=age))
        if len(self.snapshot.launchers) > 1:  # With a single IDE, its name on every row would add nothing.
            tails.append(ResultTail(text=project.ides[0].name))
        if self.loaded_at and self.snapshot.launchers.get(project.ides[0].id) is None:
            tails.append(ResultTail(text="i18n:tail_no_launcher", text_category=ResultTailTextCategory.WARNING))

        return Result(
            title=project.name,
            sub_title=display_path(project.path, Path.home()),
            icon=WoxImage.new_svg(IDE_LOGOS[project.ides[0].id]),
            identity_key=project.path,
            score=score,
            tails=tails,
            actions=self._build_actions(project),
        )

    def _build_actions(self, project: Project) -> list[ResultAction]:
        context = {"path": project.path, "name": project.name, "ide": project.ides[0].id}

        def open_in(ide: Ide, *, is_default: bool) -> ResultAction:
            async def run(ctx: Context, _: ActionContext) -> None:
                await self._open_from_action(ctx, project.path, ide)

            label = self.open_in_label.replace("{ide}", ide.name)
            return ResultAction(name=label, icon=ICON_OPEN, is_default=is_default, action=run, context_data=context)

        async def copy_path(ctx: Context, _: ActionContext) -> None:
            await self.api.copy(ctx, CopyParams(text=project.path))

        async def show_folder(ctx: Context, _: ActionContext) -> None:
            try:
                await open_folder(project.path)
            except OSError as error:
                await self._notify_open_failed(ctx, project.path, error)

        return [
            *(open_in(ide, is_default=index == 0) for index, ide in enumerate(project.ides)),
            ResultAction(name="i18n:action_copy_path", icon=ICON_COPY, action=copy_path, context_data=context),
            ResultAction(name="i18n:action_open_folder", icon=ICON_FOLDER, action=show_folder, context_data=context),
        ]

    def _build_empty_state(self) -> Result:
        if not self.snapshot.projects:
            return Result(title="i18n:empty_title", sub_title="i18n:empty_subtitle", icon=ICON_PLUGIN)
        hint = "" if self.match_path else "i18n:no_match_subtitle"  # The hint suggests turning on path matching.
        return Result(title="i18n:no_match_title", sub_title=hint, icon=ICON_PLUGIN)

    async def _open_in_ide(self, ctx: Context, path: str, ide: Ide) -> None:
        """Open path in ide. Raises LauncherNotFoundError or OSError."""
        if not self.loaded_at:
            await self._ensure_fresh(ctx, wait=True)  # A row restored from MRU can run before the first load.
        launcher = self.snapshot.launchers.get(ide.id)
        if launcher is None:
            raise LauncherNotFoundError(ide.name)
        await run_detached((*launcher, path))

    async def _open_from_action(self, ctx: Context, path: str, ide: Ide) -> None:
        try:
            await self._open_in_ide(ctx, path, ide)
        except LauncherNotFoundError:
            message = await self.api.get_translation(ctx, "launcher_missing")
            await self.api.notify(ctx, message.replace("{ide}", ide.name))
        except OSError as error:
            await self._notify_open_failed(ctx, path, error)

    async def _notify_open_failed(self, ctx: Context, target: str, error: OSError) -> None:
        message = await self.api.get_translation(ctx, "open_failed")
        await self.api.notify(ctx, message.replace("{target}", target).replace("{error}", str(error)))
        await self.api.log(ctx, LogLevel.ERROR, f"cannot open {target}: {error!r}")

    async def _register_tools(self, ctx: Context) -> None:
        tools = (
            (
                PluginToolDescriptor(
                    name="search_projects",
                    description="i18n:tool_search",
                    input_schema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search terms. Leave out to list recent projects.",
                            },
                            "limit": {"type": "integer", "minimum": 1, "maximum": 200},
                        },
                    },
                    output_schema={
                        "type": "object",
                        "properties": {
                            "projects": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "path": {"type": "string"},
                                        "lastOpened": {"type": "integer"},
                                        "ides": {"type": "array", "items": {"type": "string"}},
                                    },
                                    "required": ["name", "path", "lastOpened", "ides"],
                                },
                            }
                        },
                        "required": ["projects"],
                    },
                    annotations=PluginToolAnnotations(read_only=True, idempotent=True),
                ),
                self._tool_search_projects,
            ),
            (
                PluginToolDescriptor(
                    name="open_project",
                    description="i18n:tool_open",
                    input_schema={
                        "type": "object",
                        "properties": {
                            "path": {"type": "string", "description": "A path returned by search_projects."},
                            "ide": {
                                "type": "string",
                                "enum": [ide.id for ide in IDES],
                                "description": "Defaults to the IDE that last used the project.",
                            },
                        },
                        "required": ["path"],
                    },
                    output_schema={
                        "type": "object",
                        "properties": {"path": {"type": "string"}, "ide": {"type": "string"}},
                        "required": ["path", "ide"],
                    },
                    annotations=PluginToolAnnotations(requires_ui=True),
                ),
                self._tool_open_project,
            ),
        )
        for descriptor, handler in tools:
            result = await self.api.register_plugin_tool(
                ctx, RegisterPluginToolOption(tool=descriptor, handler=handler)
            )
            if result.error:
                await self.api.log(ctx, LogLevel.ERROR, f"cannot register {descriptor.name}: {result.error.message}")

    async def _tool_search_projects(
        self, ctx: Context, option: InvokePluginToolHandlerOption
    ) -> InvokePluginToolHandlerResult:
        await self._ensure_fresh(ctx, wait=True)
        ranked = rank_projects(self.snapshot.projects, option.arguments.get("query", ""), match_path=self.match_path)
        projects = [
            {
                "name": project.name,
                "path": project.path,
                "lastOpened": project.last_opened,
                "ides": [ide.id for ide in project.ides],
            }
            for project, _ in ranked[: option.arguments.get("limit", 20)]
        ]
        return InvokePluginToolHandlerResult(output={"projects": projects})

    async def _tool_open_project(
        self, ctx: Context, option: InvokePluginToolHandlerOption
    ) -> InvokePluginToolHandlerResult:
        await self._ensure_fresh(ctx, wait=True)
        path = option.arguments["path"]
        project = self.snapshot.find(path)
        if project is None:
            return _tool_error("PROJECT_NOT_FOUND", f"not a recent JetBrains project: {path}")
        ide = IDE_BY_ID.get(option.arguments.get("ide", "")) or project.ides[0]
        try:
            await self._open_in_ide(ctx, path, ide)
        except LauncherNotFoundError:
            return _tool_error("LAUNCHER_NOT_FOUND", f"no launcher found for {ide.name}")
        except OSError as error:
            return _tool_error("EXECUTION_FAILED", str(error))
        return InvokePluginToolHandlerResult(output={"path": path, "ide": ide.id})


def _tool_error(code: str, message: str) -> InvokePluginToolHandlerResult:
    return InvokePluginToolHandlerResult(error=PluginToolError(code=code, message=message))


plugin = JetBrainsProjectPlugin()
