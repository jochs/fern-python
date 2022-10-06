import typing

import pydantic
import typing_extensions

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

    @pydantic.validator("problem_name")
    def _validate_problem_name(cls, problem_name: str) -> str:
        for validator in CreateProblemRequest.Validators._problem_name:
            problem_name = validator(problem_name)
        return problem_name

    @pydantic.validator("problem_description")
    def _validate_problem_description(cls, problem_description: ProblemDescription) -> ProblemDescription:
        for validator in CreateProblemRequest.Validators._problem_description:
            problem_description = validator(problem_description)
        return problem_description

    @pydantic.validator("files")
    def _validate_files(cls, files: typing.Dict[Language, ProblemFiles]) -> typing.Dict[Language, ProblemFiles]:
        for validator in CreateProblemRequest.Validators._files:
            files = validator(files)
        return files

    @pydantic.validator("input_params")
    def _validate_input_params(cls, input_params: typing.List[VariableTypeAndName]) -> typing.List[VariableTypeAndName]:
        for validator in CreateProblemRequest.Validators._input_params:
            input_params = validator(input_params)
        return input_params

    @pydantic.validator("output_type")
    def _validate_output_type(cls, output_type: VariableType) -> VariableType:
        for validator in CreateProblemRequest.Validators._output_type:
            output_type = validator(output_type)
        return output_type

    @pydantic.validator("testcases")
    def _validate_testcases(
        cls, testcases: typing.List[TestCaseWithExpectedResult]
    ) -> typing.List[TestCaseWithExpectedResult]:
        for validator in CreateProblemRequest.Validators._testcases:
            testcases = validator(testcases)
        return testcases

    @pydantic.validator("method_name")
    def _validate_method_name(cls, method_name: str) -> str:
        for validator in CreateProblemRequest.Validators._method_name:
            method_name = validator(method_name)
        return method_name

    class Validators:
        _problem_name: typing.ClassVar[str] = []
        _problem_description: typing.ClassVar[ProblemDescription] = []
        _files: typing.ClassVar[typing.Dict[Language, ProblemFiles]] = []
        _input_params: typing.ClassVar[typing.List[VariableTypeAndName]] = []
        _output_type: typing.ClassVar[VariableType] = []
        _testcases: typing.ClassVar[typing.List[TestCaseWithExpectedResult]] = []
        _method_name: typing.ClassVar[str] = []

        @typing.overload
        @classmethod
        def field(problem_name: typing_extensions.Literal["problem_name"]) -> str:
            ...

        @typing.overload
        @classmethod
        def field(problem_description: typing_extensions.Literal["problem_description"]) -> ProblemDescription:
            ...

        @typing.overload
        @classmethod
        def field(files: typing_extensions.Literal["files"]) -> typing.Dict[Language, ProblemFiles]:
            ...

        @typing.overload
        @classmethod
        def field(input_params: typing_extensions.Literal["input_params"]) -> typing.List[VariableTypeAndName]:
            ...

        @typing.overload
        @classmethod
        def field(output_type: typing_extensions.Literal["output_type"]) -> VariableType:
            ...

        @typing.overload
        @classmethod
        def field(testcases: typing_extensions.Literal["testcases"]) -> typing.List[TestCaseWithExpectedResult]:
            ...

        @typing.overload
        @classmethod
        def field(method_name: typing_extensions.Literal["method_name"]) -> str:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_name":
                    cls._problem_name.append(validator)  # type: ignore
                elif field_name == "problem_description":
                    cls._problem_description.append(validator)  # type: ignore
                elif field_name == "files":
                    cls._files.append(validator)  # type: ignore
                elif field_name == "input_params":
                    cls._input_params.append(validator)  # type: ignore
                elif field_name == "output_type":
                    cls._output_type.append(validator)  # type: ignore
                elif field_name == "testcases":
                    cls._testcases.append(validator)  # type: ignore
                elif field_name == "method_name":
                    cls._method_name.append(validator)  # type: ignore
                else:
                    raise RuntimeError("Field does not exist on CreateProblemRequest: " + field_name)

                return validator

            return validator  # type: ignore

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
