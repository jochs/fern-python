# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing
import uuid

import pydantic

from ....core.datetime_utils import serialize_datetime


class SubmissionId(pydantic.BaseModel):
    __root__: uuid.UUID

    def get_as_uuid(self) -> uuid.UUID:
        return self.__root__

    @staticmethod
    def from_uuid(value: uuid.UUID) -> SubmissionId:
        return SubmissionId(__root__=value)

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionId.Validators.validate
            def validate(value: uuid.UUID) -> uuid.UUID:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[uuid.UUID], uuid.UUID]]] = []

        @classmethod
        def validate(cls, validator: typing.Callable[[uuid.UUID], uuid.UUID]) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(uuid.UUID, values.get("__root__"))
        for validator in SubmissionId.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
