import typing

import pydantic


class FileInfo(pydantic.BaseModel):
    filename: str
    contents: str

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)
