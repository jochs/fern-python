from abc import ABC, abstractmethod

import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.codegen import Filepath
from fern_python.generators.pydantic_model import PydanticGeneratorContextImpl

from ..declaration_referencers import TypeDeclarationReferencer


class FastApiGeneratorContext(ABC):
    def __init__(self, ir: ir_types.IntermediateRepresentation, generator_config: GeneratorConfig):
        self._ir = ir
        self._generator_config = generator_config
        self.pydantic_generator_context = PydanticGeneratorContextImpl(
            intermediate_representation=ir,
            type_declaration_referencer=TypeDeclarationReferencer(
                generator_config=generator_config,
                ir=ir,
            ),
        )

    @abstractmethod
    def get_filepath_for_service(self, service_name: ir_types.services.DeclaredServiceName) -> Filepath:
        ...
