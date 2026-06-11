from collections import defaultdict


class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices = vertices
        self.adj: dict[int, list[int]] = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)

    def find_bridges_and_articulation_points(self) -> tuple[list[tuple[int, int]], set[int]]:
        disc = [-1] * self.vertices
        low = [-1] * self.vertices
        visited = [False] * self.vertices
        bridges: list[tuple[int, int]] = []
        articulation: set[int] = set()
        timer = [0]

        def dfs(u: int, parent: int) -> None:
            visited[u] = True
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            children = 0
            for v in self.adj[u]:
                if v == parent:
                    continue
                if visited[v]:
                    low[u] = min(low[u], disc[v])
                else:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append((min(u, v), max(u, v)))
                    if parent != -1 and low[v] >= disc[u]:
                        articulation.add(u)
            if parent == -1 and children > 1:
                articulation.add(u)

        for start in range(self.vertices):
            if not visited[start]:
                dfs(start, -1)
        return sorted(bridges), articulation


def main() -> None:
    g = Graph(5)
    for u, v in [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]:
        g.add_edge(u, v)
    bridges, points = g.find_bridges_and_articulation_points()
    print("Мосты:", bridges)
    print("Точки сочленения:", sorted(points))


if __name__ == "__main__":
    main()
