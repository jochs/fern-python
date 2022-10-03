import typing

import pydantic


class WithDocs(pydantic.BaseModel):
    docs: typing.Optional[str]

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)
