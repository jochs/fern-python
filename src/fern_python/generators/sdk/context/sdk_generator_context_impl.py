import fern.ir.pydantic as ir_types
from generator_exec.resources import GeneratorConfig

from fern_python.codegen.filepath import Filepath

from ..declaration_referencers.environments_enum_declaration_referencer import (
    EnvironmentsEnumDeclarationReferencer,
)
from ..declaration_referencers.error_declaration_referencer import (
    ErrorDeclarationReferencer,
)
from .sdk_generator_context import SdkGeneratorContext


class SDkGeneratorContextImpl(SdkGeneratorContext):
    def __init__(
        self,
        *,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        client_class_name: str,
    ):
        super().__init__(ir=ir, generator_config=generator_config)
        self._error_declaration_handler = ErrorDeclarationReferencer(filepath_creator=self.filepath_creator)
        self._environments_enum_declaration_referencer = EnvironmentsEnumDeclarationReferencer(
            filepath_creator=self.filepath_creator, client_class_name=client_class_name
        )

    def get_filepath_for_error(self, error_name: ir_types.DeclaredErrorName) -> Filepath:
        return self._error_declaration_handler.get_filepath(name=error_name)

    def get_class_name_for_error(self, error_name: ir_types.DeclaredErrorName) -> str:
        return self._error_declaration_handler.get_class_name(name=error_name)

    def get_filepath_for_environments_enum(self) -> Filepath:
        return self._environments_enum_declaration_referencer.get_filepath(name=None)
