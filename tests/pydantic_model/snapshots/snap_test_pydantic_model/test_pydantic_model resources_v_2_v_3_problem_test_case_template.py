# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .....core.datetime_utils import serialize_datetime
from .test_case_implementation import TestCaseImplementation
from .test_case_template_id import TestCaseTemplateId


class TestCaseTemplate(pydantic.BaseModel):
    template_id: TestCaseTemplateId = pydantic.Field(alias="templateId")
    name: str
    implementation: TestCaseImplementation

    class Partial(typing_extensions.TypedDict):
        template_id: typing_extensions.NotRequired[TestCaseTemplateId]
        name: typing_extensions.NotRequired[str]
        implementation: typing_extensions.NotRequired[TestCaseImplementation]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseTemplate.Validators.root()
            def validate(values: TestCaseTemplate.Partial) -> TestCaseTemplate.Partial:
                ...

            @TestCaseTemplate.Validators.field("template_id")
            def validate_template_id(template_id: TestCaseTemplateId, values: TestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

            @TestCaseTemplate.Validators.field("name")
            def validate_name(name: str, values: TestCaseTemplate.Partial) -> str:
                ...

            @TestCaseTemplate.Validators.field("implementation")
            def validate_implementation(implementation: TestCaseImplementation, values: TestCaseTemplate.Partial) -> TestCaseImplementation:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCaseTemplate.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCaseTemplate.Validators._RootValidator]] = []
        _template_id_pre_validators: typing.ClassVar[
            typing.List[TestCaseTemplate.Validators.PreTemplateIdValidator]
        ] = []
        _template_id_post_validators: typing.ClassVar[typing.List[TestCaseTemplate.Validators.TemplateIdValidator]] = []
        _name_pre_validators: typing.ClassVar[typing.List[TestCaseTemplate.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[TestCaseTemplate.Validators.NameValidator]] = []
        _implementation_pre_validators: typing.ClassVar[
            typing.List[TestCaseTemplate.Validators.PreImplementationValidator]
        ] = []
        _implementation_post_validators: typing.ClassVar[
            typing.List[TestCaseTemplate.Validators.ImplementationValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TestCaseTemplate.Validators._RootValidator], TestCaseTemplate.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseTemplate.Validators._PreRootValidator], TestCaseTemplate.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["template_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseTemplate.Validators.PreTemplateIdValidator], TestCaseTemplate.Validators.PreTemplateIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TestCaseTemplate.Validators.TemplateIdValidator], TestCaseTemplate.Validators.TemplateIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseTemplate.Validators.PreNameValidator], TestCaseTemplate.Validators.PreNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TestCaseTemplate.Validators.NameValidator], TestCaseTemplate.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["implementation"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseTemplate.Validators.PreImplementationValidator],
            TestCaseTemplate.Validators.PreImplementationValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["implementation"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [TestCaseTemplate.Validators.ImplementationValidator], TestCaseTemplate.Validators.ImplementationValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template_id":
                    if pre:
                        cls._template_id_pre_validators.append(validator)
                    else:
                        cls._template_id_post_validators.append(validator)
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                if field_name == "implementation":
                    if pre:
                        cls._implementation_pre_validators.append(validator)
                    else:
                        cls._implementation_post_validators.append(validator)
                return validator

            return decorator

        class PreTemplateIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseTemplate.Partial) -> typing.Any:
                ...

        class TemplateIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseTemplateId, __values: TestCaseTemplate.Partial) -> TestCaseTemplateId:
                ...

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseTemplate.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: TestCaseTemplate.Partial) -> str:
                ...

        class PreImplementationValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseTemplate.Partial) -> typing.Any:
                ...

        class ImplementationValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseImplementation, __values: TestCaseTemplate.Partial
            ) -> TestCaseImplementation:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCaseTemplate.Partial) -> TestCaseTemplate.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestCaseTemplate.Partial) -> TestCaseTemplate.Partial:
        for validator in TestCaseTemplate.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestCaseTemplate.Partial) -> TestCaseTemplate.Partial:
        for validator in TestCaseTemplate.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("template_id", pre=True)
    def _pre_validate_template_id(cls, v: TestCaseTemplateId, values: TestCaseTemplate.Partial) -> TestCaseTemplateId:
        for validator in TestCaseTemplate.Validators._template_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("template_id", pre=False)
    def _post_validate_template_id(cls, v: TestCaseTemplateId, values: TestCaseTemplate.Partial) -> TestCaseTemplateId:
        for validator in TestCaseTemplate.Validators._template_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: TestCaseTemplate.Partial) -> str:
        for validator in TestCaseTemplate.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: TestCaseTemplate.Partial) -> str:
        for validator in TestCaseTemplate.Validators._name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("implementation", pre=True)
    def _pre_validate_implementation(
        cls, v: TestCaseImplementation, values: TestCaseTemplate.Partial
    ) -> TestCaseImplementation:
        for validator in TestCaseTemplate.Validators._implementation_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("implementation", pre=False)
    def _post_validate_implementation(
        cls, v: TestCaseImplementation, values: TestCaseTemplate.Partial
    ) -> TestCaseImplementation:
        for validator in TestCaseTemplate.Validators._implementation_post_validators:
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
