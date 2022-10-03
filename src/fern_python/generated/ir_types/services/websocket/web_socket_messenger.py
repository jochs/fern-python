import typing

import pydantic

from .web_socket_operation import WebSocketOperation


class WebSocketMessenger(pydantic.BaseModel):
    operations: typing.List[WebSocketOperation]

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)
