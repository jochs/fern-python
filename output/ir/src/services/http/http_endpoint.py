import typing

import pydantic
from commons.string_with_all_casings import StringWithAllCasings
from commons.with_docs import WithDocs
from services.commons.response_errors import ResponseErrors
from services.http.http_endpoint_id import HttpEndpointId
from services.http.http_header import HttpHeader
from services.http.http_method import HttpMethod
from services.http.http_path import HttpPath
from services.http.http_request import HttpRequest
from services.http.http_response import HttpResponse
from services.http.path_parameter import PathParameter
from services.http.query_parameter import QueryParameter


class HttpEndpoint(WithDocs):

    id: HttpEndpointId
    name: StringWithAllCasings
    method: HttpMethod
    headers: typing.List[HttpHeader]
    path: HttpPath
    path_parameters: typing.List[PathParameter] = pydantic.Field(alias="pathParameters")
    query_parameters: typing.List[QueryParameter] = pydantic.Field(alias="queryParameters")
    request: HttpRequest
    response: HttpResponse
    errors: ResponseErrors
    auth: int

    class Config:

        allow_population_by_field_name = True
