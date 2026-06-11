from __future__ import annotations

import sys


class TreeType:
    __slots__ = ("name", "texture")

    def __init__(self, name: str, texture: str) -> None:
        self.name = name
        self.texture = texture

    def render(self, x: int, y: int) -> str:
        return f"{self.name}@({x},{y})"


class TreeFactory:
    _types: dict[tuple[str, str], TreeType] = {}

    @classmethod
    def get_type(cls, name: str, texture: str) -> TreeType:
        key = (name, texture)
        if key not in cls._types:
            cls._types[key] = TreeType(name, texture)
        return cls._types[key]


class Tree:
    __slots__ = ("x", "y", "type")

    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self.x = x
        self.y = y
        self.type = tree_type

    def render(self) -> str:
        return self.type.render(self.x, self.y)


class Forest:
    def __init__(self) -> None:
        self.trees: list[Tree] = []

    def plant(self, x: int, y: int, name: str, texture: str) -> None:
        tree_type = TreeFactory.get_type(name, texture)
        self.trees.append(Tree(x, y, tree_type))


def main() -> None:
    forest = Forest()
    names = [("Дуб", "oak.png"), ("Сосна", "pine.png"), ("Берёза", "birch.png")]
    for i in range(10_000):
        name, texture = names[i % len(names)]
        forest.plant(i % 1000, i // 1000, name, texture)

    print(f"Посажено деревьев: {len(forest.trees)}")
    print(f"Уникальных типов (flyweight): {len(TreeFactory._types)}")
    shared = all(
        forest.trees[i].type is forest.trees[i + len(names)].type
        for i in range(len(names))
    )
    print(f"Типы разделяются между экземплярами: {shared}")
    print(f"Пример рендера: {forest.trees[0].render()}")


if __name__ == "__main__":
    main()
