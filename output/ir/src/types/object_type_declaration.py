import typing
from types.declared_type_name import DeclaredTypeName
from types.object_property import ObjectProperty

import pydantic


class ObjectTypeDeclaration(pydantic.BaseModel):

    extends: typing.List[DeclaredTypeName]
    properties: typing.List[ObjectProperty]
