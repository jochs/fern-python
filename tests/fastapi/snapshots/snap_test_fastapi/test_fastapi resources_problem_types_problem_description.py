# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .problem_description_board import ProblemDescriptionBoard


class ProblemDescription(pydantic.BaseModel):
    boards: typing.List[ProblemDescriptionBoard]

    class Partial(typing_extensions.TypedDict):
        boards: typing_extensions.NotRequired[typing.List[ProblemDescriptionBoard]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ProblemDescription.Validators.root()
            def validate(values: ProblemDescription.Partial) -> ProblemDescription.Partial:
                ...

            @ProblemDescription.Validators.field("boards")
            def validate_boards(boards: typing.List[ProblemDescriptionBoard], values: ProblemDescription.Partial) -> typing.List[ProblemDescriptionBoard]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ProblemDescription.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ProblemDescription.Validators._RootValidator]] = []
        _boards_pre_validators: typing.ClassVar[typing.List[ProblemDescription.Validators.PreBoardsValidator]] = []
        _boards_post_validators: typing.ClassVar[typing.List[ProblemDescription.Validators.BoardsValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ProblemDescription.Validators._RootValidator], ProblemDescription.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemDescription.Validators._PreRootValidator], ProblemDescription.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["boards"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemDescription.Validators.PreBoardsValidator], ProblemDescription.Validators.PreBoardsValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["boards"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ProblemDescription.Validators.BoardsValidator], ProblemDescription.Validators.BoardsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "boards":
                    if pre:
                        cls._boards_pre_validators.append(validator)
                    else:
                        cls._boards_post_validators.append(validator)
                return validator

            return decorator

        class PreBoardsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemDescription.Partial) -> typing.Any:
                ...

        class BoardsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[ProblemDescriptionBoard], __values: ProblemDescription.Partial
            ) -> typing.List[ProblemDescriptionBoard]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ProblemDescription.Partial) -> ProblemDescription.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: ProblemDescription.Partial) -> ProblemDescription.Partial:
        for validator in ProblemDescription.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: ProblemDescription.Partial) -> ProblemDescription.Partial:
        for validator in ProblemDescription.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("boards", pre=True)
    def _pre_validate_boards(
        cls, v: typing.List[ProblemDescriptionBoard], values: ProblemDescription.Partial
    ) -> typing.List[ProblemDescriptionBoard]:
        for validator in ProblemDescription.Validators._boards_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("boards", pre=False)
    def _post_validate_boards(
        cls, v: typing.List[ProblemDescriptionBoard], values: ProblemDescription.Partial
    ) -> typing.List[ProblemDescriptionBoard]:
        for validator in ProblemDescription.Validators._boards_post_validators:
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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
