# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class LightweightStackframeInformation(pydantic.BaseModel):
    num_stack_frames: int = pydantic.Field(alias="numStackFrames")
    top_stack_frame_method_name: str = pydantic.Field(alias="topStackFrameMethodName")

    class Partial(typing_extensions.TypedDict):
        num_stack_frames: typing_extensions.NotRequired[int]
        top_stack_frame_method_name: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @LightweightStackframeInformation.Validators.root()
            def validate(values: LightweightStackframeInformation.Partial) -> LightweightStackframeInformation.Partial:
                ...

            @LightweightStackframeInformation.Validators.field("num_stack_frames")
            def validate_num_stack_frames(num_stack_frames: int, values: LightweightStackframeInformation.Partial) -> int:
                ...

            @LightweightStackframeInformation.Validators.field("top_stack_frame_method_name")
            def validate_top_stack_frame_method_name(top_stack_frame_method_name: str, values: LightweightStackframeInformation.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[LightweightStackframeInformation.Validators._PreRootValidator]
        ] = []
        _post_validators: typing.ClassVar[typing.List[LightweightStackframeInformation.Validators._RootValidator]] = []
        _num_stack_frames_pre_validators: typing.ClassVar[
            typing.List[LightweightStackframeInformation.Validators.PreNumStackFramesValidator]
        ] = []
        _num_stack_frames_post_validators: typing.ClassVar[
            typing.List[LightweightStackframeInformation.Validators.NumStackFramesValidator]
        ] = []
        _top_stack_frame_method_name_pre_validators: typing.ClassVar[
            typing.List[LightweightStackframeInformation.Validators.PreTopStackFrameMethodNameValidator]
        ] = []
        _top_stack_frame_method_name_post_validators: typing.ClassVar[
            typing.List[LightweightStackframeInformation.Validators.TopStackFrameMethodNameValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators._RootValidator],
            LightweightStackframeInformation.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators._PreRootValidator],
            LightweightStackframeInformation.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["num_stack_frames"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators.PreNumStackFramesValidator],
            LightweightStackframeInformation.Validators.PreNumStackFramesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["num_stack_frames"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators.NumStackFramesValidator],
            LightweightStackframeInformation.Validators.NumStackFramesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["top_stack_frame_method_name"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators.PreTopStackFrameMethodNameValidator],
            LightweightStackframeInformation.Validators.PreTopStackFrameMethodNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["top_stack_frame_method_name"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [LightweightStackframeInformation.Validators.TopStackFrameMethodNameValidator],
            LightweightStackframeInformation.Validators.TopStackFrameMethodNameValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "num_stack_frames":
                    if pre:
                        cls._num_stack_frames_pre_validators.append(validator)
                    else:
                        cls._num_stack_frames_post_validators.append(validator)
                if field_name == "top_stack_frame_method_name":
                    if pre:
                        cls._top_stack_frame_method_name_pre_validators.append(validator)
                    else:
                        cls._top_stack_frame_method_name_post_validators.append(validator)
                return validator

            return decorator

        class PreNumStackFramesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: LightweightStackframeInformation.Partial) -> typing.Any:
                ...

        class NumStackFramesValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: LightweightStackframeInformation.Partial) -> int:
                ...

        class PreTopStackFrameMethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: LightweightStackframeInformation.Partial) -> typing.Any:
                ...

        class TopStackFrameMethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: LightweightStackframeInformation.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: LightweightStackframeInformation.Partial
            ) -> LightweightStackframeInformation.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: LightweightStackframeInformation.Partial
    ) -> LightweightStackframeInformation.Partial:
        for validator in LightweightStackframeInformation.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: LightweightStackframeInformation.Partial
    ) -> LightweightStackframeInformation.Partial:
        for validator in LightweightStackframeInformation.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("num_stack_frames", pre=True)
    def _pre_validate_num_stack_frames(cls, v: int, values: LightweightStackframeInformation.Partial) -> int:
        for validator in LightweightStackframeInformation.Validators._num_stack_frames_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("num_stack_frames", pre=False)
    def _post_validate_num_stack_frames(cls, v: int, values: LightweightStackframeInformation.Partial) -> int:
        for validator in LightweightStackframeInformation.Validators._num_stack_frames_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("top_stack_frame_method_name", pre=True)
    def _pre_validate_top_stack_frame_method_name(cls, v: str, values: LightweightStackframeInformation.Partial) -> str:
        for validator in LightweightStackframeInformation.Validators._top_stack_frame_method_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("top_stack_frame_method_name", pre=False)
    def _post_validate_top_stack_frame_method_name(
        cls, v: str, values: LightweightStackframeInformation.Partial
    ) -> str:
        for validator in LightweightStackframeInformation.Validators._top_stack_frame_method_name_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
