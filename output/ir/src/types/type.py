from __future__ import annotations

import typing

import pydantic

from .alias_type_declaration import AliasTypeDeclaration
from .enum_type_declaration import EnumTypeDeclaration
from .object_type_declaration import ObjectTypeDeclaration
from .union_type_declaration import UnionTypeDeclaration


class Type(pydantic.BaseModel):
    @staticmethod
    def alias(value: AliasTypeDeclaration) -> Type:
        return Type(__root__=_Type(type="union"))

    @staticmethod
    def enum(value: EnumTypeDeclaration) -> Type:
        return Type(__root__=_Type(type="union"))

    @staticmethod
    def object(value: ObjectTypeDeclaration) -> Type:
        return Type(__root__=_Type(type="union"))

    @staticmethod
    def union(value: UnionTypeDeclaration) -> Type:
        return Type(__root__=_Type(type="union"))


class _Type:
    class Alias(AliasTypeDeclaration):
        type: typing.Literal["alias"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Enum(EnumTypeDeclaration):
        type: typing.Literal["enum"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Object(ObjectTypeDeclaration):
        type: typing.Literal["object"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Union(UnionTypeDeclaration):
        type: typing.Literal["union"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True
