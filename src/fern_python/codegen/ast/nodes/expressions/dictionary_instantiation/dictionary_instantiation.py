from __future__ import annotations

from typing import TYPE_CHECKING, Sequence, Tuple

from ....ast_node import AstNode, AstNodeMetadata, NodeWriter


class DictionaryInstantiation(AstNode):
    def __init__(
        self,
        entries: Sequence[Tuple[Expression, Expression]] = None,
    ):
        self.entries = entries or []

    def get_metadata(self) -> AstNodeMetadata:
        metadata = AstNodeMetadata()
        for entry in self.entries:
            metadata.update(entry[0].get_metadata())
            metadata.update(entry[1].get_metadata())
        return metadata

    def write(self, writer: NodeWriter) -> None:
        writer.write("{")
        for index, (key, value) in enumerate(self.entries):
            if index > 0:
                writer.write(", ")
            writer.write_node(key)
            writer.write(": ")
            writer.write_node(value)
        writer.write("}")


if TYPE_CHECKING:
    from ..expression import Expression