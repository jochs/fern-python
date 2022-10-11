from __future__ import annotations

import typing

import pydantic
import typing_extensions


class DebugKeyValuePairs(pydantic.BaseModel):
    key: DebugVariableValue
    value: DebugVariableValue

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("key")
    def _validate_key(cls, key: DebugVariableValue) -> DebugVariableValue:
        for validator in DebugKeyValuePairs.Validators._key_validators:
            key = validator(key)
        return key

    @pydantic.validator("value")
    def _validate_value(cls, value: DebugVariableValue) -> DebugVariableValue:
        for validator in DebugKeyValuePairs.Validators._value_validators:
            value = validator(value)
        return value

    class Validators:
        _key_validators: typing.ClassVar[typing.List[typing.Callable[[DebugVariableValue], DebugVariableValue]]] = []
        _value_validators: typing.ClassVar[typing.List[typing.Callable[[DebugVariableValue], DebugVariableValue]]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["key"]
        ) -> typing.Callable[
            [typing.Callable[[DebugVariableValue], DebugVariableValue]],
            typing.Callable[[DebugVariableValue], DebugVariableValue],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value"]
        ) -> typing.Callable[
            [typing.Callable[[DebugVariableValue], DebugVariableValue]],
            typing.Callable[[DebugVariableValue], DebugVariableValue],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "key":
                    cls._key_validators.append(validator)
                elif field_name == "value":
                    cls._value_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on DebugKeyValuePairs: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True


from .debug_variable_value import DebugVariableValue  # noqa: E402

DebugKeyValuePairs.update_forward_refs()
