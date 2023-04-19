# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .compile_error import CompileError as resources_submission_types_compile_error_CompileError
from .internal_error import InternalError as resources_submission_types_internal_error_InternalError
from .runtime_error import RuntimeError as resources_submission_types_runtime_error_RuntimeError

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def compile_error(self, value: resources_submission_types_compile_error_CompileError) -> ErrorInfo:
        return ErrorInfo(__root__=_ErrorInfo.CompileError(**dict(value), type="compileError"))

    def runtime_error(self, value: resources_submission_types_runtime_error_RuntimeError) -> ErrorInfo:
        return ErrorInfo(__root__=_ErrorInfo.RuntimeError(**dict(value), type="runtimeError"))

    def internal_error(self, value: resources_submission_types_internal_error_InternalError) -> ErrorInfo:
        return ErrorInfo(__root__=_ErrorInfo.InternalError(**dict(value), type="internalError"))


class ErrorInfo(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError]:
        return self.__root__

    def visit(
        self,
        compile_error: typing.Callable[[resources_submission_types_compile_error_CompileError], T_Result],
        runtime_error: typing.Callable[[resources_submission_types_runtime_error_RuntimeError], T_Result],
        internal_error: typing.Callable[[resources_submission_types_internal_error_InternalError], T_Result],
    ) -> T_Result:
        if self.__root__.type == "compileError":
            return compile_error(self.__root__)
        if self.__root__.type == "runtimeError":
            return runtime_error(self.__root__)
        if self.__root__.type == "internalError":
            return internal_error(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ErrorInfo.Validators.validate
            def validate(value: typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError]) -> typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError]],
                    typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError]],
                typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError],
            values.get("__root__"),
        )
        for validator in ErrorInfo.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _ErrorInfo:
    class CompileError(resources_submission_types_compile_error_CompileError):
        type: typing_extensions.Literal["compileError"]

        class Config:
            allow_population_by_field_name = True

    class RuntimeError(resources_submission_types_runtime_error_RuntimeError):
        type: typing_extensions.Literal["runtimeError"]

        class Config:
            allow_population_by_field_name = True

    class InternalError(resources_submission_types_internal_error_InternalError):
        type: typing_extensions.Literal["internalError"]

        class Config:
            allow_population_by_field_name = True


ErrorInfo.update_forward_refs()
