from __future__ import annotations

from typing import TYPE_CHECKING, Sequence, Set, Tuple

from ....ast_node import AstNode, NodeWriter, ReferenceResolver
from ....references import Reference


class FunctionInvocation(AstNode):
    def __init__(
        self,
        function_definition: Reference,
        args: Sequence[Expression] = None,
        kwargs: Sequence[Tuple[str, Expression]] = None,
    ):
        self.function_definition = function_definition
        self.args = args or []
        self.kwargs = kwargs or []

    def get_references(self) -> Set[Reference]:
        references = set()
        references.add(self.function_definition)
        for arg in self.args:
            references.update(arg.get_references())
        for kwarg in self.kwargs:
            references.update(kwarg[1].get_references())
        return references

    def write(self, writer: NodeWriter, reference_resolver: ReferenceResolver) -> None:
        writer.write(f"{reference_resolver.resolve_reference(self.function_definition)}(")
        for i, arg in enumerate(self.args):
            arg.write(writer=writer, reference_resolver=reference_resolver)
            if i < len(self.args) - 1:
                writer.write(", ")
        for i, (name, value) in enumerate(self.kwargs):
            writer.write(f"{name}=")
            arg.write(writer=writer, reference_resolver=reference_resolver)
            if i < len(self.args) - 1:
                writer.write(", ")
        writer.write(")")


if TYPE_CHECKING:
    from ..expression import Expression
