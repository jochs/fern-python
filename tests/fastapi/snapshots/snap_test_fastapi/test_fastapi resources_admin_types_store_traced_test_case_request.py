import typing

import pydantic
import typing_extensions

from ...submission.types.test_case_result_with_stdout import TestCaseResultWithStdout
from ...submission.types.trace_response import TraceResponse


class StoreTracedTestCaseRequest(pydantic.BaseModel):
    result: TestCaseResultWithStdout
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("result")
    def _validate_result(cls, result: TestCaseResultWithStdout) -> TestCaseResultWithStdout:
        for validator in StoreTracedTestCaseRequest.Validators._result_validators:
            result = validator(result)
        return result

    @pydantic.validator("trace_responses")
    def _validate_trace_responses(cls, trace_responses: typing.List[TraceResponse]) -> typing.List[TraceResponse]:
        for validator in StoreTracedTestCaseRequest.Validators._trace_responses_validators:
            trace_responses = validator(trace_responses)
        return trace_responses

    class Validators:
        _result_validators: typing.ClassVar[
            typing.List[typing.Callable[[TestCaseResultWithStdout], TestCaseResultWithStdout]]
        ] = []
        _trace_responses_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[TraceResponse]], typing.List[TraceResponse]]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["result"]
        ) -> typing.Callable[
            [typing.Callable[[TestCaseResultWithStdout], TestCaseResultWithStdout]],
            typing.Callable[[TestCaseResultWithStdout], TestCaseResultWithStdout],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[TraceResponse]], typing.List[TraceResponse]]],
            typing.Callable[[typing.List[TraceResponse]], typing.List[TraceResponse]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "result":
                    cls._result_validators.append(validator)
                elif field_name == "trace_responses":
                    cls._trace_responses_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on StoreTracedTestCaseRequest: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
