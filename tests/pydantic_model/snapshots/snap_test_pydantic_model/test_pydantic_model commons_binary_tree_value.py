import typing

import pydantic
import typing_extensions

from .binary_tree_node_value import BinaryTreeNodeValue
from .node_id import NodeId


class BinaryTreeValue(pydantic.BaseModel):
    root: typing.Optional[NodeId]
    nodes: typing.Dict[NodeId, BinaryTreeNodeValue]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("root")
    def _validate_root(cls, root: typing.Optional[NodeId]) -> typing.Optional[NodeId]:
        for validator in BinaryTreeValue.Validators._root_validators:
            root = validator(root)
        return root

    @pydantic.validator("nodes")
    def _validate_nodes(
        cls, nodes: typing.Dict[NodeId, BinaryTreeNodeValue]
    ) -> typing.Dict[NodeId, BinaryTreeNodeValue]:
        for validator in BinaryTreeValue.Validators._nodes_validators:
            nodes = validator(nodes)
        return nodes

    class Validators:
        _root_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.Optional[NodeId]], typing.Optional[NodeId]]]
        ] = []
        _nodes_validators: typing.ClassVar[
            typing.List[
                typing.Callable[[typing.Dict[NodeId, BinaryTreeNodeValue]], typing.Dict[NodeId, BinaryTreeNodeValue]]
            ]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["root"]
        ) -> typing.Callable[
            [typing.Callable[[typing.Optional[NodeId]], typing.Optional[NodeId]]],
            typing.Callable[[typing.Optional[NodeId]], typing.Optional[NodeId]],
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["nodes"]
        ) -> typing.Callable[
            [typing.Callable[[typing.Dict[NodeId, BinaryTreeNodeValue]], typing.Dict[NodeId, BinaryTreeNodeValue]]],
            typing.Callable[[typing.Dict[NodeId, BinaryTreeNodeValue]], typing.Dict[NodeId, BinaryTreeNodeValue]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "root":
                    cls._root_validators.append(validator)
                elif field_name == "nodes":
                    cls._nodes_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on BinaryTreeValue: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
