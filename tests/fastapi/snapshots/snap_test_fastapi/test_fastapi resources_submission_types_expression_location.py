import typing

import pydantic
import typing_extensions


class ExpressionLocation(pydantic.BaseModel):
    start: int
    offset: int

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("start")
    def _validate_start(cls, start: int) -> int:
        for validator in ExpressionLocation.Validators._start_validators:
            start = validator(start)
        return start

    @pydantic.validator("offset")
    def _validate_offset(cls, offset: int) -> int:
        for validator in ExpressionLocation.Validators._offset_validators:
            offset = validator(offset)
        return offset

    class Validators:
        _start_validators: typing.ClassVar[typing.List[typing.Callable[[int], int]]] = []
        _offset_validators: typing.ClassVar[typing.List[typing.Callable[[int], int]]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["start"]
        ) -> typing.Callable[[typing.Callable[[int], int]], typing.Callable[[int], int]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"]
        ) -> typing.Callable[[typing.Callable[[int], int]], typing.Callable[[int], int]]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "start":
                    cls._start_validators.append(validator)
                elif field_name == "offset":
                    cls._offset_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on ExpressionLocation: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
