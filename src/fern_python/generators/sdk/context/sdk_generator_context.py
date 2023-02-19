from abc import ABC

import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.generators.pydantic_model import PydanticGeneratorContextImpl

from ..core_utilities.core_utilities import CoreUtilities
from ..sdk_filepath_creator import SdkFilepathCreator
from ..type_declaration_handler.type_declaration_referencer import (
    TypeDeclarationReferencer,
)


class SdkGeneratorContext(ABC):
    def __init__(
        self,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
    ):
        self.ir = ir
        self.generator_config = generator_config
        self.filepath_creator = SdkFilepathCreator(ir=ir, generator_config=generator_config)
        self.pydantic_generator_context = PydanticGeneratorContextImpl(
            ir=ir,
            type_declaration_referencer=TypeDeclarationReferencer(filepath_creator=self.filepath_creator),
            generator_config=generator_config,
        )
        self.core_utilities = CoreUtilities(filepath_creator=self.filepath_creator)
