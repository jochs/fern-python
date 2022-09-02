from __future__ import annotations
import pydantic
import typing
from abc import ABC, abstractmethod
from .declared_type_name import DeclaredTypeName
from .primitive_type import PrimitiveType


_Result = typing.TypeVar("_Result")


class _TypeReference:
    class Container(pydantic.BaseModel):
        type: typing.Literal["container"]
        container: ContainerType

    class Named(DeclaredTypeName):
        type: typing.Literal["named"]

    class Primitive(pydantic.BaseModel):
        type: typing.Literal["primitive"]
        primitive: PrimitiveType

    class Unknown(pydantic.BaseModel):
        type: typing.Literal["unknown"]

    class Void(pydantic.BaseModel):
        type: typing.Literal["void"]

    class _Unknown(pydantic.BaseModel, extra=pydantic.Extra.allow):
        type: str


class TypeReference(pydantic.BaseModel):
    @staticmethod
    def container(value: ContainerType) -> TypeReference:
        return TypeReference(__root__=_TypeReference.Container(type="container", container=value))

    @staticmethod
    def named(value: DeclaredTypeName) -> TypeReference:
        return TypeReference(
            __root__=_TypeReference.Named(type="named", fern_filepath=value.fern_filepath, name=value.name)
        )

    @staticmethod
    def primitive(value: PrimitiveType) -> TypeReference:
        return TypeReference(__root__=_TypeReference.Primitive(type="primitive", primitive=value))

    @staticmethod
    def unknown() -> TypeReference:
        return TypeReference(__root__=_TypeReference.Unknown(type="unknown"))

    @staticmethod
    def void() -> TypeReference:
        return TypeReference(__root__=_TypeReference.Void(type="void"))

    class _Visitor(ABC, typing.Generic[_Result]):
        @abstractmethod
        def container(self, value: ContainerType) -> _Result:
            ...

        @abstractmethod
        def named(self, value: DeclaredTypeName) -> _Result:
            ...

        @abstractmethod
        def primitive(self, value: PrimitiveType) -> _Result:
            ...

        @abstractmethod
        def unknown(self) -> _Result:
            ...

        @abstractmethod
        def void(self) -> _Result:
            ...

        @abstractmethod
        def _unknown(self) -> _Result:
            ...

    def _visit(self, visitor: _Visitor[_Result]) -> _Result:
        if self.__root__.type == "container":
            return visitor.container(typing.cast(_TypeReference.Container, self.__root__).container)
        if self.__root__.type == "named":
            return visitor.named(typing.cast(_TypeReference.Named, self.__root__))
        if self.__root__.type == "primitive":
            return visitor.primitive(typing.cast(_TypeReference.Primitive, self.__root__).primitive)
        if self.__root__.type == "unknown":
            return visitor.unknown()
        if self.__root__.type == "void":
            return visitor.void()
        return visitor._unknown()

    __root__: typing.Union[
        _TypeReference.Container,
        _TypeReference.Named,
        _TypeReference.Primitive,
        _TypeReference.Unknown,
        _TypeReference.Void,
        _TypeReference._Unknown,
    ]


from .container_type import ContainerType  # noqa E402

_TypeReference.Container.update_forward_refs()
