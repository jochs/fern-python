# This file was auto-generated by Fern from our API Definition.

# type: ignore
# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.variable_type import VariableType
from .parameter import Parameter


class NonVoidFunctionSignature(pydantic.BaseModel):
    parameters: typing.List[Parameter]
    return_type: VariableType = pydantic.Field(alias="returnType")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @NonVoidFunctionSignature.Validators.field("parameters")
            def validate_parameters(v: typing.List[Parameter], values: NonVoidFunctionSignature.Partial) -> typing.List[Parameter]:
                ...

            @NonVoidFunctionSignature.Validators.field("return_type")
            def validate_return_type(v: VariableType, values: NonVoidFunctionSignature.Partial) -> VariableType:
                ...
        """

        _parameters_validators: typing.ClassVar[
            typing.List[NonVoidFunctionSignature.Validators.ParametersValidator]
        ] = []
        _return_type_validators: typing.ClassVar[
            typing.List[NonVoidFunctionSignature.Validators.ReturnTypeValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["parameters"]
        ) -> typing.Callable[
            [NonVoidFunctionSignature.Validators.ParametersValidator],
            NonVoidFunctionSignature.Validators.ParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["return_type"]
        ) -> typing.Callable[
            [NonVoidFunctionSignature.Validators.ReturnTypeValidator],
            NonVoidFunctionSignature.Validators.ReturnTypeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameters":
                    cls._parameters_validators.append(validator)
                if field_name == "return_type":
                    cls._return_type_validators.append(validator)
                return validator

            return decorator

        class ParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[Parameter], *, values: NonVoidFunctionSignature.Partial
            ) -> typing.List[Parameter]:
                ...

        class ReturnTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: NonVoidFunctionSignature.Partial) -> VariableType:
                ...

    @pydantic.validator("parameters")
    def _validate_parameters(cls, v: typing.List[Parameter], values: typing.List[Parameter]) -> typing.List[Parameter]:
        for validator in NonVoidFunctionSignature.Validators._parameters_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("return_type")
    def _validate_return_type(cls, v: VariableType, values: VariableType) -> VariableType:
        for validator in NonVoidFunctionSignature.Validators._return_type_validators:
            v = validator(v, values=values)
        return v

    class Partial(typing.TypedDict):
        parameters: typing_extensions.NotRequired[typing.List[Parameter]]
        return_type: typing_extensions.NotRequired[VariableType]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True