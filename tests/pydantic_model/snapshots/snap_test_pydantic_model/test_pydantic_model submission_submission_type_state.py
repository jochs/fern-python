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
from ..commons.problem_id import ProblemId
from ..commons.singly_linked_list_node_value import SinglyLinkedListNodeValue
from ..commons.singly_linked_list_value import SinglyLinkedListValue
from ..commons.test_case import TestCase
from ..commons.variable_value import VariableValue
from .actual_result import ActualResult
from .compile_error import CompileError
from .error_info import ErrorInfo
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2
from .internal_error import InternalError
from .running_submission_state import RunningSubmissionState
from .runtime_error import RuntimeError
from .submission_status_for_test_case import SubmissionStatusForTestCase
from .test_case_grade import TestCaseGrade
from .test_case_hidden_grade import TestCaseHiddenGrade
from .test_case_non_hidden_grade import TestCaseNonHiddenGrade
from .test_case_result import TestCaseResult
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .test_submission_state import TestSubmissionState
from .test_submission_status import TestSubmissionStatus
from .traced_test_case import TracedTestCase
from .workspace_run_details import WorkspaceRunDetails
from .workspace_submission_state import WorkspaceSubmissionState
from .workspace_submission_status import WorkspaceSubmissionStatus

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def test(self, value: TestSubmissionState) -> SubmissionTypeState:
        return SubmissionTypeState(__root__=_SubmissionTypeState.Test(**dict(value), type="test"))

    def workspace(self, value: WorkspaceSubmissionState) -> SubmissionTypeState:
        return SubmissionTypeState(__root__=_SubmissionTypeState.Workspace(**dict(value), type="workspace"))


class SubmissionTypeState(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]:
        return self.__root__

    def visit(
        self,
        test: typing.Callable[[TestSubmissionState], T_Result],
        workspace: typing.Callable[[WorkspaceSubmissionState], T_Result],
    ) -> T_Result:
        if self.__root__.type == "test":
            return test(self.__root__)
        if self.__root__.type == "workspace":
            return workspace(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace], pydantic.Field(discriminator="type")
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionTypeState.Validators.validate
            def validate(value: typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]) -> typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]],
                    typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]],
                typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace], values.get("__root__")
        )
        for validator in SubmissionTypeState.Validators._validators:
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


class _SubmissionTypeState:
    class Test(TestSubmissionState):
        type: typing_extensions.Literal["test"]

        class Config:
            frozen = True

    class Workspace(WorkspaceSubmissionState):
        type: typing_extensions.Literal["workspace"]

        class Config:
            frozen = True


_SubmissionTypeState.Test.update_forward_refs(
    ProblemId=ProblemId,
    TestCase=TestCase,
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
    TestSubmissionStatus=TestSubmissionStatus,
    ErrorInfo=ErrorInfo,
    CompileError=CompileError,
    RuntimeError=RuntimeError,
    InternalError=InternalError,
    ExceptionInfo=ExceptionInfo,
    RunningSubmissionState=RunningSubmissionState,
    SubmissionStatusForTestCase=SubmissionStatusForTestCase,
    TestCaseResultWithStdout=TestCaseResultWithStdout,
    TestCaseResult=TestCaseResult,
    ActualResult=ActualResult,
    ExceptionV2=ExceptionV2,
    TestCaseGrade=TestCaseGrade,
    TestCaseHiddenGrade=TestCaseHiddenGrade,
    TestCaseNonHiddenGrade=TestCaseNonHiddenGrade,
    TracedTestCase=TracedTestCase,
)
_SubmissionTypeState.Workspace.update_forward_refs(
    WorkspaceSubmissionStatus=WorkspaceSubmissionStatus,
    ErrorInfo=ErrorInfo,
    CompileError=CompileError,
    RuntimeError=RuntimeError,
    InternalError=InternalError,
    ExceptionInfo=ExceptionInfo,
    RunningSubmissionState=RunningSubmissionState,
    WorkspaceRunDetails=WorkspaceRunDetails,
    ExceptionV2=ExceptionV2,
)
SubmissionTypeState.update_forward_refs()
