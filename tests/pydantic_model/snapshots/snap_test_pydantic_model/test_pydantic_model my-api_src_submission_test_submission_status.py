from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .error_info import ErrorInfo
from .running_submission_state import RunningSubmissionState
from .submission_status_for_test_case import SubmissionStatusForTestCase

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def stopped(self) -> TestSubmissionStatus:
        return TestSubmissionStatus(__root__=_TestSubmissionStatus.Stopped(type="stopped"))

    def errored(self, value: ErrorInfo) -> TestSubmissionStatus:
        return TestSubmissionStatus(__root__=_TestSubmissionStatus.Errored(type="errored", errored=value))

    def running(self, value: RunningSubmissionState) -> TestSubmissionStatus:
        return TestSubmissionStatus(__root__=_TestSubmissionStatus.Running(type="running", running=value))

    def test_case_id_to_state(self, value: typing.Dict[str, SubmissionStatusForTestCase]) -> TestSubmissionStatus:
        return TestSubmissionStatus(
            __root__=_TestSubmissionStatus.TestCaseIdToState(type="testCaseIdToState", test_case_id_to_state=value)
        )


class TestSubmissionStatus(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get(
        self,
    ) -> typing.Union[
        _TestSubmissionStatus.Stopped,
        _TestSubmissionStatus.Errored,
        _TestSubmissionStatus.Running,
        _TestSubmissionStatus.TestCaseIdToState,
    ]:
        return self.__root__

    def visit(
        self,
        stopped: typing.Callable[[], T_Result],
        errored: typing.Callable[[ErrorInfo], T_Result],
        running: typing.Callable[[RunningSubmissionState], T_Result],
        test_case_id_to_state: typing.Callable[[typing.Dict[str, SubmissionStatusForTestCase]], T_Result],
    ) -> T_Result:
        if self.__root__.type == "stopped":
            return stopped()
        if self.__root__.type == "errored":
            return errored(self.__root__.errored)
        if self.__root__.type == "running":
            return running(self.__root__.running)
        if self.__root__.type == "testCaseIdToState":
            return test_case_id_to_state(self.__root__.test_case_id_to_state)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _TestSubmissionStatus.Stopped,
            _TestSubmissionStatus.Errored,
            _TestSubmissionStatus.Running,
            _TestSubmissionStatus.TestCaseIdToState,
        ],
        pydantic.Field(discriminator="type"),
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)


class _TestSubmissionStatus:
    class Stopped(pydantic.BaseModel):
        type: typing_extensions.Literal["stopped"]

    class Errored(pydantic.BaseModel):
        type: typing_extensions.Literal["errored"]
        errored: ErrorInfo

    class Running(pydantic.BaseModel):
        type: typing_extensions.Literal["running"]
        running: RunningSubmissionState

    class TestCaseIdToState(pydantic.BaseModel):
        type: typing_extensions.Literal["testCaseIdToState"]
        test_case_id_to_state: typing.Dict[str, SubmissionStatusForTestCase] = pydantic.Field(alias="testCaseIdToState")

        class Config:
            allow_population_by_field_name = True


TestSubmissionStatus.update_forward_refs()