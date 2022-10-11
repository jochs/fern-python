import typing

import pydantic
import typing_extensions

from .invalid_request_cause import InvalidRequestCause
from .submission_request import SubmissionRequest


class InvalidRequestResponse(pydantic.BaseModel):
    request: SubmissionRequest
    cause: InvalidRequestCause

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("request")
    def _validate_request(cls, request: SubmissionRequest) -> SubmissionRequest:
        for validator in InvalidRequestResponse.Validators._request_validators:
            request = validator(request)
        return request

    @pydantic.validator("cause")
    def _validate_cause(cls, cause: InvalidRequestCause) -> InvalidRequestCause:
        for validator in InvalidRequestResponse.Validators._cause_validators:
            cause = validator(cause)
        return cause

    class Validators:
        _request_validators: typing.ClassVar[typing.List[typing.Callable[[SubmissionRequest], SubmissionRequest]]] = []
        _cause_validators: typing.ClassVar[
            typing.List[typing.Callable[[InvalidRequestCause], InvalidRequestCause]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["request"]
        ) -> typing.Callable[
            [typing.Callable[[SubmissionRequest], SubmissionRequest]],
            typing.Callable[[SubmissionRequest], SubmissionRequest],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["cause"]
        ) -> typing.Callable[
            [typing.Callable[[InvalidRequestCause], InvalidRequestCause]],
            typing.Callable[[InvalidRequestCause], InvalidRequestCause],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "request":
                    cls._request_validators.append(validator)
                elif field_name == "cause":
                    cls._cause_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on InvalidRequestResponse: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
