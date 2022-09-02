from __future__ import annotations
import pydantic
from .map_type import MapType
import typing
from abc import ABC, abstractmethod

_Result = typing.TypeVar("_Result")


class _ContainerType:
    class List(pydantic.BaseModel):
        type: typing.Literal["list"]
        list: TypeReference

    class Map(MapType):
        type: typing.Literal["map"]

    class Optional(pydantic.BaseModel):
        type: typing.Literal["optional"]
        optional: TypeReference

    class Set(pydantic.BaseModel):
        type: typing.Literal["set"]
        set: TypeReference

    class _Unknown(pydantic.BaseModel, extra=pydantic.Extra.allow):
        type: str


class ContainerType(pydantic.BaseModel):
    @staticmethod
    def list(value: TypeReference) -> ContainerType:
        return ContainerType(__root__=_ContainerType.List(type="list", list=value))

    @staticmethod
    def map(value: MapType) -> ContainerType:
        return ContainerType(
            __root__=_ContainerType.Map(type="map", key_type=value.key_type, value_type=value.value_type)
        )

    @staticmethod
    def optional(value: TypeReference) -> ContainerType:
        return ContainerType(__root__=_ContainerType.Optional(type="optional", optional=value))

    @staticmethod
    def set(value: TypeReference) -> ContainerType:
        return ContainerType(__root__=_ContainerType.Set(type="set", set=value))

    class _Visitor(ABC, typing.Generic[_Result]):
        @abstractmethod
        def list(self, value: TypeReference) -> _Result:
            ...

        @abstractmethod
        def map(self, value: MapType) -> _Result:
            ...

        @abstractmethod
        def optional(self, value: TypeReference) -> _Result:
            ...

        @abstractmethod
        def set(self, value: TypeReference) -> _Result:
            ...

        @abstractmethod
        def _unknown(self) -> _Result:
            ...

    def _visit(self, visitor: _Visitor[_Result]) -> _Result:
        if self.__root__.type == "list":
            return visitor.list(typing.cast(_ContainerType.List, self.__root__).list)
        if self.__root__.type == "map":
            return visitor.map(typing.cast(_ContainerType.Map, self.__root__))
        if self.__root__.type == "optional":
            return visitor.optional(typing.cast(_ContainerType.Optional, self.__root__).optional)
        if self.__root__.type == "set":
            return visitor.set(typing.cast(_ContainerType.Set, self.__root__).set)
        return visitor._unknown()

    __root__: typing.Union[
        _ContainerType.List, _ContainerType.Map, _ContainerType.Optional, _ContainerType.Set, _ContainerType._Unknown
    ]


from .type_reference import TypeReference  # noqa E402

_ContainerType.List.update_forward_refs()
_ContainerType.Map.update_forward_refs()
_ContainerType.Optional.update_forward_refs()
_ContainerType.Set.update_forward_refs()