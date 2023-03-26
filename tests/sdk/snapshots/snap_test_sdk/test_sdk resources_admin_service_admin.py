# This file was auto-generated by Fern from our API Definition.

import typing

from ...submission.types.submission_id import SubmissionId
from ...submission.types.test_case_result_with_stdout import TestCaseResultWithStdout
from ...submission.types.test_submission_status import TestSubmissionStatus
from ...submission.types.test_submission_update import TestSubmissionUpdate
from ...submission.types.trace_response import TraceResponse
from ...submission.types.trace_response_v_2 import TraceResponseV2
from ...submission.types.workspace_run_details import WorkspaceRunDetails
from ...submission.types.workspace_submission_status import WorkspaceSubmissionStatus
from ...submission.types.workspace_submission_update import WorkspaceSubmissionUpdate
from ...v_2.resources.problem.types.test_case_id import TestCaseId


class Admin:
    def __init__(self, *, environment: str):
        ...

    def update_test_submission_status(self, *, submission_id: SubmissionId, request: TestSubmissionStatus) -> None:
        ...

    def send_test_submission_update(self, *, submission_id: SubmissionId, request: TestSubmissionUpdate) -> None:
        ...

    def update_workspace_submission_status(
        self, *, submission_id: SubmissionId, request: WorkspaceSubmissionStatus
    ) -> None:
        ...

    def send_workspace_submission_update(
        self, *, submission_id: SubmissionId, request: WorkspaceSubmissionUpdate
    ) -> None:
        ...

    def store_traced_test_case(
        self,
        *,
        submission_id: SubmissionId,
        test_case_id: str,
        result: TestCaseResultWithStdout,
        trace_responses: typing.List[TraceResponse]
    ) -> None:
        ...

    def store_traced_test_case_v_2(
        self, *, submission_id: SubmissionId, test_case_id: TestCaseId, request: typing.List[TraceResponseV2]
    ) -> None:
        ...

    def store_traced_workspace(
        self,
        *,
        submission_id: SubmissionId,
        workspace_run_details: WorkspaceRunDetails,
        trace_responses: typing.List[TraceResponse]
    ) -> None:
        ...

    def store_traced_workspace_v_2(self, *, submission_id: SubmissionId, request: typing.List[TraceResponseV2]) -> None:
        ...