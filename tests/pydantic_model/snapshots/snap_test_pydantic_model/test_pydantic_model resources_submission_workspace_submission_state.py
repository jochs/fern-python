# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .workspace_submission_status import WorkspaceSubmissionStatus


class WorkspaceSubmissionState(pydantic.BaseModel):
    status: WorkspaceSubmissionStatus

    class Partial(typing_extensions.TypedDict):
        status: typing_extensions.NotRequired[WorkspaceSubmissionStatus]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceSubmissionState.Validators.root()
            def validate(values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionState.Partial:
                ...

            @WorkspaceSubmissionState.Validators.field("status")
            def validate_status(status: WorkspaceSubmissionStatus, values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionStatus:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[WorkspaceSubmissionState.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[WorkspaceSubmissionState.Validators._RootValidator]] = []
        _status_pre_validators: typing.ClassVar[
            typing.List[WorkspaceSubmissionState.Validators.PreStatusValidator]
        ] = []
        _status_post_validators: typing.ClassVar[typing.List[WorkspaceSubmissionState.Validators.StatusValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [WorkspaceSubmissionState.Validators._RootValidator], WorkspaceSubmissionState.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceSubmissionState.Validators._PreRootValidator],
            WorkspaceSubmissionState.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceSubmissionState.Validators.PreStatusValidator],
            WorkspaceSubmissionState.Validators.PreStatusValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [WorkspaceSubmissionState.Validators.StatusValidator], WorkspaceSubmissionState.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "status":
                    if pre:
                        cls._status_pre_validators.append(validator)
                    else:
                        cls._status_post_validators.append(validator)
                return validator

            return decorator

        class PreStatusValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: WorkspaceSubmissionState.Partial) -> typing.Any:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: WorkspaceSubmissionStatus, __values: WorkspaceSubmissionState.Partial
            ) -> WorkspaceSubmissionStatus:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionState.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionState.Partial:
        for validator in WorkspaceSubmissionState.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: WorkspaceSubmissionState.Partial) -> WorkspaceSubmissionState.Partial:
        for validator in WorkspaceSubmissionState.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("status", pre=True)
    def _pre_validate_status(
        cls, v: WorkspaceSubmissionStatus, values: WorkspaceSubmissionState.Partial
    ) -> WorkspaceSubmissionStatus:
        for validator in WorkspaceSubmissionState.Validators._status_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=False)
    def _post_validate_status(
        cls, v: WorkspaceSubmissionStatus, values: WorkspaceSubmissionState.Partial
    ) -> WorkspaceSubmissionStatus:
        for validator in WorkspaceSubmissionState.Validators._status_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
