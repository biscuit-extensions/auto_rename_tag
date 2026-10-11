from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class AutoRenameTag(Extension):
    """Automatically synchronize opening and closing HTML/XML tags"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("Auto Rename Tag extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("Auto Rename Tag installed successfully.")
