# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .invalid_request_cause import InvalidRequestCause
from .submission_request import SubmissionRequest


class InvalidRequestResponse(pydantic.BaseModel):
    request: SubmissionRequest
    cause: InvalidRequestCause

    class Partial(typing_extensions.TypedDict):
        request: typing_extensions.NotRequired[SubmissionRequest]
        cause: typing_extensions.NotRequired[InvalidRequestCause]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @InvalidRequestResponse.Validators.root()
            def validate(values: InvalidRequestResponse.Partial) -> InvalidRequestResponse.Partial:
                ...

            @InvalidRequestResponse.Validators.field("request")
            def validate_request(request: SubmissionRequest, values: InvalidRequestResponse.Partial) -> SubmissionRequest:
                ...

            @InvalidRequestResponse.Validators.field("cause")
            def validate_cause(cause: InvalidRequestCause, values: InvalidRequestResponse.Partial) -> InvalidRequestCause:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[InvalidRequestResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[InvalidRequestResponse.Validators._RootValidator]] = []
        _request_pre_validators: typing.ClassVar[
            typing.List[InvalidRequestResponse.Validators.PreRequestValidator]
        ] = []
        _request_post_validators: typing.ClassVar[typing.List[InvalidRequestResponse.Validators.RequestValidator]] = []
        _cause_pre_validators: typing.ClassVar[typing.List[InvalidRequestResponse.Validators.PreCauseValidator]] = []
        _cause_post_validators: typing.ClassVar[typing.List[InvalidRequestResponse.Validators.CauseValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators._RootValidator], InvalidRequestResponse.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators._PreRootValidator], InvalidRequestResponse.Validators._PreRootValidator
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
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
            cls, field_name: typing_extensions.Literal["request"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators.PreRequestValidator],
            InvalidRequestResponse.Validators.PreRequestValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["request"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators.RequestValidator], InvalidRequestResponse.Validators.RequestValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["cause"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators.PreCauseValidator], InvalidRequestResponse.Validators.PreCauseValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["cause"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [InvalidRequestResponse.Validators.CauseValidator], InvalidRequestResponse.Validators.CauseValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "request":
                    if pre:
                        cls._request_pre_validators.append(validator)
                    else:
                        cls._request_post_validators.append(validator)
                if field_name == "cause":
                    if pre:
                        cls._cause_pre_validators.append(validator)
                    else:
                        cls._cause_post_validators.append(validator)
                return validator

            return decorator

        class PreRequestValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: InvalidRequestResponse.Partial) -> typing.Any:
                ...

        class RequestValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionRequest, __values: InvalidRequestResponse.Partial) -> SubmissionRequest:
                ...

        class PreCauseValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: InvalidRequestResponse.Partial) -> typing.Any:
                ...

        class CauseValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: InvalidRequestCause, __values: InvalidRequestResponse.Partial
            ) -> InvalidRequestCause:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: InvalidRequestResponse.Partial) -> InvalidRequestResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: InvalidRequestResponse.Partial) -> InvalidRequestResponse.Partial:
        for validator in InvalidRequestResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: InvalidRequestResponse.Partial) -> InvalidRequestResponse.Partial:
        for validator in InvalidRequestResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("request", pre=True)
    def _pre_validate_request(cls, v: SubmissionRequest, values: InvalidRequestResponse.Partial) -> SubmissionRequest:
        for validator in InvalidRequestResponse.Validators._request_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("request", pre=False)
    def _post_validate_request(cls, v: SubmissionRequest, values: InvalidRequestResponse.Partial) -> SubmissionRequest:
        for validator in InvalidRequestResponse.Validators._request_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("cause", pre=True)
    def _pre_validate_cause(cls, v: InvalidRequestCause, values: InvalidRequestResponse.Partial) -> InvalidRequestCause:
        for validator in InvalidRequestResponse.Validators._cause_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("cause", pre=False)
    def _post_validate_cause(
        cls, v: InvalidRequestCause, values: InvalidRequestResponse.Partial
    ) -> InvalidRequestCause:
        for validator in InvalidRequestResponse.Validators._cause_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
