from enum import Enum
from typing import List, Optional, Tuple

from fern_python.codegen import AST

REQUESTS_MODULE = AST.Module.built_in(
    ("requests",),
    types_package=AST.Dependency(
        name="types-requests",
        version="2.28.11.16",
    ),
)


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class Requests:
    @staticmethod
    def make_request(
        *,
        method: HttpMethod,
        query_parameters: List[Tuple[str, AST.Expression]],
        request_body: Optional[AST.Expression],
        response_variable_name: str,
    ) -> AST.Expression:
        def write(writer: AST.NodeWriter) -> None:
            writer.write(f"{response_variable_name} = ")
            writer.write_reference(
                AST.ClassReference(
                    qualified_name_excluding_import=(), import_=AST.ReferenceImport(module=REQUESTS_MODULE)
                )
            )
            writer.write_line(f'.request("{method.value}", "",')
            with writer.indent():
                if len(query_parameters) > 0:
                    writer.write("params={")

                    for i, (query_parameter_key, query_parameter_value) in enumerate(query_parameters):
                        if i > 0:
                            writer.write(", ")
                        writer.write(f'"{query_parameter_key}": ')
                        writer.write_node(query_parameter_value)

                    writer.write_line("}")

                if request_body is not None:
                    writer.write("json=")
                    writer.write_node(request_body)
                    writer.write_line()
            writer.write_line(")")

        return AST.Expression(AST.CodeWriter(write))
