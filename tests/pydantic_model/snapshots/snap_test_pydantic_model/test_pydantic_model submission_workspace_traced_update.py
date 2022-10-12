# This file was auto-generated by Fern from our API Definition.

# type: ignore
# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class WorkspaceTracedUpdate(pydantic.BaseModel):
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceTracedUpdate.Validators.field("trace_responses_size")
            def validate_trace_responses_size(v: int, values: WorkspaceTracedUpdate.Partial) -> int:
                ...
        """

        _trace_responses_size_validators: typing.ClassVar[
            typing.List[WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator]
        ] = []

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses_size"]
        ) -> typing.Callable[
            [WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator],
            WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "trace_responses_size":
                    cls._trace_responses_size_validators.append(validator)
                return validator

            return decorator

        class TraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, v: int, *, values: WorkspaceTracedUpdate.Partial) -> int:
                ...

    @pydantic.validator("trace_responses_size")
    def _validate_trace_responses_size(cls, v: int, values: int) -> int:
        for validator in WorkspaceTracedUpdate.Validators._trace_responses_size_validators:
            v = validator(v, values=values)
        return v

    class Partial(typing.TypedDict):
        trace_responses_size: typing_extensions.NotRequired[int]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True