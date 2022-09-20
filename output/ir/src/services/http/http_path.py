import typing

import pydantic

from .http_path_part import HttpPathPart


class HttpPath(pydantic.BaseModel):
    head: int
    parts: typing.List[HttpPathPart]
