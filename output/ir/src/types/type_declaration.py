from types.declared_type_name import DeclaredTypeName
from types.type import Type

from commons.with_docs import WithDocs


class TypeDeclaration(WithDocs):

    name: DeclaredTypeName
    shape: Type
