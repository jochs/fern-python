# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .binary_tree_value import BinaryTreeValue
from .doubly_linked_list_value import DoublyLinkedListValue
from .key_value_pair import KeyValuePair
from .map_value import MapValue
from .singly_linked_list_value import SinglyLinkedListValue


class VariableValue_IntegerValue(pydantic.BaseModel):
    type: typing_extensions.Literal["integerValue"]
    value: int

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_BooleanValue(pydantic.BaseModel):
    type: typing_extensions.Literal["booleanValue"]
    value: bool

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_DoubleValue(pydantic.BaseModel):
    type: typing_extensions.Literal["doubleValue"]
    value: float

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_StringValue(pydantic.BaseModel):
    type: typing_extensions.Literal["stringValue"]
    value: str

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_CharValue(pydantic.BaseModel):
    type: typing_extensions.Literal["charValue"]
    value: str

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_MapValue(MapValue):
    type: typing_extensions.Literal["mapValue"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_ListValue(pydantic.BaseModel):
    type: typing_extensions.Literal["listValue"]
    value: typing.List[VariableValue]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_BinaryTreeValue(BinaryTreeValue):
    type: typing_extensions.Literal["binaryTreeValue"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_SinglyLinkedListValue(SinglyLinkedListValue):
    type: typing_extensions.Literal["singlyLinkedListValue"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_DoublyLinkedListValue(DoublyLinkedListValue):
    type: typing_extensions.Literal["doublyLinkedListValue"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class VariableValue_NullValue(pydantic.BaseModel):
    type: typing_extensions.Literal["nullValue"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


VariableValue = typing_extensions.Annotated[
    typing.Union[
        VariableValue_IntegerValue,
        VariableValue_BooleanValue,
        VariableValue_DoubleValue,
        VariableValue_StringValue,
        VariableValue_CharValue,
        VariableValue_MapValue,
        VariableValue_ListValue,
        VariableValue_BinaryTreeValue,
        VariableValue_SinglyLinkedListValue,
        VariableValue_DoublyLinkedListValue,
        VariableValue_NullValue,
    ],
    pydantic.Field(discriminator="type"),
]
VariableValue_MapValue.update_forward_refs(KeyValuePair=KeyValuePair, MapValue=MapValue, VariableValue=VariableValue)
