# This file was auto-generated by Fern from our API Definition.

# type: ignore
# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.problem_id import ProblemId
from ...commons.variable_type import VariableType


class LightweightProblemInfoV2(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_name: str = pydantic.Field(alias="problemName")
    problem_version: int = pydantic.Field(alias="problemVersion")
    variable_types: typing.List[VariableType] = pydantic.Field(alias="variableTypes")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @LightweightProblemInfoV2.Validators.field("problem_id")
            def validate_problem_id(v: ProblemId, values: LightweightProblemInfoV2.Partial) -> ProblemId:
                ...

            @LightweightProblemInfoV2.Validators.field("problem_name")
            def validate_problem_name(v: str, values: LightweightProblemInfoV2.Partial) -> str:
                ...

            @LightweightProblemInfoV2.Validators.field("problem_version")
            def validate_problem_version(v: int, values: LightweightProblemInfoV2.Partial) -> int:
                ...

            @LightweightProblemInfoV2.Validators.field("variable_types")
            def validate_variable_types(v: typing.List[VariableType], values: LightweightProblemInfoV2.Partial) -> typing.List[VariableType]:
                ...
        """

        _problem_id_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemIdValidator]
        ] = []
        _problem_name_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemNameValidator]
        ] = []
        _problem_version_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemVersionValidator]
        ] = []
        _variable_types_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.VariableTypesValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.ProblemIdValidator],
            LightweightProblemInfoV2.Validators.ProblemIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"]
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.ProblemNameValidator],
            LightweightProblemInfoV2.Validators.ProblemNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"]
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.ProblemVersionValidator],
            LightweightProblemInfoV2.Validators.ProblemVersionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variable_types"]
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.VariableTypesValidator],
            LightweightProblemInfoV2.Validators.VariableTypesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                if field_name == "problem_name":
                    cls._problem_name_validators.append(validator)
                if field_name == "problem_version":
                    cls._problem_version_validators.append(validator)
                if field_name == "variable_types":
                    cls._variable_types_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, v: ProblemId, *, values: LightweightProblemInfoV2.Partial) -> ProblemId:
                ...

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: LightweightProblemInfoV2.Partial) -> str:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, v: int, *, values: LightweightProblemInfoV2.Partial) -> int:
                ...

        class VariableTypesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[VariableType], *, values: LightweightProblemInfoV2.Partial
            ) -> typing.List[VariableType]:
                ...

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, v: ProblemId, values: ProblemId) -> ProblemId:
        for validator in LightweightProblemInfoV2.Validators._problem_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_name")
    def _validate_problem_name(cls, v: str, values: str) -> str:
        for validator in LightweightProblemInfoV2.Validators._problem_name_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("problem_version")
    def _validate_problem_version(cls, v: int, values: int) -> int:
        for validator in LightweightProblemInfoV2.Validators._problem_version_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("variable_types")
    def _validate_variable_types(
        cls, v: typing.List[VariableType], values: typing.List[VariableType]
    ) -> typing.List[VariableType]:
        for validator in LightweightProblemInfoV2.Validators._variable_types_validators:
            v = validator(v, values=values)
        return v

    class Partial(typing.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_name: typing_extensions.NotRequired[str]
        problem_version: typing_extensions.NotRequired[int]
        variable_types: typing_extensions.NotRequired[typing.List[VariableType]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True