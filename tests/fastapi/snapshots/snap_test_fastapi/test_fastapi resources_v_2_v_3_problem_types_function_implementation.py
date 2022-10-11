import typing

import pydantic
import typing_extensions


class FunctionImplementation(pydantic.BaseModel):
    impl: str
    imports: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("impl")
    def _validate_impl(cls, impl: str) -> str:
        for validator in FunctionImplementation.Validators._impl_validators:
            impl = validator(impl)
        return impl

    @pydantic.validator("imports")
    def _validate_imports(cls, imports: typing.Optional[str]) -> typing.Optional[str]:
        for validator in FunctionImplementation.Validators._imports_validators:
            imports = validator(imports)
        return imports

    class Validators:
        _impl_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _imports_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.Optional[str]], typing.Optional[str]]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["impl"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["imports"]
        ) -> typing.Callable[
            [typing.Callable[[typing.Optional[str]], typing.Optional[str]]],
            typing.Callable[[typing.Optional[str]], typing.Optional[str]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "impl":
                    cls._impl_validators.append(validator)
                elif field_name == "imports":
                    cls._imports_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on FunctionImplementation: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
