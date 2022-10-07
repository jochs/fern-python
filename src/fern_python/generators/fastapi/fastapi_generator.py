import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.cli.abstract_generator import AbstractGenerator
from fern_python.codegen import AST, Project
from fern_python.generator_exec_wrapper import GeneratorExecWrapper
from fern_python.generators.pydantic_model import (
    PydanticModelCustomConfig,
    PydanticModelGenerator,
)

from .context import FastApiGeneratorContext, FastApiGeneratorContextImpl


class FastApiGenerator(AbstractGenerator):
    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:
        context = FastApiGeneratorContextImpl(ir=ir, generator_config=generator_config)
        PydanticModelGenerator().generate_types(
            generator_exec_wrapper=generator_exec_wrapper,
            custom_config=PydanticModelCustomConfig.parse_obj({}),
            ir=ir,
            project=project,
            context=context.pydantic_generator_context,
        )
        for service in ir.services.http:
            self._generate_service(
                context=context,
                ir=ir,
                generator_exec_wrapper=generator_exec_wrapper,
                service=service,
                project=project,
            )

    def _generate_service(
        self,
        context: FastApiGeneratorContext,
        ir: ir_types.IntermediateRepresentation,
        generator_exec_wrapper: GeneratorExecWrapper,
        service: ir_types.services.HttpService,
        project: Project,
    ) -> None:
        filepath = context.get_filepath_for_service(service.name)
        with self.source_file(
            project=project, filepath=filepath, generator_exec_wrapper=generator_exec_wrapper
        ) as source_file:
            source_file.add_arbitrary_code(AST.CodeWriter("print('hi')"))
