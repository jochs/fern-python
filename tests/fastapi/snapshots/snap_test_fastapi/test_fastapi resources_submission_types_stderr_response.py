# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class StderrResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    stderr: str

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        stderr: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StderrResponse.Validators.root
            def validate(values: StderrResponse.Partial) -> StderrResponse.Partial:
                ...

            @StderrResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: StderrResponse.Partial) -> SubmissionId:
                ...

            @StderrResponse.Validators.field("stderr")
            def validate_stderr(stderr: str, values: StderrResponse.Partial) -> str:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[StderrResponse.Partial], StderrResponse.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[typing.List[StderrResponse.Validators.SubmissionIdValidator]] = []
        _stderr_validators: typing.ClassVar[typing.List[StderrResponse.Validators.StderrValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[StderrResponse.Partial], StderrResponse.Partial]
        ) -> typing.Callable[[StderrResponse.Partial], StderrResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [StderrResponse.Validators.SubmissionIdValidator], StderrResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stderr"]
        ) -> typing.Callable[[StderrResponse.Validators.StderrValidator], StderrResponse.Validators.StderrValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "stderr":
                    cls._stderr_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, submission_id: SubmissionId, *, values: StderrResponse.Partial) -> SubmissionId:
                ...

        class StderrValidator(typing_extensions.Protocol):
            def __call__(self, stderr: str, *, values: StderrResponse.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: StderrResponse.Partial) -> StderrResponse.Partial:
        for validator in StderrResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, submission_id: SubmissionId, values: StderrResponse.Partial) -> SubmissionId:
        for validator in StderrResponse.Validators._submission_id_validators:
            submission_id = validator(submission_id, values=values)
        return submission_id

    @pydantic.validator("stderr")
    def _validate_stderr(cls, stderr: str, values: StderrResponse.Partial) -> str:
        for validator in StderrResponse.Validators._stderr_validators:
            stderr = validator(stderr, values=values)
        return stderr

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
