from typing import List, Optional

import fern.ir.pydantic as ir_types
from typing_extensions import Never

from fern_python.codegen import AST, SourceFile
from fern_python.external_dependencies import HttpMethod, Pydantic, Requests

from ..context.sdk_generator_context import SdkGeneratorContext
from .abstract_request_body_parameters import AbstractRequestBodyParameters
from .inlined_request_body_parameters import InlinedRequestBodyParameters
from .referenced_request_body_parameters import ReferencedRequestBodyParameters


class ClientGenerator:
    ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME = "environment"
    ENVIRONMENT_MEMBER_NAME = "_environment"
    RESPONSE_VARIABLE = "_response"

    def __init__(self, context: SdkGeneratorContext, package: ir_types.Package, class_name: str):
        self._context = context
        self._package = package
        self._class_name = class_name

    def generate(self, source_file: SourceFile) -> None:
        class_declaration = AST.ClassDeclaration(
            name=self._class_name,
            constructor=AST.ClassConstructor(
                signature=AST.FunctionSignature(
                    named_parameters=[
                        AST.FunctionParameter(
                            name=ClientGenerator.ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME,
                            type_hint=AST.TypeHint(self._context.get_reference_to_environments_enum())
                            if self._context.ir.environments is not None
                            else AST.TypeHint.str_(),
                        ),
                    ]
                ),
                body=AST.CodeWriter(self._write_constructor_body),
            ),
        )

        if self._package.service is not None:
            service = self._context.ir.services[self._package.service]
            for endpoint in service.endpoints:
                request_body_parameters: Optional[AbstractRequestBodyParameters] = (
                    endpoint.request_body.visit(
                        inlined_request_body=lambda inlined_request_body: InlinedRequestBodyParameters(
                            endpoint=endpoint,
                            request_body=inlined_request_body,
                            context=self._context,
                        ),
                        reference=lambda referenced_request_body: ReferencedRequestBodyParameters(
                            endpoint=endpoint,
                            request_body=referenced_request_body,
                            context=self._context,
                        ),
                        file_upload=raise_file_upload_not_supported,
                    )
                    if endpoint.request_body is not None
                    else None
                )
                class_declaration.add_method(
                    AST.FunctionDeclaration(
                        name=endpoint.name.get_as_name().snake_case.unsafe_name,
                        signature=AST.FunctionSignature(
                            named_parameters=self._get_endpoint_parameters(service=service, endpoint=endpoint),
                            return_type=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                                endpoint.response.response_body_type
                            )
                            if endpoint.response is not None
                            else AST.TypeHint.none(),
                        ),
                        body=self._create_endpoint_body_writer(
                            endpoint=endpoint, request_body_parameters=request_body_parameters
                        ),
                    )
                )

        source_file.add_class_declaration(
            declaration=class_declaration,
            should_export=False,
        )

    def _write_constructor_body(self, writer: AST.NodeWriter) -> None:
        self._context.ir.services
        writer.write_line("...")

    def _get_endpoint_parameters(
        self,
        *,
        service: ir_types.HttpService,
        endpoint: ir_types.HttpEndpoint,
    ) -> List[AST.FunctionParameter]:
        parameters: List[AST.FunctionParameter] = []

        for path_parameter in service.path_parameters + endpoint.path_parameters:
            parameters.append(
                AST.FunctionParameter(
                    name=self._get_path_parameter_name(path_parameter),
                    type_hint=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                        path_parameter.value_type
                    ),
                ),
            )

        for query_parameter in endpoint.query_parameters:
            parameters.append(
                AST.FunctionParameter(
                    name=self._get_query_parameter_name(query_parameter),
                    type_hint=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                        query_parameter.value_type
                    ),
                ),
            )

        if endpoint.request_body is not None:
            parameters.extend(
                endpoint.request_body.visit(
                    inlined_request_body=self._get_parameters_for_inlined_request_body,
                    reference=lambda reference: self._get_parameters_for_referenced_request_body(
                        endpoint=endpoint,
                        referenced_request_body=reference,
                    ),
                    file_upload=raise_file_upload_not_supported,
                )
            )
        return parameters

    def _get_path_parameter_name(self, path_parameter: ir_types.PathParameter) -> str:
        return path_parameter.name.snake_case.unsafe_name

    def _get_query_parameter_name(self, query_parameter: ir_types.QueryParameter) -> str:
        return query_parameter.name.name.snake_case.unsafe_name

    def _create_endpoint_body_writer(
        self,
        *,
        endpoint: ir_types.HttpEndpoint,
        request_body_parameters: Optional[AbstractRequestBodyParameters],
    ) -> AST.CodeWriter:
        def write(writer: AST.NodeWriter) -> None:
            writer.write_node(
                Requests.make_request(
                    method=endpoint.method.visit(
                        get=lambda: HttpMethod.GET,
                        post=lambda: HttpMethod.POST,
                        put=lambda: HttpMethod.PUT,
                        patch=lambda: HttpMethod.PATCH,
                        delete=lambda: HttpMethod.DELETE,
                    ),
                    query_parameters=[
                        (
                            query_parameter.name.wire_value,
                            AST.Expression(self._get_query_parameter_name(query_parameter)),
                        )
                        for query_parameter in endpoint.query_parameters
                    ],
                    request_body=request_body_parameters.get_reference_to_request_body()
                    if request_body_parameters is not None
                    else None,
                    response_variable_name=ClientGenerator.RESPONSE_VARIABLE,
                )
            )
            if endpoint.response is not None:
                writer.write("return ")
                writer.write_node(
                    Pydantic.parse_obj_as(
                        self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                            endpoint.response.response_body_type
                        ),
                        AST.Expression(ClientGenerator.RESPONSE_VARIABLE),
                    )
                )

        return AST.CodeWriter(write)

    def _get_parameters_for_inlined_request_body(
        self, inlined_request_body: ir_types.InlinedRequestBody
    ) -> List[AST.FunctionParameter]:
        parameters: List[AST.FunctionParameter] = []
        for property in self._get_all_properties_for_inlined_request_body(inlined_request_body):
            parameters.append(
                AST.FunctionParameter(
                    name=property.name.name.snake_case.unsafe_name,
                    type_hint=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                        property.value_type
                    ),
                ),
            )
        return parameters

    def _get_all_properties_for_inlined_request_body(
        self, inlined_request_body: ir_types.InlinedRequestBody
    ) -> List[ir_types.InlinedRequestBodyProperty]:
        properties = inlined_request_body.properties.copy()
        for extension in inlined_request_body.extends:
            properties.extend(
                [
                    ir_types.InlinedRequestBodyProperty(
                        name=extended_property.name,
                        value_type=extended_property.value_type,
                        docs=extended_property.docs,
                    )
                    for extended_property in (
                        self._context.pydantic_generator_context.get_all_properties_including_extensions(extension)
                    )
                ]
            )
        return properties

    def _get_parameters_for_referenced_request_body(
        self,
        *,
        endpoint: ir_types.HttpEndpoint,
        referenced_request_body: ir_types.HttpRequestBodyReference,
    ) -> List[AST.FunctionParameter]:
        if endpoint.sdk_request is None:
            raise RuntimeError("Request body is referenced by SDKRequestBody is not defined")
        return [
            AST.FunctionParameter(
                name=endpoint.sdk_request.request_parameter_name.snake_case.unsafe_name,
                type_hint=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                    referenced_request_body.request_body_type
                ),
            )
        ]


def raise_file_upload_not_supported(request: ir_types.FileUploadRequest) -> Never:
    raise RuntimeError("File upload is not supported")
