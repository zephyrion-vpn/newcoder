from __future__ import annotations

from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor") -> object: ...


class Number(Node):
    def __init__(self, value: float) -> None:
        self.value = value

    def accept(self, visitor: "Visitor") -> object:
        return visitor.visit_number(self)


class BinaryOp(Node):
    def __init__(self, op: str, left: Node, right: Node) -> None:
        self.op = op
        self.left = left
        self.right = right

    def accept(self, visitor: "Visitor") -> object:
        return visitor.visit_binary(self)


class Visitor(ABC):
    @abstractmethod
    def visit_number(self, node: Number) -> object: ...

    @abstractmethod
    def visit_binary(self, node: BinaryOp) -> object: ...


class Evaluator(Visitor):
    def visit_number(self, node: Number) -> float:
        return node.value

    def visit_binary(self, node: BinaryOp) -> float:
        left = node.left.accept(self)
        right = node.right.accept(self)
        ops = {
            "+": left + right,
            "-": left - right,
            "*": left * right,
            "/": left / right if right else float("inf"),
        }
        return ops[node.op]


class Printer(Visitor):
    def visit_number(self, node: Number) -> str:
        return str(node.value)

    def visit_binary(self, node: BinaryOp) -> str:
        return f"({node.left.accept(self)} {node.op} {node.right.accept(self)})"


def main() -> None:
    # (3 + 5) * (10 - 4)
    tree = BinaryOp(
        "*",
        BinaryOp("+", Number(3), Number(5)),
        BinaryOp("-", Number(10), Number(4)),
    )
    print("Выражение:", tree.accept(Printer()))
    print("Результат:", tree.accept(Evaluator()))


if __name__ == "__main__":
    main()
