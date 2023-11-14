from fern_python.codegen.ast import AstNode
from fern_python.codegen.ast import AstNodeMetadata
from fern_python.codegen.ast import Expression
from fern_python.codegen.ast import NodeWriter


class ConditionalExpression(AstNode):

    def __init__(self, test: Expression, left: AstNode, right: AstNode) -> None:
        self.test = test
        self.left = left
        self.right = right
    def get_metadata(self) -> AstNodeMetadata:
        pass

    def write(self, writer: NodeWriter) -> None:
        writer.write_node(self.left)
        writer.write(" if ")
        writer.write_node(self.test)
        writer.write(" else ")
        writer.write_node(self.right)
