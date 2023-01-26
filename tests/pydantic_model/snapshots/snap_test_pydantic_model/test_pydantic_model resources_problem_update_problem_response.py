# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class UpdateProblemResponse(pydantic.BaseModel):
    problem_version: int = pydantic.Field(alias="problemVersion")

    class Partial(typing_extensions.TypedDict):
        problem_version: typing_extensions.NotRequired[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @UpdateProblemResponse.Validators.root()
            def validate(values: UpdateProblemResponse.Partial) -> UpdateProblemResponse.Partial:
                ...

            @UpdateProblemResponse.Validators.field("problem_version")
            def validate_problem_version(problem_version: int, values: UpdateProblemResponse.Partial) -> int:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[UpdateProblemResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[UpdateProblemResponse.Validators._RootValidator]] = []
        _problem_version_pre_validators: typing.ClassVar[
            typing.List[UpdateProblemResponse.Validators.PreProblemVersionValidator]
        ] = []
        _problem_version_post_validators: typing.ClassVar[
            typing.List[UpdateProblemResponse.Validators.ProblemVersionValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [UpdateProblemResponse.Validators._RootValidator], UpdateProblemResponse.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [UpdateProblemResponse.Validators._PreRootValidator], UpdateProblemResponse.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["problem_version"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [UpdateProblemResponse.Validators.PreProblemVersionValidator],
            UpdateProblemResponse.Validators.PreProblemVersionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["problem_version"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [UpdateProblemResponse.Validators.ProblemVersionValidator],
            UpdateProblemResponse.Validators.ProblemVersionValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_version":
                    if pre:
                        cls._problem_version_pre_validators.append(validator)
                    else:
                        cls._problem_version_post_validators.append(validator)
                return validator

            return decorator

        class PreProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: UpdateProblemResponse.Partial) -> typing.Any:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: UpdateProblemResponse.Partial) -> int:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: UpdateProblemResponse.Partial) -> UpdateProblemResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: UpdateProblemResponse.Partial) -> UpdateProblemResponse.Partial:
        for validator in UpdateProblemResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: UpdateProblemResponse.Partial) -> UpdateProblemResponse.Partial:
        for validator in UpdateProblemResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_version", pre=True)
    def _pre_validate_problem_version(cls, v: int, values: UpdateProblemResponse.Partial) -> int:
        for validator in UpdateProblemResponse.Validators._problem_version_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=False)
    def _post_validate_problem_version(cls, v: int, values: UpdateProblemResponse.Partial) -> int:
        for validator in UpdateProblemResponse.Validators._problem_version_post_validators:
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
