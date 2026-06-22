from __future__ import annotations

from typing import TYPE_CHECKING

import tomlrt

if TYPE_CHECKING:
    from tomlrt import Document

    from hatch.utils.fs import Path


def save_toml_document(document: Document, path: Path):
    path.ensure_parent_dir_exists()
    path.write_atomic(tomlrt.dumps(document), "w", encoding="utf-8")


def create_toml_document(config: dict) -> Document:
    return tomlrt.Document(config)
