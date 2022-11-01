# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.language import Language


class UnexpectedLanguageError(pydantic.BaseModel):
    expected_language: Language = pydantic.Field(alias="expectedLanguage")
    actual_language: Language = pydantic.Field(alias="actualLanguage")

    class Partial(typing_extensions.TypedDict):
        expected_language: typing_extensions.NotRequired[Language]
        actual_language: typing_extensions.NotRequired[Language]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @UnexpectedLanguageError.Validators.root
            def validate(values: UnexpectedLanguageError.Partial) -> UnexpectedLanguageError.Partial:
                ...

            @UnexpectedLanguageError.Validators.field("expected_language")
            def validate_expected_language(expected_language: Language, values: UnexpectedLanguageError.Partial) -> Language:
                ...

            @UnexpectedLanguageError.Validators.field("actual_language")
            def validate_actual_language(actual_language: Language, values: UnexpectedLanguageError.Partial) -> Language:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[UnexpectedLanguageError.Partial], UnexpectedLanguageError.Partial]]
        ] = []
        _expected_language_validators: typing.ClassVar[
            typing.List[UnexpectedLanguageError.Validators.ExpectedLanguageValidator]
        ] = []
        _actual_language_validators: typing.ClassVar[
            typing.List[UnexpectedLanguageError.Validators.ActualLanguageValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[UnexpectedLanguageError.Partial], UnexpectedLanguageError.Partial]
        ) -> typing.Callable[[UnexpectedLanguageError.Partial], UnexpectedLanguageError.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_language"]
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators.ExpectedLanguageValidator],
            UnexpectedLanguageError.Validators.ExpectedLanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_language"]
        ) -> typing.Callable[
            [UnexpectedLanguageError.Validators.ActualLanguageValidator],
            UnexpectedLanguageError.Validators.ActualLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "expected_language":
                    cls._expected_language_validators.append(validator)
                if field_name == "actual_language":
                    cls._actual_language_validators.append(validator)
                return validator

            return decorator

        class ExpectedLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: UnexpectedLanguageError.Partial) -> Language:
                ...

        class ActualLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: UnexpectedLanguageError.Partial) -> Language:
                ...

    @pydantic.root_validator
    def _validate(cls, values: UnexpectedLanguageError.Partial) -> UnexpectedLanguageError.Partial:
        for validator in UnexpectedLanguageError.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("expected_language")
    def _validate_expected_language(cls, v: Language, values: UnexpectedLanguageError.Partial) -> Language:
        for validator in UnexpectedLanguageError.Validators._expected_language_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_language")
    def _validate_actual_language(cls, v: Language, values: UnexpectedLanguageError.Partial) -> Language:
        for validator in UnexpectedLanguageError.Validators._actual_language_validators:
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
