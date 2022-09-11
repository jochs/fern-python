from __future__ import annotations

import typing
from abc import ABC, abstractmethod

import pydantic
import typing_extensions

from ..logging.task_id import TaskId
from .remote_generator_environment import RemoteGeneratorEnvironment

_Result = typing.TypeVar("_Result")


class _GeneratorEnvironment:
    class Local(pydantic.BaseModel):
        type: typing.Literal["local"]

    class Remote(RemoteGeneratorEnvironment):
        type: typing.Literal["remote"]


class GeneratorEnvironment(pydantic.BaseModel):
    @staticmethod
    def local() -> GeneratorEnvironment:
        return GeneratorEnvironment(__root__=_GeneratorEnvironment.Local(type="local"))

    @staticmethod
    def remote(coordinator_url: str, coordinator_url_v2: str, id: TaskId) -> GeneratorEnvironment:
        return GeneratorEnvironment(
            __root__=_GeneratorEnvironment.Remote(
                type="remote", coordinator_url=coordinator_url, coordinator_url_v2=coordinator_url_v2, id=id
            )
        )

    __root__: typing_extensions.Annotated[
        typing.Union[
            _GeneratorEnvironment.Local,
            _GeneratorEnvironment.Remote,
        ],
        pydantic.Field(discriminator="type"),
    ]

    class _Visitor(ABC, typing.Generic[_Result]):
        @abstractmethod
        def local(self) -> _Result:
            ...

        @abstractmethod
        def remote(self, value: RemoteGeneratorEnvironment) -> _Result:
            ...

    def _visit(self, visitor: _Visitor[_Result]) -> _Result:
        if self.__root__.type == "local":
            return visitor.local()
        if self.__root__.type == "remote":
            return visitor.remote(self.__root__)
