# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .node_id import NodeId


class BinaryTreeNodeValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    val: float
    right: typing.Optional[NodeId]
    left: typing.Optional[NodeId]

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        val: typing_extensions.NotRequired[float]
        right: typing_extensions.NotRequired[typing.Optional[NodeId]]
        left: typing_extensions.NotRequired[typing.Optional[NodeId]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BinaryTreeNodeValue.Validators.root
            def validate(values: BinaryTreeNodeValue.Partial) -> BinaryTreeNodeValue.Partial:
                ...

            @BinaryTreeNodeValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: BinaryTreeNodeValue.Partial) -> NodeId:
                ...

            @BinaryTreeNodeValue.Validators.field("val")
            def validate_val(val: float, values: BinaryTreeNodeValue.Partial) -> float:
                ...

            @BinaryTreeNodeValue.Validators.field("right")
            def validate_right(right: typing.Optional[NodeId], values: BinaryTreeNodeValue.Partial) -> typing.Optional[NodeId]:
                ...

            @BinaryTreeNodeValue.Validators.field("left")
            def validate_left(left: typing.Optional[NodeId], values: BinaryTreeNodeValue.Partial) -> typing.Optional[NodeId]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[BinaryTreeNodeValue.Partial], BinaryTreeNodeValue.Partial]]
        ] = []
        _node_id_validators: typing.ClassVar[typing.List[BinaryTreeNodeValue.Validators.NodeIdValidator]] = []
        _val_validators: typing.ClassVar[typing.List[BinaryTreeNodeValue.Validators.ValValidator]] = []
        _right_validators: typing.ClassVar[typing.List[BinaryTreeNodeValue.Validators.RightValidator]] = []
        _left_validators: typing.ClassVar[typing.List[BinaryTreeNodeValue.Validators.LeftValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[BinaryTreeNodeValue.Partial], BinaryTreeNodeValue.Partial]
        ) -> typing.Callable[[BinaryTreeNodeValue.Partial], BinaryTreeNodeValue.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"]
        ) -> typing.Callable[
            [BinaryTreeNodeValue.Validators.NodeIdValidator], BinaryTreeNodeValue.Validators.NodeIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["val"]
        ) -> typing.Callable[
            [BinaryTreeNodeValue.Validators.ValValidator], BinaryTreeNodeValue.Validators.ValValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["right"]
        ) -> typing.Callable[
            [BinaryTreeNodeValue.Validators.RightValidator], BinaryTreeNodeValue.Validators.RightValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["left"]
        ) -> typing.Callable[
            [BinaryTreeNodeValue.Validators.LeftValidator], BinaryTreeNodeValue.Validators.LeftValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    cls._node_id_validators.append(validator)
                if field_name == "val":
                    cls._val_validators.append(validator)
                if field_name == "right":
                    cls._right_validators.append(validator)
                if field_name == "left":
                    cls._left_validators.append(validator)
                return validator

            return decorator

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, node_id: NodeId, *, values: BinaryTreeNodeValue.Partial) -> NodeId:
                ...

        class ValValidator(typing_extensions.Protocol):
            def __call__(self, val: float, *, values: BinaryTreeNodeValue.Partial) -> float:
                ...

        class RightValidator(typing_extensions.Protocol):
            def __call__(
                self, right: typing.Optional[NodeId], *, values: BinaryTreeNodeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class LeftValidator(typing_extensions.Protocol):
            def __call__(
                self, left: typing.Optional[NodeId], *, values: BinaryTreeNodeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: BinaryTreeNodeValue.Partial) -> BinaryTreeNodeValue.Partial:
        for validator in BinaryTreeNodeValue.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id")
    def _validate_node_id(cls, node_id: NodeId, values: BinaryTreeNodeValue.Partial) -> NodeId:
        for validator in BinaryTreeNodeValue.Validators._node_id_validators:
            node_id = validator(node_id, values=values)
        return node_id

    @pydantic.validator("val")
    def _validate_val(cls, val: float, values: BinaryTreeNodeValue.Partial) -> float:
        for validator in BinaryTreeNodeValue.Validators._val_validators:
            val = validator(val, values=values)
        return val

    @pydantic.validator("right")
    def _validate_right(
        cls, right: typing.Optional[NodeId], values: BinaryTreeNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in BinaryTreeNodeValue.Validators._right_validators:
            right = validator(right, values=values)
        return right

    @pydantic.validator("left")
    def _validate_left(
        cls, left: typing.Optional[NodeId], values: BinaryTreeNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in BinaryTreeNodeValue.Validators._left_validators:
            left = validator(left, values=values)
        return left

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
