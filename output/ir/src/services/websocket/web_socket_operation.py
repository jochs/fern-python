from commons.wire_string_with_all_casings import WireStringWithAllCasings
from commons.with_docs import WithDocs
from services.commons.response_errors import ResponseErrors
from services.websocket.web_socket_request import WebSocketRequest
from services.websocket.web_socket_response import WebSocketResponse


class WebSocketOperation(WithDocs):

    name: WireStringWithAllCasings
    request: WebSocketRequest
    response: WebSocketResponse
    errors: ResponseErrors
