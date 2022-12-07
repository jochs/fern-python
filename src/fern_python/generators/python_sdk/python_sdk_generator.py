import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.cli.abstract_generator import AbstractGenerator
from fern_python.codegen import Project
from fern_python.generator_exec_wrapper import GeneratorExecWrapper
from fern_python.generators.pydantic_model import (
    PydanticModelCustomConfig,
    PydanticModelGenerator,
)


class PythonSdkGenerator(AbstractGenerator):
    def run(
        self,
        *,
        generator_exec_wrapper: GeneratorExecWrapper,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project: Project,
    ) -> None:

        PydanticModelGenerator().generate_types(
            generator_exec_wrapper=generator_exec_wrapper,
            custom_config=PydanticModelCustomConfig.parse_obj(
                {"wrapped_aliases": False, "forbid_extra_fields": False, "exclude_validators": True}
            ),
            ir=ir,
            project=project,
            context=context.pydantic_generator_context,
        )
