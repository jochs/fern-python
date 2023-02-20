import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.codegen.filepath import Filepath

from ..type_declaration_handler.error_declaration_referencer import (
    ErrorDeclarationReferencer,
)
from .sdk_generator_context import SdkGeneratorContext


class SDkGeneratorContextImpl(SdkGeneratorContext):
    def __init__(
        self,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
    ):
        super().__init__(ir=ir, generator_config=generator_config)
        self._error_declaration_handler = ErrorDeclarationReferencer(filepath_creator=self.filepath_creator)

    def get_filepath_for_error(self, error_name: ir_types.DeclaredErrorName) -> Filepath:
        return self._error_declaration_handler.get_filepath(name=error_name)

    def get_class_name_for_error(self, error_name: ir_types.DeclaredErrorName) -> str:
        return self._error_declaration_handler.get_class_name(name=error_name)
