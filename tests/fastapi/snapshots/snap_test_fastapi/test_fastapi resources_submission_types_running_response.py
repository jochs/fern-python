# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .running_submission_state import RunningSubmissionState
from .submission_id import SubmissionId


class RunningResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    state: RunningSubmissionState

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        state: typing_extensions.NotRequired[RunningSubmissionState]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RunningResponse.Validators.root
            def validate(values: RunningResponse.Partial) -> RunningResponse.Partial:
                ...

            @RunningResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: RunningResponse.Partial) -> SubmissionId:
                ...

            @RunningResponse.Validators.field("state")
            def validate_state(state: RunningSubmissionState, values: RunningResponse.Partial) -> RunningSubmissionState:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[RunningResponse.Partial], RunningResponse.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[typing.List[RunningResponse.Validators.SubmissionIdValidator]] = []
        _state_validators: typing.ClassVar[typing.List[RunningResponse.Validators.StateValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[RunningResponse.Partial], RunningResponse.Partial]
        ) -> typing.Callable[[RunningResponse.Partial], RunningResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [RunningResponse.Validators.SubmissionIdValidator], RunningResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["state"]
        ) -> typing.Callable[[RunningResponse.Validators.StateValidator], RunningResponse.Validators.StateValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "state":
                    cls._state_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: RunningResponse.Partial) -> SubmissionId:
                ...

        class StateValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: RunningSubmissionState, __values: RunningResponse.Partial
            ) -> RunningSubmissionState:
                ...

    @pydantic.root_validator
    def _validate(cls, values: RunningResponse.Partial) -> RunningResponse.Partial:
        for validator in RunningResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: RunningResponse.Partial) -> SubmissionId:
        for validator in RunningResponse.Validators._submission_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("state")
    def _validate_state(cls, v: RunningSubmissionState, values: RunningResponse.Partial) -> RunningSubmissionState:
        for validator in RunningResponse.Validators._state_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
