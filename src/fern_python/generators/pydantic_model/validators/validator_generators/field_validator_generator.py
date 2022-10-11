from fern_python.codegen import AST
from fern_python.pydantic_codegen import PydanticField, PydanticModel

from .validator_generator import ValidatorGenerator


class FieldValidatorGenerator(ValidatorGenerator):
    _DECORATOR_FIELD_NAME_ARGUMENT = "field_name"
    _VALIDATOR_PARAMETER_NAME = "validator"

    def __init__(self, field: PydanticField, model: PydanticModel, reference_to_validators_class: AST.ClassReference):
        super().__init__(model=model, reference_to_validators_class=reference_to_validators_class)
        self.field = field

    def add_validator_to_model(self) -> None:
        self._model.add_field_validator(
            validator_name=f"_validate_{self.field.name}",
            field_name=self.field.name,
            field_parameter_name=self._get_validator_parameter_name(),
            field_type=self.field.type_hint,
            body=AST.CodeWriter(self._write_validator_body),
        )

    def _get_validator_parameter_name(self) -> str:
        return self.field.name

    def get_validator_class_var(self) -> str:
        return f"_{self.field.name}_validators"

    def _write_validator_body(self, writer: AST.NodeWriter, reference_resolver: AST.ReferenceResolver) -> None:
        parameter_name = self._get_validator_parameter_name()

        INDIVIDUAL_VALIDATOR_NAME = "validator"
        writer.write(f"for {INDIVIDUAL_VALIDATOR_NAME} in ")
        writer.write_node(AST.ReferenceNode(self._reference_to_validators_class))
        writer.write_line(f".{self.get_validator_class_var()}:")

        with writer.indent():
            writer.write(f"{parameter_name} = ")
            writer.write_node(
                AST.FunctionInvocation(
                    function_definition=AST.Reference(
                        qualified_name_excluding_import=(INDIVIDUAL_VALIDATOR_NAME,),
                    ),
                    args=[AST.Expression(parameter_name)],
                )
            )
            writer.write_line()
        writer.write_line(f"return {parameter_name}")

    def get_class_var_for_validators_class(self) -> AST.VariableDeclaration:
        return AST.VariableDeclaration(
            name=self.get_validator_class_var(),
            type_hint=AST.TypeHint.class_var(AST.TypeHint.list(self._get_type_of_validator())),
            initializer=AST.Expression("[]"),
        )

    def get_overload_for_validators_class(self) -> AST.FunctionSignature:
        return AST.FunctionSignature(
            parameters=[
                AST.FunctionParameter(
                    name=FieldValidatorGenerator._DECORATOR_FIELD_NAME_ARGUMENT,
                    type_hint=AST.TypeHint.literal(AST.Expression(f'"{self.field.name}"')),
                )
            ],
            return_type=AST.TypeHint.callable([self._get_type_of_validator()], self._get_type_of_validator()),
        )

    def _get_type_of_validator(self) -> AST.TypeHint:
        return AST.TypeHint.callable([self.field.type_hint], self.field.type_hint)
