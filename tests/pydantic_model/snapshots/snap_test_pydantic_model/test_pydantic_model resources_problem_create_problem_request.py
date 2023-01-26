# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from ..commons.language import Language
from ..commons.test_case_with_expected_result import TestCaseWithExpectedResult
from ..commons.variable_type import VariableType
from .problem_description import ProblemDescription
from .problem_files import ProblemFiles
from .variable_type_and_name import VariableTypeAndName


class CreateProblemRequest(pydantic.BaseModel):
    problem_name: str = pydantic.Field(alias="problemName")
    problem_description: ProblemDescription = pydantic.Field(alias="problemDescription")
    files: typing.Dict[Language, ProblemFiles]
    input_params: typing.List[VariableTypeAndName] = pydantic.Field(alias="inputParams")
    output_type: VariableType = pydantic.Field(alias="outputType")
    testcases: typing.List[TestCaseWithExpectedResult]
    method_name: str = pydantic.Field(alias="methodName")

    class Partial(typing_extensions.TypedDict):
        problem_name: typing_extensions.NotRequired[str]
        problem_description: typing_extensions.NotRequired[ProblemDescription]
        files: typing_extensions.NotRequired[typing.Dict[Language, ProblemFiles]]
        input_params: typing_extensions.NotRequired[typing.List[VariableTypeAndName]]
        output_type: typing_extensions.NotRequired[VariableType]
        testcases: typing_extensions.NotRequired[typing.List[TestCaseWithExpectedResult]]
        method_name: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CreateProblemRequest.Validators.root()
            def validate(values: CreateProblemRequest.Partial) -> CreateProblemRequest.Partial:
                ...

            @CreateProblemRequest.Validators.field("problem_name")
            def validate_problem_name(problem_name: str, values: CreateProblemRequest.Partial) -> str:
                ...

            @CreateProblemRequest.Validators.field("problem_description")
            def validate_problem_description(problem_description: ProblemDescription, values: CreateProblemRequest.Partial) -> ProblemDescription:
                ...

            @CreateProblemRequest.Validators.field("files")
            def validate_files(files: typing.Dict[Language, ProblemFiles], values: CreateProblemRequest.Partial) -> typing.Dict[Language, ProblemFiles]:
                ...

            @CreateProblemRequest.Validators.field("input_params")
            def validate_input_params(input_params: typing.List[VariableTypeAndName], values: CreateProblemRequest.Partial) -> typing.List[VariableTypeAndName]:
                ...

            @CreateProblemRequest.Validators.field("output_type")
            def validate_output_type(output_type: VariableType, values: CreateProblemRequest.Partial) -> VariableType:
                ...

            @CreateProblemRequest.Validators.field("testcases")
            def validate_testcases(testcases: typing.List[TestCaseWithExpectedResult], values: CreateProblemRequest.Partial) -> typing.List[TestCaseWithExpectedResult]:
                ...

            @CreateProblemRequest.Validators.field("method_name")
            def validate_method_name(method_name: str, values: CreateProblemRequest.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators._RootValidator]] = []
        _problem_name_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.PreProblemNameValidator]
        ] = []
        _problem_name_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.ProblemNameValidator]
        ] = []
        _problem_description_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.PreProblemDescriptionValidator]
        ] = []
        _problem_description_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.ProblemDescriptionValidator]
        ] = []
        _files_pre_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators.PreFilesValidator]] = []
        _files_post_validators: typing.ClassVar[typing.List[CreateProblemRequest.Validators.FilesValidator]] = []
        _input_params_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.PreInputParamsValidator]
        ] = []
        _input_params_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.InputParamsValidator]
        ] = []
        _output_type_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.PreOutputTypeValidator]
        ] = []
        _output_type_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.OutputTypeValidator]
        ] = []
        _testcases_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.PreTestcasesValidator]
        ] = []
        _testcases_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.TestcasesValidator]
        ] = []
        _method_name_pre_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.PreMethodNameValidator]
        ] = []
        _method_name_post_validators: typing.ClassVar[
            typing.List[CreateProblemRequest.Validators.MethodNameValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequest.Validators._RootValidator], CreateProblemRequest.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators._PreRootValidator], CreateProblemRequest.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["problem_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.PreProblemNameValidator],
            CreateProblemRequest.Validators.PreProblemNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.ProblemNameValidator], CreateProblemRequest.Validators.ProblemNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_description"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.PreProblemDescriptionValidator],
            CreateProblemRequest.Validators.PreProblemDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["problem_description"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.ProblemDescriptionValidator],
            CreateProblemRequest.Validators.ProblemDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.PreFilesValidator], CreateProblemRequest.Validators.PreFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.FilesValidator], CreateProblemRequest.Validators.FilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["input_params"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.PreInputParamsValidator],
            CreateProblemRequest.Validators.PreInputParamsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["input_params"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.InputParamsValidator], CreateProblemRequest.Validators.InputParamsValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["output_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.PreOutputTypeValidator],
            CreateProblemRequest.Validators.PreOutputTypeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["output_type"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.OutputTypeValidator], CreateProblemRequest.Validators.OutputTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.PreTestcasesValidator],
            CreateProblemRequest.Validators.PreTestcasesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.TestcasesValidator], CreateProblemRequest.Validators.TestcasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.PreMethodNameValidator],
            CreateProblemRequest.Validators.PreMethodNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateProblemRequest.Validators.MethodNameValidator], CreateProblemRequest.Validators.MethodNameValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_name":
                    if pre:
                        cls._problem_name_pre_validators.append(validator)
                    else:
                        cls._problem_name_post_validators.append(validator)
                if field_name == "problem_description":
                    if pre:
                        cls._problem_description_pre_validators.append(validator)
                    else:
                        cls._problem_description_post_validators.append(validator)
                if field_name == "files":
                    if pre:
                        cls._files_pre_validators.append(validator)
                    else:
                        cls._files_post_validators.append(validator)
                if field_name == "input_params":
                    if pre:
                        cls._input_params_pre_validators.append(validator)
                    else:
                        cls._input_params_post_validators.append(validator)
                if field_name == "output_type":
                    if pre:
                        cls._output_type_pre_validators.append(validator)
                    else:
                        cls._output_type_post_validators.append(validator)
                if field_name == "testcases":
                    if pre:
                        cls._testcases_pre_validators.append(validator)
                    else:
                        cls._testcases_post_validators.append(validator)
                if field_name == "method_name":
                    if pre:
                        cls._method_name_pre_validators.append(validator)
                    else:
                        cls._method_name_post_validators.append(validator)
                return validator

            return decorator

        class PreProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequest.Partial) -> typing.Any:
                ...

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: CreateProblemRequest.Partial) -> str:
                ...

        class PreProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequest.Partial) -> typing.Any:
                ...

        class ProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemDescription, __values: CreateProblemRequest.Partial) -> ProblemDescription:
                ...

        class PreFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequest.Partial) -> typing.Any:
                ...

        class FilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, ProblemFiles], __values: CreateProblemRequest.Partial
            ) -> typing.Dict[Language, ProblemFiles]:
                ...

        class PreInputParamsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequest.Partial) -> typing.Any:
                ...

        class InputParamsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[VariableTypeAndName], __values: CreateProblemRequest.Partial
            ) -> typing.List[VariableTypeAndName]:
                ...

        class PreOutputTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequest.Partial) -> typing.Any:
                ...

        class OutputTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: CreateProblemRequest.Partial) -> VariableType:
                ...

        class PreTestcasesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequest.Partial) -> typing.Any:
                ...

        class TestcasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCaseWithExpectedResult], __values: CreateProblemRequest.Partial
            ) -> typing.List[TestCaseWithExpectedResult]:
                ...

        class PreMethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateProblemRequest.Partial) -> typing.Any:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: CreateProblemRequest.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: CreateProblemRequest.Partial) -> CreateProblemRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: CreateProblemRequest.Partial) -> CreateProblemRequest.Partial:
        for validator in CreateProblemRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: CreateProblemRequest.Partial) -> CreateProblemRequest.Partial:
        for validator in CreateProblemRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_name", pre=True)
    def _pre_validate_problem_name(cls, v: str, values: CreateProblemRequest.Partial) -> str:
        for validator in CreateProblemRequest.Validators._problem_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_name", pre=False)
    def _post_validate_problem_name(cls, v: str, values: CreateProblemRequest.Partial) -> str:
        for validator in CreateProblemRequest.Validators._problem_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_description", pre=True)
    def _pre_validate_problem_description(
        cls, v: ProblemDescription, values: CreateProblemRequest.Partial
    ) -> ProblemDescription:
        for validator in CreateProblemRequest.Validators._problem_description_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_description", pre=False)
    def _post_validate_problem_description(
        cls, v: ProblemDescription, values: CreateProblemRequest.Partial
    ) -> ProblemDescription:
        for validator in CreateProblemRequest.Validators._problem_description_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("files", pre=True)
    def _pre_validate_files(
        cls, v: typing.Dict[Language, ProblemFiles], values: CreateProblemRequest.Partial
    ) -> typing.Dict[Language, ProblemFiles]:
        for validator in CreateProblemRequest.Validators._files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("files", pre=False)
    def _post_validate_files(
        cls, v: typing.Dict[Language, ProblemFiles], values: CreateProblemRequest.Partial
    ) -> typing.Dict[Language, ProblemFiles]:
        for validator in CreateProblemRequest.Validators._files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("input_params", pre=True)
    def _pre_validate_input_params(
        cls, v: typing.List[VariableTypeAndName], values: CreateProblemRequest.Partial
    ) -> typing.List[VariableTypeAndName]:
        for validator in CreateProblemRequest.Validators._input_params_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("input_params", pre=False)
    def _post_validate_input_params(
        cls, v: typing.List[VariableTypeAndName], values: CreateProblemRequest.Partial
    ) -> typing.List[VariableTypeAndName]:
        for validator in CreateProblemRequest.Validators._input_params_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("output_type", pre=True)
    def _pre_validate_output_type(cls, v: VariableType, values: CreateProblemRequest.Partial) -> VariableType:
        for validator in CreateProblemRequest.Validators._output_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("output_type", pre=False)
    def _post_validate_output_type(cls, v: VariableType, values: CreateProblemRequest.Partial) -> VariableType:
        for validator in CreateProblemRequest.Validators._output_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("testcases", pre=True)
    def _pre_validate_testcases(
        cls, v: typing.List[TestCaseWithExpectedResult], values: CreateProblemRequest.Partial
    ) -> typing.List[TestCaseWithExpectedResult]:
        for validator in CreateProblemRequest.Validators._testcases_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("testcases", pre=False)
    def _post_validate_testcases(
        cls, v: typing.List[TestCaseWithExpectedResult], values: CreateProblemRequest.Partial
    ) -> typing.List[TestCaseWithExpectedResult]:
        for validator in CreateProblemRequest.Validators._testcases_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("method_name", pre=True)
    def _pre_validate_method_name(cls, v: str, values: CreateProblemRequest.Partial) -> str:
        for validator in CreateProblemRequest.Validators._method_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("method_name", pre=False)
    def _post_validate_method_name(cls, v: str, values: CreateProblemRequest.Partial) -> str:
        for validator in CreateProblemRequest.Validators._method_name_post_validators:
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
