from __future__ import annotations

import typing

import pydantic

from .container_type import ContainerType
from .primitive_type import PrimitiveType
from .resolved_named_type import ResolvedNamedType


class ResolvedTypeReference(pydantic.BaseModel):
    @staticmethod
    def container(value: ContainerType) -> ResolvedTypeReference:
        return ResolvedTypeReference(__root__=_ResolvedTypeReference(type="void"))

    @staticmethod
    def named(value: ResolvedNamedType) -> ResolvedTypeReference:
        return ResolvedTypeReference(__root__=_ResolvedTypeReference(type="void"))

    @staticmethod
    def primitive(value: PrimitiveType) -> ResolvedTypeReference:
        return ResolvedTypeReference(__root__=_ResolvedTypeReference(type="void"))

    @staticmethod
    def unknown() -> ResolvedTypeReference:
        return ResolvedTypeReference(__root__=_ResolvedTypeReference(type="void"))

    @staticmethod
    def void() -> ResolvedTypeReference:
        return ResolvedTypeReference(__root__=_ResolvedTypeReference(type="void"))


class _ResolvedTypeReference:
    class Container(pydantic.BaseModel):
        type: typing.Literal["container"] = pydantic.Field(alias="_type")
        value: ContainerType

        class Config:
            allow_population_by_field_name = True

    class Named(ResolvedNamedType):
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
