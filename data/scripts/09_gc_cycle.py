import gc
import weakref


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.partner: "Node | None" = None

    def __repr__(self) -> str:
        return f"Node({self.name})"


def make_cycle() -> weakref.ref:
    a = Node("A")
    b = Node("B")
    a.partner = b
    b.partner = a  # циклическая ссылка
    return weakref.ref(a)


def main() -> None:
    gc.collect()
    gc.disable()  # отключаем автоматический сбор, чтобы показать явный

    ref = make_cycle()
    print(f"После создания цикла, объект жив: {ref() is not None}")

    # Счётчик ссылок не обнуляется из-за цикла, обычный refcount не освободит память.
    collected = gc.collect()
    print(f"gc.collect() собрал объектов: {collected}")
    print(f"После сборки, объект жив: {ref() is not None}")
    print(f"Цикл успешно удалён: {ref() is None}")

    gc.enable()


if __name__ == "__main__":
    main()
