from __future__ import annotations

from typing import List, Sequence, Set

from ....ast_node import AstNode, GenericTypeVar, NodeWriter, ReferenceResolver
from ....references import ClassReference, Reference
from ..function import FunctionDeclaration, FunctionParameter
from ..variable import VariableDeclaration
from .class_constructor import ClassConstructor


class ClassDeclaration(AstNode):
    def __init__(self, name: str, extends: Sequence[ClassReference] = None, constructor: ClassConstructor = None):
        self.name = name
        self.extends = extends or []
        self.constructor = constructor
        self.statements: List[AstNode] = []

    def add_attribute(self, variable_declaration: VariableDeclaration) -> None:
        self.statements.append(variable_declaration)

    def add_method(
        self,
        declaration: FunctionDeclaration,
        is_static: bool = False,
    ) -> FunctionDeclaration:
        """
            - adds 'self' parameter to signature if not static
            - adds @staticmethod decorator if static
        returns new declaration
        """
        parameters = (
            declaration.parameters if is_static else [FunctionParameter(name="self")] + list(declaration.parameters)
        )

        decorators = (
            list(declaration.decorators) + [Reference(qualified_name_excluding_import=("staticmethod",))]
            if is_static
            else declaration.decorators
        )

        declaration = FunctionDeclaration(
            name=declaration.name,
            parameters=parameters,
            return_type=declaration.return_type,
            body=declaration.body,
            decorators=decorators,
        )

        self.statements.append(declaration)

        return declaration

    def add_class(self, declaration: ClassDeclaration) -> None:
        self.statements.append(declaration)

    def get_references(self) -> Set[Reference]:
        references: Set[Reference] = set(self.extends)
        if self.constructor is not None:
            references.update(self.constructor.get_references())
        for statement in self.statements:
            references.update(statement.get_references())
        return references

    def get_generics(self) -> Set[GenericTypeVar]:
        generics: Set[GenericTypeVar] = set()
        if self.constructor is not None:
            generics.update(self.constructor.get_generics())
        for statement in self.statements:
            generics.update(statement.get_generics())
        return generics

    def write(self, writer: NodeWriter, reference_resolver: ReferenceResolver) -> None:
        top_line = f"class {self.name}"
        if len(self.extends) > 0:
            top_line += f"({', '.join(reference_resolver.resolve_reference(r) for r in self.extends)})"
        top_line += ":"
        writer.write_line(top_line)

        with writer.indent():
            for statement in self.statements:
                writer.write_node(statement)
            if len(self.statements) == 0:
                writer.write("pass")
            writer.write_line()