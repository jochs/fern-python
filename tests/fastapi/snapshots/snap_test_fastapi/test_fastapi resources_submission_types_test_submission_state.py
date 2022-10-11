import typing

import pydantic
import typing_extensions

from ...commons.types.problem_id import ProblemId
from ...commons.types.test_case import TestCase
from .test_submission_status import TestSubmissionStatus


class TestSubmissionState(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    default_test_cases: typing.List[TestCase] = pydantic.Field(alias="defaultTestCases")
    custom_test_cases: typing.List[TestCase] = pydantic.Field(alias="customTestCases")
    status: TestSubmissionStatus

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, problem_id: ProblemId) -> ProblemId:
        for validator in TestSubmissionState.Validators._problem_id_validators:
            problem_id = validator(problem_id)
        return problem_id

    @pydantic.validator("default_test_cases")
    def _validate_default_test_cases(cls, default_test_cases: typing.List[TestCase]) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._default_test_cases_validators:
            default_test_cases = validator(default_test_cases)
        return default_test_cases

    @pydantic.validator("custom_test_cases")
    def _validate_custom_test_cases(cls, custom_test_cases: typing.List[TestCase]) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._custom_test_cases_validators:
            custom_test_cases = validator(custom_test_cases)
        return custom_test_cases

    @pydantic.validator("status")
    def _validate_status(cls, status: TestSubmissionStatus) -> TestSubmissionStatus:
        for validator in TestSubmissionState.Validators._status_validators:
            status = validator(status)
        return status

    class Validators:
        _problem_id_validators: typing.ClassVar[typing.List[typing.Callable[[ProblemId], ProblemId]]] = []
        _default_test_cases_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[TestCase]], typing.List[TestCase]]]
        ] = []
        _custom_test_cases_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[TestCase]], typing.List[TestCase]]]
        ] = []
        _status_validators: typing.ClassVar[
            typing.List[typing.Callable[[TestSubmissionStatus], TestSubmissionStatus]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[[typing.Callable[[ProblemId], ProblemId]], typing.Callable[[ProblemId], ProblemId]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["default_test_cases"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[TestCase]], typing.List[TestCase]]],
            typing.Callable[[typing.List[TestCase]], typing.List[TestCase]],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_test_cases"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[TestCase]], typing.List[TestCase]]],
            typing.Callable[[typing.List[TestCase]], typing.List[TestCase]],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"]
        ) -> typing.Callable[
            [typing.Callable[[TestSubmissionStatus], TestSubmissionStatus]],
            typing.Callable[[TestSubmissionStatus], TestSubmissionStatus],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                elif field_name == "default_test_cases":
                    cls._default_test_cases_validators.append(validator)
                elif field_name == "custom_test_cases":
                    cls._custom_test_cases_validators.append(validator)
                elif field_name == "status":
                    cls._status_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on TestSubmissionState: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
