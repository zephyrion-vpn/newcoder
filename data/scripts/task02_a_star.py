import heapq
from math import inf

Cell = tuple[int, int]


def _heuristic(a: Cell, b: Cell) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _neighbors(grid: list[list[int]], cell: Cell):
    rows, cols = len(grid), len(grid[0])
    row, col = cell
    for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n_row, n_col = row + d_row, col + d_col
        if 0 <= n_row < rows and 0 <= n_col < cols and grid[n_row][n_col] == 0:
            yield (n_row, n_col)


def _reconstruct(came_from: dict[Cell, Cell], current: Cell) -> list[Cell]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def a_star(grid: list[list[int]], start: Cell, goal: Cell) -> list[Cell] | None:
    if not grid or not grid[0]:
        raise ValueError("Сетка не может быть пустой.")
    for cell in (start, goal):
        row, col = cell
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            raise ValueError(f"Клетка вне сетки: {cell}")
        if grid[row][col] != 0:
            raise ValueError(f"Клетка занята препятствием: {cell}")

    open_heap: list[tuple[int, int, Cell]] = [(_heuristic(start, goal), 0, start)]
    came_from: dict[Cell, Cell] = {}
    g_score: dict[Cell, int] = {start: 0}
    visited: set[Cell] = set()

    while open_heap:
        _, cost, current = heapq.heappop(open_heap)
        if current == goal:
            return _reconstruct(came_from, current)
        if current in visited:
            continue
        visited.add(current)
        for neighbor in _neighbors(grid, current):
            tentative = cost + 1
            if tentative < g_score.get(neighbor, inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                heapq.heappush(
                    open_heap, (tentative + _heuristic(neighbor, goal), tentative, neighbor)
                )
    return None


def main() -> None:
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    path = a_star(grid, (0, 0), (4, 4))
    print("Путь:", path)
    print("Длина:", len(path) - 1 if path else "нет пути")


if __name__ == "__main__":
    main()
