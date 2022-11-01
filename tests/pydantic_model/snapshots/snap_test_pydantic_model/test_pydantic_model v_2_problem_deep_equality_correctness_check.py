# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .parameter_id import ParameterId


class DeepEqualityCorrectnessCheck(pydantic.BaseModel):
    expected_value_parameter_id: ParameterId = pydantic.Field(alias="expectedValueParameterId")

    class Partial(typing_extensions.TypedDict):
        expected_value_parameter_id: typing_extensions.NotRequired[ParameterId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DeepEqualityCorrectnessCheck.Validators.root
            def validate(values: DeepEqualityCorrectnessCheck.Partial) -> DeepEqualityCorrectnessCheck.Partial:
                ...

            @DeepEqualityCorrectnessCheck.Validators.field("expected_value_parameter_id")
            def validate_expected_value_parameter_id(expected_value_parameter_id: ParameterId, values: DeepEqualityCorrectnessCheck.Partial) -> ParameterId:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[DeepEqualityCorrectnessCheck.Partial], DeepEqualityCorrectnessCheck.Partial]]
        ] = []
        _expected_value_parameter_id_validators: typing.ClassVar[
            typing.List[DeepEqualityCorrectnessCheck.Validators.ExpectedValueParameterIdValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[[DeepEqualityCorrectnessCheck.Partial], DeepEqualityCorrectnessCheck.Partial],
        ) -> typing.Callable[[DeepEqualityCorrectnessCheck.Partial], DeepEqualityCorrectnessCheck.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_value_parameter_id"]
        ) -> typing.Callable[
            [DeepEqualityCorrectnessCheck.Validators.ExpectedValueParameterIdValidator],
            DeepEqualityCorrectnessCheck.Validators.ExpectedValueParameterIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "expected_value_parameter_id":
                    cls._expected_value_parameter_id_validators.append(validator)
                return validator

            return decorator

        class ExpectedValueParameterIdValidator(typing_extensions.Protocol):
            def __call__(
                self, expected_value_parameter_id: ParameterId, *, values: DeepEqualityCorrectnessCheck.Partial
            ) -> ParameterId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: DeepEqualityCorrectnessCheck.Partial) -> DeepEqualityCorrectnessCheck.Partial:
        for validator in DeepEqualityCorrectnessCheck.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("expected_value_parameter_id")
    def _validate_expected_value_parameter_id(
        cls, expected_value_parameter_id: ParameterId, values: DeepEqualityCorrectnessCheck.Partial
    ) -> ParameterId:
        for validator in DeepEqualityCorrectnessCheck.Validators._expected_value_parameter_id_validators:
            expected_value_parameter_id = validator(expected_value_parameter_id, values=values)
        return expected_value_parameter_id

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
