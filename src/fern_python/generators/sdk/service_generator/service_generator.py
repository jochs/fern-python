import fern.ir.pydantic as ir_types

from fern_python.codegen import AST, SourceFile

from ..context.sdk_generator_context import SdkGeneratorContext


class ServiceGenerator:
    ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME = "environment"
    ENVIRONMENT_MEMBER_NAME = "_environment"

    def __init__(self, context: SdkGeneratorContext, package: ir_types.Package, class_name: str):
        self._context = context
        self._package = package
        self._class_name = class_name

    def generate(self, source_file: SourceFile) -> None:
        source_file.add_class_declaration(
            declaration=AST.ClassDeclaration(
                name=self._class_name,
                constructor=AST.ClassConstructor(
                    signature=AST.FunctionSignature(
                        parameters=[
                            AST.FunctionParameter(
                                name=ServiceGenerator.ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME,
                                type_hint=AST.TypeHint(self._context.get_reference_to_environments_enum())
                                if self._context.ir.environments is not None
                                else AST.TypeHint.str_(),
                            ),
                        ]
                    ),
                    body=AST.CodeWriter(self._write_constructor_body),
                ),
            ),
            should_export=False,
        )

    def _write_constructor_body(self, writer: AST.NodeWriter) -> None:
        writer.write_line("...")
