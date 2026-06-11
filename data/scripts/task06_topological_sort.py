from collections import deque
from typing import Hashable, Mapping, Sequence

Graph = Mapping[Hashable, Sequence[Hashable]]


def topological_sort(graph: Graph) -> list[Hashable]:
    nodes: set[Hashable] = set(graph)
    for successors in graph.values():
        nodes.update(successors)

    indegree = {node: 0 for node in nodes}
    for successors in graph.values():
        for successor in successors:
            indegree[successor] += 1

    queue = deque(sorted((n for n in nodes if indegree[n] == 0), key=repr))
    order: list[Hashable] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for successor in sorted(graph.get(node, ()), key=repr):
            indegree[successor] -= 1
            if indegree[successor] == 0:
                queue.append(successor)

    if len(order) != len(nodes):
        raise ValueError("Граф содержит цикл, топологическая сортировка невозможна.")
    return order


def main() -> None:
    build_graph = {
        "база": ["ядро", "утилиты"],
        "ядро": ["сервис"],
        "утилиты": ["сервис"],
        "сервис": ["приложение"],
        "приложение": [],
    }
    print("Порядок сборки:", " -> ".join(topological_sort(build_graph)))


if __name__ == "__main__":
    main()
