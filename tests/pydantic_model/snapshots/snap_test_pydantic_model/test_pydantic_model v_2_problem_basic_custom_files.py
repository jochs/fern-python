# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.language import Language
from .basic_test_case_template import BasicTestCaseTemplate
from .files import Files
from .non_void_function_signature import NonVoidFunctionSignature


class BasicCustomFiles(pydantic.BaseModel):
    method_name: str = pydantic.Field(alias="methodName")
    signature: NonVoidFunctionSignature
    additional_files: typing.Dict[Language, Files] = pydantic.Field(alias="additionalFiles")
    basic_test_case_template: BasicTestCaseTemplate = pydantic.Field(alias="basicTestCaseTemplate")

    class Partial(typing_extensions.TypedDict):
        method_name: typing_extensions.NotRequired[str]
        signature: typing_extensions.NotRequired[NonVoidFunctionSignature]
        additional_files: typing_extensions.NotRequired[typing.Dict[Language, Files]]
        basic_test_case_template: typing_extensions.NotRequired[BasicTestCaseTemplate]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BasicCustomFiles.Validators.root()
            def validate(values: BasicCustomFiles.Partial) -> BasicCustomFiles.Partial:
                ...

            @BasicCustomFiles.Validators.field("method_name")
            def validate_method_name(method_name: str, values: BasicCustomFiles.Partial) -> str:
                ...

            @BasicCustomFiles.Validators.field("signature")
            def validate_signature(signature: NonVoidFunctionSignature, values: BasicCustomFiles.Partial) -> NonVoidFunctionSignature:
                ...

            @BasicCustomFiles.Validators.field("additional_files")
            def validate_additional_files(additional_files: typing.Dict[Language, Files], values: BasicCustomFiles.Partial) -> typing.Dict[Language, Files]:
                ...

            @BasicCustomFiles.Validators.field("basic_test_case_template")
            def validate_basic_test_case_template(basic_test_case_template: BasicTestCaseTemplate, values: BasicCustomFiles.Partial) -> BasicTestCaseTemplate:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[BasicCustomFiles.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[BasicCustomFiles.Validators._RootValidator]] = []
        _method_name_pre_validators: typing.ClassVar[
            typing.List[BasicCustomFiles.Validators.PreMethodNameValidator]
        ] = []
        _method_name_post_validators: typing.ClassVar[typing.List[BasicCustomFiles.Validators.MethodNameValidator]] = []
        _signature_pre_validators: typing.ClassVar[typing.List[BasicCustomFiles.Validators.PreSignatureValidator]] = []
        _signature_post_validators: typing.ClassVar[typing.List[BasicCustomFiles.Validators.SignatureValidator]] = []
        _additional_files_pre_validators: typing.ClassVar[
            typing.List[BasicCustomFiles.Validators.PreAdditionalFilesValidator]
        ] = []
        _additional_files_post_validators: typing.ClassVar[
            typing.List[BasicCustomFiles.Validators.AdditionalFilesValidator]
        ] = []
        _basic_test_case_template_pre_validators: typing.ClassVar[
            typing.List[BasicCustomFiles.Validators.PreBasicTestCaseTemplateValidator]
        ] = []
        _basic_test_case_template_post_validators: typing.ClassVar[
            typing.List[BasicCustomFiles.Validators.BasicTestCaseTemplateValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[BasicCustomFiles.Validators._RootValidator], BasicCustomFiles.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators._PreRootValidator], BasicCustomFiles.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.PreMethodNameValidator], BasicCustomFiles.Validators.PreMethodNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.MethodNameValidator], BasicCustomFiles.Validators.MethodNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.PreSignatureValidator], BasicCustomFiles.Validators.PreSignatureValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["signature"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.SignatureValidator], BasicCustomFiles.Validators.SignatureValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["additional_files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.PreAdditionalFilesValidator],
            BasicCustomFiles.Validators.PreAdditionalFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["additional_files"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.AdditionalFilesValidator], BasicCustomFiles.Validators.AdditionalFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["basic_test_case_template"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.PreBasicTestCaseTemplateValidator],
            BasicCustomFiles.Validators.PreBasicTestCaseTemplateValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["basic_test_case_template"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [BasicCustomFiles.Validators.BasicTestCaseTemplateValidator],
            BasicCustomFiles.Validators.BasicTestCaseTemplateValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "method_name":
                    if pre:
                        cls._method_name_pre_validators.append(validator)
                    else:
                        cls._method_name_post_validators.append(validator)
                if field_name == "signature":
                    if pre:
                        cls._signature_pre_validators.append(validator)
                    else:
                        cls._signature_post_validators.append(validator)
                if field_name == "additional_files":
                    if pre:
                        cls._additional_files_pre_validators.append(validator)
                    else:
                        cls._additional_files_post_validators.append(validator)
                if field_name == "basic_test_case_template":
                    if pre:
                        cls._basic_test_case_template_pre_validators.append(validator)
                    else:
                        cls._basic_test_case_template_post_validators.append(validator)
                return validator

            return decorator

        class PreMethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicCustomFiles.Partial) -> typing.Any:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: BasicCustomFiles.Partial) -> str:
                ...

        class PreSignatureValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicCustomFiles.Partial) -> typing.Any:
                ...

        class SignatureValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: NonVoidFunctionSignature, __values: BasicCustomFiles.Partial
            ) -> NonVoidFunctionSignature:
                ...

        class PreAdditionalFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicCustomFiles.Partial) -> typing.Any:
                ...

        class AdditionalFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, Files], __values: BasicCustomFiles.Partial
            ) -> typing.Dict[Language, Files]:
                ...

        class PreBasicTestCaseTemplateValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BasicCustomFiles.Partial) -> typing.Any:
                ...

        class BasicTestCaseTemplateValidator(typing_extensions.Protocol):
            def __call__(self, __v: BasicTestCaseTemplate, __values: BasicCustomFiles.Partial) -> BasicTestCaseTemplate:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: BasicCustomFiles.Partial) -> BasicCustomFiles.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: BasicCustomFiles.Partial) -> BasicCustomFiles.Partial:
        for validator in BasicCustomFiles.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: BasicCustomFiles.Partial) -> BasicCustomFiles.Partial:
        for validator in BasicCustomFiles.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("method_name", pre=True)
    def _pre_validate_method_name(cls, v: str, values: BasicCustomFiles.Partial) -> str:
        for validator in BasicCustomFiles.Validators._method_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("method_name", pre=False)
    def _post_validate_method_name(cls, v: str, values: BasicCustomFiles.Partial) -> str:
        for validator in BasicCustomFiles.Validators._method_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("signature", pre=True)
    def _pre_validate_signature(
        cls, v: NonVoidFunctionSignature, values: BasicCustomFiles.Partial
    ) -> NonVoidFunctionSignature:
        for validator in BasicCustomFiles.Validators._signature_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("signature", pre=False)
    def _post_validate_signature(
        cls, v: NonVoidFunctionSignature, values: BasicCustomFiles.Partial
    ) -> NonVoidFunctionSignature:
        for validator in BasicCustomFiles.Validators._signature_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("additional_files", pre=True)
    def _pre_validate_additional_files(
        cls, v: typing.Dict[Language, Files], values: BasicCustomFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in BasicCustomFiles.Validators._additional_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("additional_files", pre=False)
    def _post_validate_additional_files(
        cls, v: typing.Dict[Language, Files], values: BasicCustomFiles.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in BasicCustomFiles.Validators._additional_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("basic_test_case_template", pre=True)
    def _pre_validate_basic_test_case_template(
        cls, v: BasicTestCaseTemplate, values: BasicCustomFiles.Partial
    ) -> BasicTestCaseTemplate:
        for validator in BasicCustomFiles.Validators._basic_test_case_template_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("basic_test_case_template", pre=False)
    def _post_validate_basic_test_case_template(
        cls, v: BasicTestCaseTemplate, values: BasicCustomFiles.Partial
    ) -> BasicTestCaseTemplate:
        for validator in BasicCustomFiles.Validators._basic_test_case_template_post_validators:
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
