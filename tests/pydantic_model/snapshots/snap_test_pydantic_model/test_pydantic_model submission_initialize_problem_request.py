# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.problem_id import ProblemId


class InitializeProblemRequest(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_version: typing.Optional[int] = pydantic.Field(alias="problemVersion")

    class Partial(typing_extensions.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_version: typing_extensions.NotRequired[typing.Optional[int]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @InitializeProblemRequest.Validators.root
            def validate(values: InitializeProblemRequest.Partial) -> InitializeProblemRequest.Partial:
                ...

            @InitializeProblemRequest.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: InitializeProblemRequest.Partial) -> ProblemId:
                ...

            @InitializeProblemRequest.Validators.field("problem_version")
            def validate_problem_version(problem_version: typing.Optional[int], values: InitializeProblemRequest.Partial) -> typing.Optional[int]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[InitializeProblemRequest.Partial], InitializeProblemRequest.Partial]]
        ] = []
        _problem_id_validators: typing.ClassVar[
            typing.List[InitializeProblemRequest.Validators.ProblemIdValidator]
        ] = []
        _problem_version_validators: typing.ClassVar[
            typing.List[InitializeProblemRequest.Validators.ProblemVersionValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[InitializeProblemRequest.Partial], InitializeProblemRequest.Partial]
        ) -> typing.Callable[[InitializeProblemRequest.Partial], InitializeProblemRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators.ProblemIdValidator],
            InitializeProblemRequest.Validators.ProblemIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"]
        ) -> typing.Callable[
            [InitializeProblemRequest.Validators.ProblemVersionValidator],
            InitializeProblemRequest.Validators.ProblemVersionValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                if field_name == "problem_version":
                    cls._problem_version_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, problem_id: ProblemId, *, values: InitializeProblemRequest.Partial) -> ProblemId:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(
                self, problem_version: typing.Optional[int], *, values: InitializeProblemRequest.Partial
            ) -> typing.Optional[int]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: InitializeProblemRequest.Partial) -> InitializeProblemRequest.Partial:
        for validator in InitializeProblemRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, problem_id: ProblemId, values: InitializeProblemRequest.Partial) -> ProblemId:
        for validator in InitializeProblemRequest.Validators._problem_id_validators:
            problem_id = validator(problem_id, values=values)
        return problem_id

    @pydantic.validator("problem_version")
    def _validate_problem_version(
        cls, problem_version: typing.Optional[int], values: InitializeProblemRequest.Partial
    ) -> typing.Optional[int]:
        for validator in InitializeProblemRequest.Validators._problem_version_validators:
            problem_version = validator(problem_version, values=values)
        return problem_version

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
