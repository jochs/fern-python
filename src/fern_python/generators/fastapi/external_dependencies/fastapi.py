from typing import List, Tuple

from fern_python.codegen import AST

FAST_API_MODULE = AST.Module.external(
    module_path=("fastapi",),
    dependency=AST.Dependency(
        name="fastapi",
        version="^0.79.0",
    ),
)


def _export(name: str) -> AST.ClassReference:
    return AST.ClassReference(
        qualified_name_excluding_import=(name,), import_=AST.ReferenceImport(module=FAST_API_MODULE)
    )


class APIRouter:

    TYPE = AST.TypeHint(type=_export("APIRouter"))

    @staticmethod
    def _invoke() -> AST.Expression:
        return AST.Expression(
            AST.FunctionInvocation(
                function_definition=_export("APIRouter"),
                args=[AST.Expression(AST.CodeWriter("..."))],
            )
        )


class FastAPI:
    Body = AST.Expression(
        AST.FunctionInvocation(
            function_definition=_export("Body"),
            args=[AST.Expression(AST.CodeWriter("..."))],
        )
    )

    Path = AST.Expression(
        AST.FunctionInvocation(
            function_definition=_export("Path"),
            args=[AST.Expression(AST.CodeWriter("..."))],
        )
    )

    APIRouter = APIRouter

    @staticmethod
    def Query(*, is_optional: bool, variable_name: str, wire_value: str) -> AST.Expression:
        kwargs: List[Tuple[str, AST.Expression]] = []
        if is_optional:
            kwargs.append(("default", AST.Expression(AST.TypeHint.none())))
        if variable_name != wire_value:
            kwargs.append(("alias", AST.Expression(AST.CodeWriter(f'"{wire_value}"'))))
        return AST.Expression(AST.FunctionInvocation(function_definition=_export("Query"), kwargs=kwargs))
