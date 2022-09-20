from __future__ import annotations

import typing

import pydantic


class ContainerType(pydantic.BaseModel):
    @staticmethod
    def list(value: TypeReference) -> ContainerType:
        return ContainerType(__root__=_ContainerType(type="set"))

    @staticmethod
    def map(value: MapType) -> ContainerType:
        return ContainerType(__root__=_ContainerType(type="set"))

    @staticmethod
    def optional(value: TypeReference) -> ContainerType:
        return ContainerType(__root__=_ContainerType(type="set"))

    @staticmethod
    def set(value: TypeReference) -> ContainerType:
        return ContainerType(__root__=_ContainerType(type="set"))


from .map_type import MapType  # noqa: E402
from .type_reference import TypeReference  # noqa: E402


class _ContainerType:
    class List(pydantic.BaseModel):
        type: typing.Literal["list"] = pydantic.Field(alias="_type")
        value: TypeReference

        class Config:
            allow_population_by_field_name = True

    class Map(MapType):
        type: typing.Literal["map"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Optional(pydantic.BaseModel):
        type: typing.Literal["optional"] = pydantic.Field(alias="_type")
        value: TypeReference

        class Config:
            allow_population_by_field_name = True

    class Set(pydantic.BaseModel):
        type: typing.Literal["set"] = pydantic.Field(alias="_type")
        value: TypeReference

        class Config:
            allow_population_by_field_name = True


ContainerType.update_forward_refs()
