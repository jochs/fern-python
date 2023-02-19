import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from .sdk_generator_context import SdkGeneratorContext


class SDkGeneratorContextImpl(SdkGeneratorContext):
    def __init__(
        self,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
    ):
        super().__init__(ir=ir, generator_config=generator_config)
