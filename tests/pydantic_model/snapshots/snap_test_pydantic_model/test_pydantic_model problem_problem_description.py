# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .problem_description_board import ProblemDescriptionBoard


class ProblemDescription(pydantic.BaseModel):
    boards: typing.List[ProblemDescriptionBoard]

    class Partial(typing_extensions.TypedDict):
        boards: typing_extensions.NotRequired[typing.List[ProblemDescriptionBoard]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ProblemDescription.Validators.root
            def validate(values: ProblemDescription.Partial) -> ProblemDescription.Partial:
                ...

            @ProblemDescription.Validators.field("boards")
            def validate_boards(boards: typing.List[ProblemDescriptionBoard], values: ProblemDescription.Partial) -> typing.List[ProblemDescriptionBoard]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[ProblemDescription.Partial], ProblemDescription.Partial]]
        ] = []
        _boards_validators: typing.ClassVar[typing.List[ProblemDescription.Validators.BoardsValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[ProblemDescription.Partial], ProblemDescription.Partial]
        ) -> typing.Callable[[ProblemDescription.Partial], ProblemDescription.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["boards"]
        ) -> typing.Callable[
            [ProblemDescription.Validators.BoardsValidator], ProblemDescription.Validators.BoardsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "boards":
                    cls._boards_validators.append(validator)
                return validator

            return decorator

        class BoardsValidator(typing_extensions.Protocol):
            def __call__(
                self, boards: typing.List[ProblemDescriptionBoard], *, values: ProblemDescription.Partial
            ) -> typing.List[ProblemDescriptionBoard]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: ProblemDescription.Partial) -> ProblemDescription.Partial:
        for validator in ProblemDescription.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("boards")
    def _validate_boards(
        cls, boards: typing.List[ProblemDescriptionBoard], values: ProblemDescription.Partial
    ) -> typing.List[ProblemDescriptionBoard]:
        for validator in ProblemDescription.Validators._boards_validators:
            boards = validator(boards, values=values)
        return boards

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
