import typing

import pydantic
from services.websocket.web_socket_operation import WebSocketOperation


class WebSocketMessenger(pydantic.BaseModel):

    operations: typing.List[WebSocketOperation]
