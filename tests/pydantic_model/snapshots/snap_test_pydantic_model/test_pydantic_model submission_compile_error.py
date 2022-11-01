# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class CompileError(pydantic.BaseModel):
    message: str

    class Partial(typing_extensions.TypedDict):
        message: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CompileError.Validators.root
            def validate(values: CompileError.Partial) -> CompileError.Partial:
                ...

            @CompileError.Validators.field("message")
            def validate_message(message: str, values: CompileError.Partial) -> str:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[CompileError.Partial], CompileError.Partial]]] = []
        _message_validators: typing.ClassVar[typing.List[CompileError.Validators.MessageValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[CompileError.Partial], CompileError.Partial]
        ) -> typing.Callable[[CompileError.Partial], CompileError.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["message"]
        ) -> typing.Callable[[CompileError.Validators.MessageValidator], CompileError.Validators.MessageValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "message":
                    cls._message_validators.append(validator)
                return validator

            return decorator

        class MessageValidator(typing_extensions.Protocol):
            def __call__(self, message: str, *, values: CompileError.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: CompileError.Partial) -> CompileError.Partial:
        for validator in CompileError.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("message")
    def _validate_message(cls, message: str, values: CompileError.Partial) -> str:
        for validator in CompileError.Validators._message_validators:
            message = validator(message, values=values)
        return message

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
