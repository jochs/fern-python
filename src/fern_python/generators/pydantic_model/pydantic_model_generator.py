from typing import Optional

from generator_exec.resources.config import GeneratorConfig, GeneratorPublishConfig
from generator_exec.resources.logging import GeneratorUpdate, LogLevel, LogUpdate

from ...cli.abstract_generator import AbstractGenerator
from ...codegen import Project
from ...generated import ir_types
from ...generator_exec_wrapper import GeneratorExecWrapper
from ...logger import Logger
from .context import DeclarationHandlerContextImpl
from .filepaths import get_filepath_for_type
from .type_declaration_handler import TypeDeclarationHandler


class LoggerImpl(Logger):
    def log(self, content: str) -> None:
        print(content)


class PydanticModelGenerator(AbstractGenerator):
    def __init__(self) -> None:
        self._logger = LoggerImpl()

    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        for type_to_generate in ir.types:
            self._generate_type(project, ir=ir, type=type_to_generate, generator_exec_wrapper=generator_exec_wrapper)

    def _generate_type(
        self,
        project: Project,
        ir: ir_types.IntermediateRepresentation,
        type: ir_types.TypeDeclaration,
        generator_exec_wrapper: GeneratorExecWrapper,
    ) -> None:
        filepath = filepath = get_filepath_for_type(
            type_name=type.name,
            api_name=ir.api_name,
        )
        with project.source_file(filepath=filepath) as source_file:
            context = DeclarationHandlerContextImpl(
                source_file=source_file,
                intermediate_representation=ir,
            )
            type_declaration_handler = TypeDeclarationHandler(
                declaration=type,
                context=context,
                logger=self._logger,
            )
            type_declaration_handler.run()
            generator_exec_wrapper.send_update(
                GeneratorUpdate.factory.log(
                    LogUpdate(level=LogLevel.DEBUG, message=f"Generated file {filepath.to_str()}")
                )
            )

    def get_package_to_publish(
        self,
        *,
        generator_config: GeneratorConfig,
    ) -> Optional[str]:
        return generator_config.output.mode.visit(
            publish=lambda generator_publish_config: self._get_published_package_name(generator_publish_config),
            download_files=lambda: None,
        )

    def _get_published_package_name(self, generator_publish_config: GeneratorPublishConfig) -> str:
        return generator_publish_config.registries_v_2.pypi.package_name
