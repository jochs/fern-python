# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.binary_tree_node_value import BinaryTreeNodeValue
from ..commons.binary_tree_value import BinaryTreeValue
from ..commons.doubly_linked_list_node_value import DoublyLinkedListNodeValue
from ..commons.doubly_linked_list_value import DoublyLinkedListValue
from ..commons.key_value_pair import KeyValuePair
from ..commons.map_value import MapValue
from ..commons.node_id import NodeId
from ..commons.singly_linked_list_node_value import SinglyLinkedListNodeValue
from ..commons.singly_linked_list_value import SinglyLinkedListValue
from ..commons.variable_value import VariableValue
from ..v_2.problem.test_case_id import TestCaseId
from .error_info import ErrorInfo
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2
from .graded_test_case_update import GradedTestCaseUpdate
from .recorded_test_case_update import RecordedTestCaseUpdate
from .running_submission_state import RunningSubmissionState
from .test_case_grade import TestCaseGrade
from .test_case_hidden_grade import TestCaseHiddenGrade
from .test_case_non_hidden_grade import TestCaseNonHiddenGrade

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def running(self, value: RunningSubmissionState) -> TestSubmissionUpdateInfo:
        return TestSubmissionUpdateInfo(__root__=_TestSubmissionUpdateInfo.Running(type="running", value=value))

    def stopped(self) -> TestSubmissionUpdateInfo:
        return TestSubmissionUpdateInfo(__root__=_TestSubmissionUpdateInfo.Stopped(type="stopped"))

    def errored(self, value: ErrorInfo) -> TestSubmissionUpdateInfo:
        return TestSubmissionUpdateInfo(__root__=_TestSubmissionUpdateInfo.Errored(type="errored", value=value))

    def graded_test_case(self, value: GradedTestCaseUpdate) -> TestSubmissionUpdateInfo:
        return TestSubmissionUpdateInfo(
            __root__=_TestSubmissionUpdateInfo.GradedTestCase(**dict(value), type="gradedTestCase")
        )

    def recorded_test_case(self, value: RecordedTestCaseUpdate) -> TestSubmissionUpdateInfo:
        return TestSubmissionUpdateInfo(
            __root__=_TestSubmissionUpdateInfo.RecordedTestCase(**dict(value), type="recordedTestCase")
        )

    def finished(self) -> TestSubmissionUpdateInfo:
        return TestSubmissionUpdateInfo(__root__=_TestSubmissionUpdateInfo.Finished(type="finished"))


class TestSubmissionUpdateInfo(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _TestSubmissionUpdateInfo.Running,
        _TestSubmissionUpdateInfo.Stopped,
        _TestSubmissionUpdateInfo.Errored,
        _TestSubmissionUpdateInfo.GradedTestCase,
        _TestSubmissionUpdateInfo.RecordedTestCase,
        _TestSubmissionUpdateInfo.Finished,
    ]:
        return self.__root__

    def visit(
        self,
        running: typing.Callable[[RunningSubmissionState], T_Result],
        stopped: typing.Callable[[], T_Result],
        errored: typing.Callable[[ErrorInfo], T_Result],
        graded_test_case: typing.Callable[[GradedTestCaseUpdate], T_Result],
        recorded_test_case: typing.Callable[[RecordedTestCaseUpdate], T_Result],
        finished: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.__root__.type == "running":
            return running(self.__root__.value)
        if self.__root__.type == "stopped":
            return stopped()
        if self.__root__.type == "errored":
            return errored(self.__root__.value)
        if self.__root__.type == "gradedTestCase":
            return graded_test_case(self.__root__)
        if self.__root__.type == "recordedTestCase":
            return recorded_test_case(self.__root__)
        if self.__root__.type == "finished":
            return finished()

    __root__: typing_extensions.Annotated[
        typing.Union[
            _TestSubmissionUpdateInfo.Running,
            _TestSubmissionUpdateInfo.Stopped,
            _TestSubmissionUpdateInfo.Errored,
            _TestSubmissionUpdateInfo.GradedTestCase,
            _TestSubmissionUpdateInfo.RecordedTestCase,
            _TestSubmissionUpdateInfo.Finished,
        ],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestSubmissionUpdateInfo.Validators.validate
            def validate(value: typing.Union[_TestSubmissionUpdateInfo.Running, _TestSubmissionUpdateInfo.Stopped, _TestSubmissionUpdateInfo.Errored, _TestSubmissionUpdateInfo.GradedTestCase, _TestSubmissionUpdateInfo.RecordedTestCase, _TestSubmissionUpdateInfo.Finished]) -> typing.Union[_TestSubmissionUpdateInfo.Running, _TestSubmissionUpdateInfo.Stopped, _TestSubmissionUpdateInfo.Errored, _TestSubmissionUpdateInfo.GradedTestCase, _TestSubmissionUpdateInfo.RecordedTestCase, _TestSubmissionUpdateInfo.Finished]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _TestSubmissionUpdateInfo.Running,
                            _TestSubmissionUpdateInfo.Stopped,
                            _TestSubmissionUpdateInfo.Errored,
                            _TestSubmissionUpdateInfo.GradedTestCase,
                            _TestSubmissionUpdateInfo.RecordedTestCase,
                            _TestSubmissionUpdateInfo.Finished,
                        ]
                    ],
                    typing.Union[
                        _TestSubmissionUpdateInfo.Running,
                        _TestSubmissionUpdateInfo.Stopped,
                        _TestSubmissionUpdateInfo.Errored,
                        _TestSubmissionUpdateInfo.GradedTestCase,
                        _TestSubmissionUpdateInfo.RecordedTestCase,
                        _TestSubmissionUpdateInfo.Finished,
                    ],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _TestSubmissionUpdateInfo.Running,
                        _TestSubmissionUpdateInfo.Stopped,
                        _TestSubmissionUpdateInfo.Errored,
                        _TestSubmissionUpdateInfo.GradedTestCase,
                        _TestSubmissionUpdateInfo.RecordedTestCase,
                        _TestSubmissionUpdateInfo.Finished,
                    ]
                ],
                typing.Union[
                    _TestSubmissionUpdateInfo.Running,
                    _TestSubmissionUpdateInfo.Stopped,
                    _TestSubmissionUpdateInfo.Errored,
                    _TestSubmissionUpdateInfo.GradedTestCase,
                    _TestSubmissionUpdateInfo.RecordedTestCase,
                    _TestSubmissionUpdateInfo.Finished,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _TestSubmissionUpdateInfo.Running,
                _TestSubmissionUpdateInfo.Stopped,
                _TestSubmissionUpdateInfo.Errored,
                _TestSubmissionUpdateInfo.GradedTestCase,
                _TestSubmissionUpdateInfo.RecordedTestCase,
                _TestSubmissionUpdateInfo.Finished,
            ],
            values.get("__root__"),
        )
        for validator in TestSubmissionUpdateInfo.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True


class _TestSubmissionUpdateInfo:
    class Running(pydantic.BaseModel):
        type: typing_extensions.Literal["running"]
        value: RunningSubmissionState

        class Config:
            frozen = True

    class Stopped(pydantic.BaseModel):
        type: typing_extensions.Literal["stopped"]

        class Config:
            frozen = True

    class Errored(pydantic.BaseModel):
        type: typing_extensions.Literal["errored"]
        value: ErrorInfo

        class Config:
            frozen = True

    class GradedTestCase(GradedTestCaseUpdate):
        type: typing_extensions.Literal["gradedTestCase"]

        class Config:
            frozen = True

    class RecordedTestCase(RecordedTestCaseUpdate):
        type: typing_extensions.Literal["recordedTestCase"]

        class Config:
            frozen = True

    class Finished(pydantic.BaseModel):
        type: typing_extensions.Literal["finished"]

        class Config:
            frozen = True


_TestSubmissionUpdateInfo.GradedTestCase.update_forward_refs(
    TestCaseId=TestCaseId,
    TestCaseGrade=TestCaseGrade,
    TestCaseHiddenGrade=TestCaseHiddenGrade,
    TestCaseNonHiddenGrade=TestCaseNonHiddenGrade,
    VariableValue=VariableValue,
    MapValue=MapValue,
    KeyValuePair=KeyValuePair,
    BinaryTreeValue=BinaryTreeValue,
    NodeId=NodeId,
    BinaryTreeNodeValue=BinaryTreeNodeValue,
    SinglyLinkedListValue=SinglyLinkedListValue,
    SinglyLinkedListNodeValue=SinglyLinkedListNodeValue,
    DoublyLinkedListValue=DoublyLinkedListValue,
    DoublyLinkedListNodeValue=DoublyLinkedListNodeValue,
    ExceptionV2=ExceptionV2,
    ExceptionInfo=ExceptionInfo,
)
_TestSubmissionUpdateInfo.RecordedTestCase.update_forward_refs(TestCaseId=TestCaseId)
TestSubmissionUpdateInfo.update_forward_refs()
