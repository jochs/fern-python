import typing

from ...commons.with_docs import WithDocs
from ...types.type_reference import TypeReference


class WebSocketRequest(WithDocs):
    type: typing.Optional[TypeReference]

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)
