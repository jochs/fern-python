# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ........core.datetime_utils import serialize_datetime
from .test_case_id import TestCaseId


class TestCaseMetadata(pydantic.BaseModel):
    id: TestCaseId
    name: str
    hidden: bool

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[TestCaseId]
        name: typing_extensions.NotRequired[str]
        hidden: typing_extensions.NotRequired[bool]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
