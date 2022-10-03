import typing

import pydantic

from .http_path_part import HttpPathPart


class HttpPath(pydantic.BaseModel):
    head: str
    parts: typing.List[HttpPathPart]

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)
