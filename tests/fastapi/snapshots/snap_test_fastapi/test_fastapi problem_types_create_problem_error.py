from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .generic_create_problem_error import GenericCreateProblemError

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def generic(self, value: GenericCreateProblemError) -> CreateProblemError:
        return CreateProblemError(__root__=_CreateProblemError.Generic(**dict(value), error_type="generic"))


class CreateProblemError(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_CreateProblemError.Generic]:
        return self.__root__

    def visit(self, generic: typing.Callable[[GenericCreateProblemError], T_Result]) -> T_Result:
        if self.__root__.error_type == "generic":
            return generic(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_CreateProblemError.Generic], pydantic.Field(discriminator="error_type")
    ]

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(typing.Union[_CreateProblemError.Generic], values.get("__root__"))
        for validator in CreateProblemError.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[[typing.Union[_CreateProblemError.Generic]], typing.Union[_CreateProblemError.Generic]]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_CreateProblemError.Generic]], typing.Union[_CreateProblemError.Generic]
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


class _CreateProblemError:
    class Generic(GenericCreateProblemError):
        error_type: typing_extensions.Literal["generic"] = pydantic.Field(alias="_type")

        class Config:
            frozen = True
            allow_population_by_field_name = True


CreateProblemError.update_forward_refs()
