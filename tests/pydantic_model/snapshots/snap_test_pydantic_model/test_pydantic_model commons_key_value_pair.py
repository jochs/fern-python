# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class KeyValuePair(pydantic.BaseModel):
    key: VariableValue
    value: VariableValue

    class Partial(typing_extensions.TypedDict):
        key: typing_extensions.NotRequired[VariableValue]
        value: typing_extensions.NotRequired[VariableValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @KeyValuePair.Validators.root
            def validate(values: KeyValuePair.Partial) -> KeyValuePair.Partial:
                ...

            @KeyValuePair.Validators.field("key")
            def validate_key(key: VariableValue, values: KeyValuePair.Partial) -> VariableValue:
                ...

            @KeyValuePair.Validators.field("value")
            def validate_value(value: VariableValue, values: KeyValuePair.Partial) -> VariableValue:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[KeyValuePair.Partial], KeyValuePair.Partial]]] = []
        _key_pre_validators: typing.ClassVar[typing.List[KeyValuePair.Validators.KeyValidator]] = []
        _key_post_validators: typing.ClassVar[typing.List[KeyValuePair.Validators.KeyValidator]] = []
        _value_pre_validators: typing.ClassVar[typing.List[KeyValuePair.Validators.ValueValidator]] = []
        _value_post_validators: typing.ClassVar[typing.List[KeyValuePair.Validators.ValueValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[KeyValuePair.Partial], KeyValuePair.Partial]
        ) -> typing.Callable[[KeyValuePair.Partial], KeyValuePair.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["key"]
        ) -> typing.Callable[[KeyValuePair.Validators.KeyValidator], KeyValuePair.Validators.KeyValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value"]
        ) -> typing.Callable[[KeyValuePair.Validators.ValueValidator], KeyValuePair.Validators.ValueValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "key":
                    if pre:
                        cls._key_post_validators.append(validator)
                    else:
                        cls._key_post_validators.append(validator)
                if field_name == "value":
                    if pre:
                        cls._value_post_validators.append(validator)
                    else:
                        cls._value_post_validators.append(validator)
                return validator

            return decorator

        class KeyValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableValue, __values: KeyValuePair.Partial) -> VariableValue:
                ...

        class ValueValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableValue, __values: KeyValuePair.Partial) -> VariableValue:
                ...

    @pydantic.root_validator
    def _validate(cls, values: KeyValuePair.Partial) -> KeyValuePair.Partial:
        for validator in KeyValuePair.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("key", pre=True)
    def _pre_validate_key(cls, v: VariableValue, values: KeyValuePair.Partial) -> VariableValue:
        for validator in KeyValuePair.Validators._key_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("key", pre=False)
    def _post_validate_key(cls, v: VariableValue, values: KeyValuePair.Partial) -> VariableValue:
        for validator in KeyValuePair.Validators._key_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value", pre=True)
    def _pre_validate_value(cls, v: VariableValue, values: KeyValuePair.Partial) -> VariableValue:
        for validator in KeyValuePair.Validators._value_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value", pre=False)
    def _post_validate_value(cls, v: VariableValue, values: KeyValuePair.Partial) -> VariableValue:
        for validator in KeyValuePair.Validators._value_post_validators:
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


from .variable_value import VariableValue  # noqa: E402

KeyValuePair.update_forward_refs()
