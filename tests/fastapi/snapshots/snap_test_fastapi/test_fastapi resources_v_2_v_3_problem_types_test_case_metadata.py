import typing

import pydantic
import typing_extensions

from .test_case_id import TestCaseId


class TestCaseMetadata(pydantic.BaseModel):
    id: TestCaseId
    name: str
    hidden: bool

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("id")
    def _validate_id(cls, id: TestCaseId) -> TestCaseId:
        for validator in TestCaseMetadata.Validators._id_validators:
            id = validator(id)
        return id

    @pydantic.validator("name")
    def _validate_name(cls, name: str) -> str:
        for validator in TestCaseMetadata.Validators._name_validators:
            name = validator(name)
        return name

    @pydantic.validator("hidden")
    def _validate_hidden(cls, hidden: bool) -> bool:
        for validator in TestCaseMetadata.Validators._hidden_validators:
            hidden = validator(hidden)
        return hidden

    class Validators:
        _id_validators: typing.ClassVar[typing.List[typing.Callable[[TestCaseId], TestCaseId]]] = []
        _name_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _hidden_validators: typing.ClassVar[typing.List[typing.Callable[[bool], bool]]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"]
        ) -> typing.Callable[[typing.Callable[[TestCaseId], TestCaseId]], typing.Callable[[TestCaseId], TestCaseId]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["hidden"]
        ) -> typing.Callable[[typing.Callable[[bool], bool]], typing.Callable[[bool], bool]]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    cls._id_validators.append(validator)
                elif field_name == "name":
                    cls._name_validators.append(validator)
                elif field_name == "hidden":
                    cls._hidden_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on TestCaseMetadata: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
