# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class RecordedResponseNotification(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")
    test_case_id: typing.Optional[str] = pydantic.Field(alias="testCaseId")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        trace_responses_size: typing_extensions.NotRequired[int]
        test_case_id: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @RecordedResponseNotification.Validators.root
            def validate(values: RecordedResponseNotification.Partial) -> RecordedResponseNotification.Partial:
                ...

            @RecordedResponseNotification.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: RecordedResponseNotification.Partial) -> SubmissionId:
                ...

            @RecordedResponseNotification.Validators.field("trace_responses_size")
            def validate_trace_responses_size(trace_responses_size: int, values: RecordedResponseNotification.Partial) -> int:
                ...

            @RecordedResponseNotification.Validators.field("test_case_id")
            def validate_test_case_id(test_case_id: typing.Optional[str], values: RecordedResponseNotification.Partial) -> typing.Optional[str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[RecordedResponseNotification.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[RecordedResponseNotification.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[RecordedResponseNotification.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[RecordedResponseNotification.Validators.SubmissionIdValidator]
        ] = []
        _trace_responses_size_pre_validators: typing.ClassVar[
            typing.List[RecordedResponseNotification.Validators.TraceResponsesSizeValidator]
        ] = []
        _trace_responses_size_post_validators: typing.ClassVar[
            typing.List[RecordedResponseNotification.Validators.TraceResponsesSizeValidator]
        ] = []
        _test_case_id_pre_validators: typing.ClassVar[
            typing.List[RecordedResponseNotification.Validators.TestCaseIdValidator]
        ] = []
        _test_case_id_post_validators: typing.ClassVar[
            typing.List[RecordedResponseNotification.Validators.TestCaseIdValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> RecordedResponseNotification.Validators._RootValidator:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: bool = False
        ) -> typing.Callable[
            [RecordedResponseNotification.Validators.SubmissionIdValidator],
            RecordedResponseNotification.Validators.SubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses_size"], *, pre: bool = False
        ) -> typing.Callable[
            [RecordedResponseNotification.Validators.TraceResponsesSizeValidator],
            RecordedResponseNotification.Validators.TraceResponsesSizeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case_id"], *, pre: bool = False
        ) -> typing.Callable[
            [RecordedResponseNotification.Validators.TestCaseIdValidator],
            RecordedResponseNotification.Validators.TestCaseIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "trace_responses_size":
                    if pre:
                        cls._trace_responses_size_pre_validators.append(validator)
                    else:
                        cls._trace_responses_size_post_validators.append(validator)
                if field_name == "test_case_id":
                    if pre:
                        cls._test_case_id_pre_validators.append(validator)
                    else:
                        cls._test_case_id_post_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: RecordedResponseNotification.Partial) -> SubmissionId:
                ...

        class TraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: RecordedResponseNotification.Partial) -> int:
                ...

        class TestCaseIdValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[str], __values: RecordedResponseNotification.Partial
            ) -> typing.Optional[str]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: RecordedResponseNotification.Partial) -> RecordedResponseNotification.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: RecordedResponseNotification.Partial) -> RecordedResponseNotification.Partial:
        for validator in RecordedResponseNotification.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: RecordedResponseNotification.Partial) -> RecordedResponseNotification.Partial:
        for validator in RecordedResponseNotification.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: RecordedResponseNotification.Partial) -> SubmissionId:
        for validator in RecordedResponseNotification.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(
        cls, v: SubmissionId, values: RecordedResponseNotification.Partial
    ) -> SubmissionId:
        for validator in RecordedResponseNotification.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses_size", pre=True)
    def _pre_validate_trace_responses_size(cls, v: int, values: RecordedResponseNotification.Partial) -> int:
        for validator in RecordedResponseNotification.Validators._trace_responses_size_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses_size", pre=False)
    def _post_validate_trace_responses_size(cls, v: int, values: RecordedResponseNotification.Partial) -> int:
        for validator in RecordedResponseNotification.Validators._trace_responses_size_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case_id", pre=True)
    def _pre_validate_test_case_id(
        cls, v: typing.Optional[str], values: RecordedResponseNotification.Partial
    ) -> typing.Optional[str]:
        for validator in RecordedResponseNotification.Validators._test_case_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case_id", pre=False)
    def _post_validate_test_case_id(
        cls, v: typing.Optional[str], values: RecordedResponseNotification.Partial
    ) -> typing.Optional[str]:
        for validator in RecordedResponseNotification.Validators._test_case_id_post_validators:
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
