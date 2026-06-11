from math import inf

Matrix = list[list[float]]


def floyd_warshall(graph: Matrix) -> Matrix:
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Матрица смежности должна быть квадратной.")
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            via_k = dist[i][k]
            if via_k == inf:
                continue
            row_i = dist[i]
            row_k = dist[k]
            for j in range(n):
                candidate = via_k + row_k[j]
                if candidate < row_i[j]:
                    row_i[j] = candidate
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Граф содержит отрицательный цикл.")
    return dist


def main() -> None:
    graph = [
        [0, 3, inf, 7],
        [8, 0, 2, inf],
        [5, inf, 0, 1],
        [2, inf, inf, 0],
    ]
    result = floyd_warshall(graph)
    for row in result:
        print("  ".join("inf" if value == inf else str(int(value)) for value in row))


if __name__ == "__main__":
    main()
