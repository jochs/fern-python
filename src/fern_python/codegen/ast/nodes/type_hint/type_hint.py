from __future__ import annotations

from typing import Sequence, Set, Union

from ...ast_node import AstNode, NodeWriter, ReferenceResolver
from ...references import ClassReference, Reference, ReferenceImport
from ..code_writer import CodeWriter


def get_reference_to_typing_import(name: str) -> ClassReference:
    return ClassReference(
        import_=ReferenceImport(
            module=("typing",),
        ),
        qualified_name_excluding_import=(name,),
    )


def get_reference_to_built_in_primitive(name: str) -> ClassReference:
    return ClassReference(
        qualified_name_excluding_import=(name,),
    )


class TypeHint(AstNode):
    def __init__(
        self,
        reference: ClassReference,
        type_parameters: Sequence[Union[TypeHint, CodeWriter]] = None,
    ):
        self._reference = reference
        self._type_parameters = type_parameters or []

    @staticmethod
    def str() -> TypeHint:
        return TypeHint(reference=get_reference_to_built_in_primitive("str"))

    @staticmethod
    def bool() -> TypeHint:
        return TypeHint(reference=get_reference_to_built_in_primitive("bool"))

    @staticmethod
    def int() -> TypeHint:
        return TypeHint(reference=get_reference_to_built_in_primitive("int"))

    @staticmethod
    def float() -> TypeHint:
        return TypeHint(reference=get_reference_to_built_in_primitive("float"))

    @staticmethod
    def none() -> TypeHint:
        return TypeHint(reference=get_reference_to_built_in_primitive("None"))

    @staticmethod
    def optional(wrapped_type: TypeHint) -> TypeHint:
        return TypeHint(
            reference=get_reference_to_typing_import("Optional"),
            type_parameters=[wrapped_type],
        )

    @staticmethod
    def list(wrapped_type: TypeHint) -> TypeHint:
        return TypeHint(
            reference=get_reference_to_typing_import("List"),
            type_parameters=[wrapped_type],
        )

    @staticmethod
    def set(wrapped_type: TypeHint) -> TypeHint:
        return TypeHint(
            reference=get_reference_to_typing_import("Set"),
            type_parameters=[wrapped_type],
        )

    @staticmethod
    def dict(key_type: TypeHint, value_type: TypeHint) -> TypeHint:
        return TypeHint(
            reference=get_reference_to_typing_import("Dict"),
            type_parameters=[key_type, value_type],
        )

    @staticmethod
    def any() -> TypeHint:
        return TypeHint(reference=get_reference_to_typing_import("Optional"))

    @staticmethod
    def annotated(type: TypeHint, annotation: CodeWriter) -> TypeHint:
        return TypeHint(
            reference=ClassReference(
                import_=ReferenceImport(
                    module=("typing_extensions",),
                ),
                qualified_name_excluding_import=("Annotated",),
            ),
            type_parameters=[annotation],
        )

    def get_references(self) -> Set[Reference]:
        references: Set[Reference] = set()
        references.add(self._reference)
        for type_parameter in self._type_parameters:
            references.update(type_parameter.get_references())
        return references

    def write(self, writer: NodeWriter, reference_resolver: ReferenceResolver) -> None:
        writer.write(reference_resolver.resolve_reference(self._reference))
        if len(self._type_parameters) > 0:
            writer.write("[")
            for i, type_parameter in enumerate(self._type_parameters):
                type_parameter.write(writer=writer, reference_resolver=reference_resolver)
                if i < len(self._type_parameters) - 1:
                    writer.write(", ")
            writer.write("]")
