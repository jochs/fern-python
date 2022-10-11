from typing import Sequence

from fern_python.codegen import AST
from fern_python.pydantic_codegen import PydanticModel

from .validator_generators import FieldValidatorGenerator, ValidatorGenerator
from .validators_generator import ValidatorsGenerator


class PydanticValidatorsGenerator(ValidatorsGenerator):
    def __init__(self, model: PydanticModel):
        super().__init__(model=model)
        self._validator_generators = [
            FieldValidatorGenerator(
                field=field,
                model=self._model,
                reference_to_validators_class=self._get_reference_to_validators_class(),
            )
            for field in model.get_public_fields()
        ]

    def _populate_validators_class(self, validators_class: AST.ClassDeclaration) -> None:
        self._add_field_validators_to_validators_class(validators_class=validators_class)

    def _add_field_validators_to_validators_class(self, validators_class: AST.ClassDeclaration) -> None:
        if len(self._validator_generators) == 0:
            return

        for generator in self._validator_generators:
            validators_class.add_class_var(generator.get_class_var_for_validators_class())

        validators_class.add_method(
            decorator=AST.ClassMethodDecorator.CLASS_METHOD,
            declaration=AST.FunctionDeclaration(
                name="field",
                signature=AST.FunctionSignature(
                    parameters=[
                        AST.FunctionParameter(
                            name=FieldValidatorGenerator._DECORATOR_FIELD_NAME_ARGUMENT,
                            type_hint=AST.TypeHint.str_(),
                        )
                    ],
                    return_type=AST.TypeHint.any(),
                ),
                body=AST.CodeWriter(self._write_add_field_validator_body),
                overloads=[generator.get_overload_for_validators_class() for generator in self._validator_generators],
            ),
        )

    def _write_add_field_validator_body(
        self,
        writer: AST.NodeWriter,
        reference_resolver: AST.ReferenceResolver,
    ) -> None:
        DECORATOR_FUNCTION_NAME = "decorator"

        def write_decorator_body(
            writer: AST.NodeWriter,
            reference_resolver: AST.ReferenceResolver,
        ) -> None:
            for i, generator in enumerate(self._validator_generators):
                writer.write("if" if i == 0 else "elif")
                writer.write(f" {FieldValidatorGenerator._DECORATOR_FIELD_NAME_ARGUMENT} == ")
                writer.write(f'"{generator.field.name}":')
                writer.write_line()
                with writer.indent():
                    append_statement = AST.FunctionInvocation(
                        function_definition=AST.Reference(
                            qualified_name_excluding_import=(
                                "cls",
                                generator.get_validator_class_var(),
                                "append",
                            )
                        ),
                        args=[AST.Expression(FieldValidatorGenerator._VALIDATOR_PARAMETER_NAME)],
                    )
                    writer.write_node(append_statement)
                writer.write_line()
            writer.write_line("else:")
            with writer.indent():
                writer.write(f'raise RuntimeError("Field does not exist on {self._model.name}: " + ')
                writer.write(FieldValidatorGenerator._DECORATOR_FIELD_NAME_ARGUMENT)
                writer.write_line(")")
                writer.write_line()
            writer.write(f"return {FieldValidatorGenerator._VALIDATOR_PARAMETER_NAME}")

        decorator = AST.FunctionDeclaration(
            name=DECORATOR_FUNCTION_NAME,
            signature=AST.FunctionSignature(
                parameters=[AST.FunctionParameter(name="validator", type_hint=AST.TypeHint.any())],
                return_type=AST.TypeHint.any(),
            ),
            body=AST.CodeWriter(write_decorator_body),
        )

        writer.write_node(decorator)
        writer.write(f"return {DECORATOR_FUNCTION_NAME}")

    def _get_validator_generators(self) -> Sequence[ValidatorGenerator]:
        return self._validator_generators
