# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.problem_id import ProblemId
from ..v_2.problem.problem_info_v_2 import ProblemInfoV2
from .test_submission_update import TestSubmissionUpdate


class TestSubmissionStatusV2(pydantic.BaseModel):
    updates: typing.List[TestSubmissionUpdate]
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_version: int = pydantic.Field(alias="problemVersion")
    problem_info: ProblemInfoV2 = pydantic.Field(alias="problemInfo")

    class Partial(typing_extensions.TypedDict):
        updates: typing_extensions.NotRequired[typing.List[TestSubmissionUpdate]]
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_version: typing_extensions.NotRequired[int]
        problem_info: typing_extensions.NotRequired[ProblemInfoV2]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestSubmissionStatusV2.Validators.root
            def validate(values: TestSubmissionStatusV2.Partial) -> TestSubmissionStatusV2.Partial:
                ...

            @TestSubmissionStatusV2.Validators.field("updates")
            def validate_updates(updates: typing.List[TestSubmissionUpdate], values: TestSubmissionStatusV2.Partial) -> typing.List[TestSubmissionUpdate]:
                ...

            @TestSubmissionStatusV2.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: TestSubmissionStatusV2.Partial) -> ProblemId:
                ...

            @TestSubmissionStatusV2.Validators.field("problem_version")
            def validate_problem_version(problem_version: int, values: TestSubmissionStatusV2.Partial) -> int:
                ...

            @TestSubmissionStatusV2.Validators.field("problem_info")
            def validate_problem_info(problem_info: ProblemInfoV2, values: TestSubmissionStatusV2.Partial) -> ProblemInfoV2:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TestSubmissionStatusV2.Partial], TestSubmissionStatusV2.Partial]]
        ] = []
        _updates_validators: typing.ClassVar[typing.List[TestSubmissionStatusV2.Validators.UpdatesValidator]] = []
        _problem_id_validators: typing.ClassVar[typing.List[TestSubmissionStatusV2.Validators.ProblemIdValidator]] = []
        _problem_version_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemVersionValidator]
        ] = []
        _problem_info_validators: typing.ClassVar[
            typing.List[TestSubmissionStatusV2.Validators.ProblemInfoValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestSubmissionStatusV2.Partial], TestSubmissionStatusV2.Partial]
        ) -> typing.Callable[[TestSubmissionStatusV2.Partial], TestSubmissionStatusV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["updates"]
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.UpdatesValidator], TestSubmissionStatusV2.Validators.UpdatesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.ProblemIdValidator], TestSubmissionStatusV2.Validators.ProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"]
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.ProblemVersionValidator],
            TestSubmissionStatusV2.Validators.ProblemVersionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_info"]
        ) -> typing.Callable[
            [TestSubmissionStatusV2.Validators.ProblemInfoValidator],
            TestSubmissionStatusV2.Validators.ProblemInfoValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "updates":
                    cls._updates_validators.append(validator)
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                if field_name == "problem_version":
                    cls._problem_version_validators.append(validator)
                if field_name == "problem_info":
                    cls._problem_info_validators.append(validator)
                return validator

            return decorator

        class UpdatesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestSubmissionUpdate], __values: TestSubmissionStatusV2.Partial
            ) -> typing.List[TestSubmissionUpdate]:
                ...

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: TestSubmissionStatusV2.Partial) -> ProblemId:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: TestSubmissionStatusV2.Partial) -> int:
                ...

        class ProblemInfoValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemInfoV2, __values: TestSubmissionStatusV2.Partial) -> ProblemInfoV2:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestSubmissionStatusV2.Partial) -> TestSubmissionStatusV2.Partial:
        for validator in TestSubmissionStatusV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("updates")
    def _validate_updates(
        cls, v: typing.List[TestSubmissionUpdate], values: TestSubmissionStatusV2.Partial
    ) -> typing.List[TestSubmissionUpdate]:
        for validator in TestSubmissionStatusV2.Validators._updates_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, v: ProblemId, values: TestSubmissionStatusV2.Partial) -> ProblemId:
        for validator in TestSubmissionStatusV2.Validators._problem_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version")
    def _validate_problem_version(cls, v: int, values: TestSubmissionStatusV2.Partial) -> int:
        for validator in TestSubmissionStatusV2.Validators._problem_version_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_info")
    def _validate_problem_info(cls, v: ProblemInfoV2, values: TestSubmissionStatusV2.Partial) -> ProblemInfoV2:
        for validator in TestSubmissionStatusV2.Validators._problem_info_validators:
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
