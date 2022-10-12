from fern_python.codegen import AST
from ..external_dependencies import FastAPI


class ExceptionHandlerGenerator:
    def generate(
        self,
        *,
        exception_handler_name: str,
        app_variable: str,
        exception_cls: AST.ClassReference,
        write_return_statement: AST.CodeWriter,
    ) -> AST.FunctionDeclaration:
        def write_body(writer: AST.NodeWriter) -> None:
            writer.write(f"{FastAPI.EXCEPTION_HANDLER_REQUEST_ARGUMENT}.state.logger.info(")
            writer.write(f'f"{{{FastAPI.EXCEPTION_HANDLER_EXCEPTION_ARGUMENT}.__class__.__name__}} in ')
            writer.write(f'{{{FastAPI.EXCEPTION_HANDLER_REQUEST_ARGUMENT}.url.path}}", ')
            writer.write_line(f"exc_info={FastAPI.EXCEPTION_HANDLER_EXCEPTION_ARGUMENT})")

            writer.write("return ")
            writer.write_node(write_return_statement)
            writer.write_line()

        return FastAPI.exception_handler(
            exception_handler_name=exception_handler_name,
            app_variable=app_variable,
            exception_type=exception_cls,
            body=AST.CodeWriter(write_body),
        )
