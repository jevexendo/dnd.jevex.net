from __future__ import annotations

import re

import mkdocs.plugins
from mkdocs.config import Config
from mkdocs.config.config_options import Type as ConfigType
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin, get_plugin_logger
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

log = get_plugin_logger(__name__)


class DungeonsConfig(Config):
    foo = ConfigType(str, default="a default value")


class DungeonsPlugin(BasePlugin[DungeonsConfig]):
    @mkdocs.plugins.event_priority(-50)
    def on_page_markdown(self, markdown: str, /, *, page: Page, config: MkDocsConfig, files: Files):
        path = page.file.src_uri
        for m in re.finditer(r"\bhttp://[^) ]+", markdown):
            log.warning(f"Documentation file '{path}' contains a non-HTTPS link: {m[0]}")
