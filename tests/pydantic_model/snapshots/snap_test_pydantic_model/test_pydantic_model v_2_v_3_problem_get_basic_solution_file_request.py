import typing

import pydantic
import typing_extensions

from .non_void_function_signature import NonVoidFunctionSignature


class GetBasicSolutionFileRequest(pydantic.BaseModel):
    method_name: str = pydantic.Field(alias="methodName")
    signature: NonVoidFunctionSignature

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("method_name")
    def _validate_method_name(cls, method_name: str) -> str:
        for validator in GetBasicSolutionFileRequest.Validators._method_name_validators:
            method_name = validator(method_name)
        return method_name

    @pydantic.validator("signature")
    def _validate_signature(cls, signature: NonVoidFunctionSignature) -> NonVoidFunctionSignature:
        for validator in GetBasicSolutionFileRequest.Validators._signature_validators:
            signature = validator(signature)
        return signature

    class Validators:
        _method_name_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _signature_validators: typing.ClassVar[
            typing.List[typing.Callable[[NonVoidFunctionSignature], NonVoidFunctionSignature]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"]
        ) -> typing.Callable[
            [typing.Callable[[NonVoidFunctionSignature], NonVoidFunctionSignature]],
            typing.Callable[[NonVoidFunctionSignature], NonVoidFunctionSignature],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "method_name":
                    cls._method_name_validators.append(validator)
                elif field_name == "signature":
                    cls._signature_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on GetBasicSolutionFileRequest: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
