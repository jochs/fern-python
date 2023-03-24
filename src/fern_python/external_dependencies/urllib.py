from fern_python.codegen import AST

STARLETTE_MODULE = AST.Module.built_in(("urllib",))


def _export(*name: str) -> AST.ClassReference:
    return AST.ClassReference(
        qualified_name_excluding_import=name, import_=AST.ReferenceImport(module=STARLETTE_MODULE)
    )


class UrlLib:
    @staticmethod
    def urljoin(base: AST.Expression, url: AST.Expression) -> AST.Expression:
        def write_base(writer: AST.NodeWriter) -> None:
            writer.write('f"{')
            writer.write_node(base)
            writer.write('}/"')

        return AST.Expression(
            AST.FunctionInvocation(
                function_definition=_export("parse", "urljoin"),
                args=[
                    AST.Expression(AST.CodeWriter(write_base)),
                    url,
                ],
            ),
        )
