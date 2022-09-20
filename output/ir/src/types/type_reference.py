from __future__ import annotations

import typing

import pydantic

from .declared_type_name import DeclaredTypeName
from .primitive_type import PrimitiveType


class TypeReference(pydantic.BaseModel):
    @staticmethod
    def container(value: ContainerType) -> TypeReference:
        return TypeReference(__root__=_TypeReference(type="void"))

    @staticmethod
    def named(value: DeclaredTypeName) -> TypeReference:
        return TypeReference(__root__=_TypeReference(type="void"))

    @staticmethod
    def primitive(value: PrimitiveType) -> TypeReference:
        return TypeReference(__root__=_TypeReference(type="void"))

    @staticmethod
    def unknown() -> TypeReference:
        return TypeReference(__root__=_TypeReference(type="void"))

    @staticmethod
    def void() -> TypeReference:
        return TypeReference(__root__=_TypeReference(type="void"))


from .container_type import ContainerType  # noqa: E402


class _TypeReference:
    class Container(pydantic.BaseModel):
        type: typing.Literal["container"] = pydantic.Field(alias="_type")
        value: ContainerType

        class Config:
            allow_population_by_field_name = True

    class Named(DeclaredTypeName):
        type: typing.Literal["named"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Primitive(pydantic.BaseModel):
        type: typing.Literal["primitive"] = pydantic.Field(alias="_type")
        value: PrimitiveType

        class Config:
            allow_population_by_field_name = True

    class Unknown(pydantic.BaseModel):
        type: typing.Literal["unknown"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Void(pydantic.BaseModel):
        type: typing.Literal["void"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True


TypeReference.update_forward_refs()
