# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.problem_id import ProblemId
from ....commons.variable_type import VariableType


class LightweightProblemInfoV2(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_name: str = pydantic.Field(alias="problemName")
    problem_version: int = pydantic.Field(alias="problemVersion")
    variable_types: typing.List[VariableType] = pydantic.Field(alias="variableTypes")

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_name: typing_extensions.NotRequired[str]
        problem_version: typing_extensions.NotRequired[int]
        variable_types: typing_extensions.NotRequired[typing.List[VariableType]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @LightweightProblemInfoV2.Validators.root
            def validate(values: LightweightProblemInfoV2.Partial) -> LightweightProblemInfoV2.Partial:
                ...

            @LightweightProblemInfoV2.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: LightweightProblemInfoV2.Partial) -> ProblemId:
                ...

            @LightweightProblemInfoV2.Validators.field("problem_name")
            def validate_problem_name(problem_name: str, values: LightweightProblemInfoV2.Partial) -> str:
                ...

            @LightweightProblemInfoV2.Validators.field("problem_version")
            def validate_problem_version(problem_version: int, values: LightweightProblemInfoV2.Partial) -> int:
                ...

            @LightweightProblemInfoV2.Validators.field("variable_types")
            def validate_variable_types(variable_types: typing.List[VariableType], values: LightweightProblemInfoV2.Partial) -> typing.List[VariableType]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[LightweightProblemInfoV2.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[LightweightProblemInfoV2.Validators._RootValidator]] = []
        _problem_id_pre_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemIdValidator]
        ] = []
        _problem_id_post_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemIdValidator]
        ] = []
        _problem_name_pre_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemNameValidator]
        ] = []
        _problem_name_post_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemNameValidator]
        ] = []
        _problem_version_pre_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemVersionValidator]
        ] = []
        _problem_version_post_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.ProblemVersionValidator]
        ] = []
        _variable_types_pre_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.VariableTypesValidator]
        ] = []
        _variable_types_post_validators: typing.ClassVar[
            typing.List[LightweightProblemInfoV2.Validators.VariableTypesValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> LightweightProblemInfoV2.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: bool = False
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.ProblemIdValidator],
            LightweightProblemInfoV2.Validators.ProblemIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"], *, pre: bool = False
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.ProblemNameValidator],
            LightweightProblemInfoV2.Validators.ProblemNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"], *, pre: bool = False
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.ProblemVersionValidator],
            LightweightProblemInfoV2.Validators.ProblemVersionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variable_types"], *, pre: bool = False
        ) -> typing.Callable[
            [LightweightProblemInfoV2.Validators.VariableTypesValidator],
            LightweightProblemInfoV2.Validators.VariableTypesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    if pre:
                        cls._problem_id_pre_validators.append(validator)
                    else:
                        cls._problem_id_post_validators.append(validator)
                if field_name == "problem_name":
                    if pre:
                        cls._problem_name_pre_validators.append(validator)
                    else:
                        cls._problem_name_post_validators.append(validator)
                if field_name == "problem_version":
                    if pre:
                        cls._problem_version_pre_validators.append(validator)
                    else:
                        cls._problem_version_post_validators.append(validator)
                if field_name == "variable_types":
                    if pre:
                        cls._variable_types_pre_validators.append(validator)
                    else:
                        cls._variable_types_post_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: LightweightProblemInfoV2.Partial) -> ProblemId:
                ...

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: LightweightProblemInfoV2.Partial) -> str:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: LightweightProblemInfoV2.Partial) -> int:
                ...

        class VariableTypesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[VariableType], __values: LightweightProblemInfoV2.Partial
            ) -> typing.List[VariableType]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: LightweightProblemInfoV2.Partial) -> LightweightProblemInfoV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: LightweightProblemInfoV2.Partial) -> LightweightProblemInfoV2.Partial:
        for validator in LightweightProblemInfoV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: LightweightProblemInfoV2.Partial) -> LightweightProblemInfoV2.Partial:
        for validator in LightweightProblemInfoV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_id", pre=True)
    def _pre_validate_problem_id(cls, v: ProblemId, values: LightweightProblemInfoV2.Partial) -> ProblemId:
        for validator in LightweightProblemInfoV2.Validators._problem_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=False)
    def _post_validate_problem_id(cls, v: ProblemId, values: LightweightProblemInfoV2.Partial) -> ProblemId:
        for validator in LightweightProblemInfoV2.Validators._problem_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_name", pre=True)
    def _pre_validate_problem_name(cls, v: str, values: LightweightProblemInfoV2.Partial) -> str:
        for validator in LightweightProblemInfoV2.Validators._problem_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_name", pre=False)
    def _post_validate_problem_name(cls, v: str, values: LightweightProblemInfoV2.Partial) -> str:
        for validator in LightweightProblemInfoV2.Validators._problem_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=True)
    def _pre_validate_problem_version(cls, v: int, values: LightweightProblemInfoV2.Partial) -> int:
        for validator in LightweightProblemInfoV2.Validators._problem_version_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=False)
    def _post_validate_problem_version(cls, v: int, values: LightweightProblemInfoV2.Partial) -> int:
        for validator in LightweightProblemInfoV2.Validators._problem_version_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("variable_types", pre=True)
    def _pre_validate_variable_types(
        cls, v: typing.List[VariableType], values: LightweightProblemInfoV2.Partial
    ) -> typing.List[VariableType]:
        for validator in LightweightProblemInfoV2.Validators._variable_types_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("variable_types", pre=False)
    def _post_validate_variable_types(
        cls, v: typing.List[VariableType], values: LightweightProblemInfoV2.Partial
    ) -> typing.List[VariableType]:
        for validator in LightweightProblemInfoV2.Validators._variable_types_post_validators:
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
