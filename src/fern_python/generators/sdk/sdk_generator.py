import fern.ir.pydantic as ir_types
from generator_exec.resources.config import GeneratorConfig

from fern_python.cli.abstract_generator import AbstractGenerator
from fern_python.codegen import Project
from fern_python.generator_exec_wrapper import GeneratorExecWrapper
from fern_python.generators.pydantic_model import (
    PydanticModelCustomConfig,
    PydanticModelGenerator,
)
from fern_python.generators.sdk.context.sdk_generator_context import SdkGeneratorContext
from fern_python.generators.sdk.context.sdk_generator_context_impl import (
    SDkGeneratorContextImpl,
)
from fern_python.source_file_generator import SourceFileGenerator

from .custom_config import SDKCustomConfig
from .environment_generator.environment_generator import EnvironmentGenerator
from .error_generator.error_generator import ErrorGenerator


class SdkGenerator(AbstractGenerator):
    def should_format_files(
        self,
        *,
        generator_config: GeneratorConfig,
    ) -> bool:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})
        return not custom_config.skip_formatting

    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        custom_config = SDKCustomConfig.parse_obj(generator_config.custom_config or {})
        self._pydantic_model_custom_config = PydanticModelCustomConfig(
            wrapped_aliases=custom_config.wrapped_aliases,
            skip_formatting=custom_config.skip_formatting,
        )

        context = SDkGeneratorContextImpl(
            ir=ir,
            generator_config=generator_config,
            client_class_name=custom_config.client_class_name
            or (pascalCase(generator_config.organization) + pascalCase(generator_config.workspace_name)),
        )

        PydanticModelGenerator().generate_types(
            generator_exec_wrapper=generator_exec_wrapper,
            custom_config=self._pydantic_model_custom_config,
            ir=ir,
            project=project,
            context=context.pydantic_generator_context,
        )

        if ir.environments is not None:
            self._generate_environments(
                context=context,
                environments=ir.environments.environments,
                generator_exec_wrapper=generator_exec_wrapper,
                project=project,
            )

        for service in ir.services.values():
            self._generate_service(
                context=context,
                ir=ir,
                generator_exec_wrapper=generator_exec_wrapper,
                service=service,
                project=project,
            )

        for error in ir.errors.values():
            self._generate_error(
                context=context,
                ir=ir,
                generator_exec_wrapper=generator_exec_wrapper,
                error=error,
                project=project,
            )

        context.core_utilities.copy_to_project(project=project)

    def _generate_environments(
        self,
        context: SdkGeneratorContext,
        environments: ir_types.Environments,
        generator_exec_wrapper: GeneratorExecWrapper,
        project: Project,
    ) -> None:
        filepath = context.get_filepath_for_environments_enum()
        with SourceFileGenerator.generate(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            EnvironmentGenerator(context=context, environments=environments).generate(source_file=source_file)

    def _generate_service(
        self,
        context: SdkGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generator_exec_wrapper: GeneratorExecWrapper,
        service: ir_types.HttpService,
        project: Project,
    ) -> None:
        pass

    def _generate_error(
        self,
        context: SdkGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generator_exec_wrapper: GeneratorExecWrapper,
        error: ir_types.ErrorDeclaration,
        project: Project,
    ) -> None:
        filepath = context.get_filepath_for_error(error.name)
        with SourceFileGenerator.generate(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            ErrorGenerator(context=context, error=error).generate(source_file=source_file)


def pascalCase(x: str) -> str:
    return "".join(char for char in x.title() if not x.isspace())
