from fern_python.codegen import AST, SourceFile
from fern_python.generated import ir_types

VISITOR_RESULT_TYPE_VAR = "T_Result"


def generate_enum(name: ir_types.DeclaredTypeName, enum: ir_types.EnumTypeDeclaration, source_file: SourceFile) -> None:
    source_file.add_declaration(
        AST.VariableDeclaration(
            name=VISITOR_RESULT_TYPE_VAR,
            initializer=AST.FunctionInvocation(
                function_definition=AST.Reference(
                    import_=AST.ReferenceImport(module=("typing",)),
                    qualified_name_excluding_import=("TypeVar",),
                ),
                args=[AST.CodeWriter(f'"{VISITOR_RESULT_TYPE_VAR}"')],
            ),
        ),
    )

    enum_class = AST.ClassDeclaration(
        name=name.name,
        extends=[
            AST.ClassReference(
                qualified_name_excluding_import=("str",),
            ),
            AST.ClassReference(
                import_=AST.ReferenceImport(module=("enum",)),
                qualified_name_excluding_import=("Enum",),
            ),
        ],
    )

    source_file.add_declaration(enum_class)

    for value in enum.values:
        enum_class.add_attribute(
            AST.VariableDeclaration(name=value.name.snake_case, initializer=AST.CodeWriter(f'"{value.value}"'))
        )
