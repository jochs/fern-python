from __future__ import annotations

import typing

import pydantic

from .declared_type_name import DeclaredTypeName
from .single_union_type_property import SingleUnionTypeProperty


class SingleUnionTypeProperties(pydantic.BaseModel):
    @staticmethod
    def same_properties_as_object(value: DeclaredTypeName) -> SingleUnionTypeProperties:
        return SingleUnionTypeProperties(__root__=_SingleUnionTypeProperties(properties_type="noProperties"))

    @staticmethod
    def single_property(value: SingleUnionTypeProperty) -> SingleUnionTypeProperties:
        return SingleUnionTypeProperties(__root__=_SingleUnionTypeProperties(properties_type="noProperties"))

    @staticmethod
    def no_properties() -> SingleUnionTypeProperties:
        return SingleUnionTypeProperties(__root__=_SingleUnionTypeProperties(properties_type="noProperties"))


class _SingleUnionTypeProperties:
    class SamePropertiesAsObject(DeclaredTypeName):
        properties_type: typing.Literal["samePropertiesAsObject"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class SingleProperty(SingleUnionTypeProperty):
        properties_type: typing.Literal["singleProperty"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class NoProperties(pydantic.BaseModel):
        properties_type: typing.Literal["noProperties"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True
