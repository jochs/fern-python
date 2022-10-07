from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2
from .variable_value import VariableValue

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def value(self, value: VariableValue) -> ActualResult:
        return ActualResult(__root__=_ActualResult.Value(type="value", value=value))

    def exception(self, value: ExceptionInfo) -> ActualResult:
        return ActualResult(__root__=_ActualResult.Exception(**dict(value), type="exception"))

    def exception_v_2(self, value: ExceptionV2) -> ActualResult:
        return ActualResult(__root__=_ActualResult.ExceptionV2(type="exceptionV2", value=value))


class ActualResult(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]:
        return self.__root__

    def visit(
        self,
        value: typing.Callable[[VariableValue], T_Result],
        exception: typing.Callable[[ExceptionInfo], T_Result],
        exception_v_2: typing.Callable[[ExceptionV2], T_Result],
    ) -> T_Result:
        if self.__root__.type == "value":
            return value(self.__root__.value)
        if self.__root__.type == "exception":
            return exception(self.__root__)
        if self.__root__.type == "exceptionV2":
            return exception_v_2(self.__root__.exception_v_2)

    __root__: typing_extensions.Annotated[
        typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
        pydantic.Field(discriminator="type"),
    ]

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
            values.get("__root__"),
        )
        for validator in ActualResult.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]],
                    typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2]],
                typing.Union[_ActualResult.Value, _ActualResult.Exception, _ActualResult.ExceptionV2],
            ],
        ) -> None:
            cls._validators.append(validator)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True


class _ActualResult:
    class Value(pydantic.BaseModel):
        type: typing_extensions.Literal["value"]
        value: VariableValue

        class Config:
            frozen = True

    class Exception(ExceptionInfo):
        type: typing_extensions.Literal["exception"]

        class Config:
            frozen = True

    class ExceptionV2(pydantic.BaseModel):
        type: typing_extensions.Literal["exceptionV2"]
        value: ExceptionV2

        class Config:
            frozen = True


ActualResult.update_forward_refs()
