# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime


class GenericValue(pydantic.BaseModel):
    stringified_type: typing.Optional[str] = pydantic.Field(alias="stringifiedType")
    stringified_value: str = pydantic.Field(alias="stringifiedValue")

    class Partial(typing_extensions.TypedDict):
        stringified_type: typing_extensions.NotRequired[typing.Optional[str]]
        stringified_value: typing_extensions.NotRequired[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
