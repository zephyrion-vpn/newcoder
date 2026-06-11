import os
import random
import sys
import time


def create_grid(rows: int, cols: int, seed: int | None = None) -> list[list[int]]:
    rng = random.Random(seed)
    return [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


def count_neighbors(grid: list[list[int]], r: int, c: int) -> int:
    rows, cols = len(grid), len(grid[0])
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                total += grid[nr][nc]
    return total


def step(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            alive = grid[r][c]
            neighbors = count_neighbors(grid, r, c)
            if alive and neighbors in (2, 3):
                new_grid[r][c] = 1
            elif not alive and neighbors == 3:
                new_grid[r][c] = 1
    return new_grid


def render(grid: list[list[int]]) -> str:
    return "\n".join("".join("█" if cell else " " for cell in row) for row in grid)


def main() -> None:
    rows = cols = 20
    grid = create_grid(rows, cols, seed=7)
    interactive = sys.stdin.isatty()
    generations = 100 if interactive else 5

    for gen in range(generations):
        if interactive:
            os.system("cls" if os.name == "nt" else "clear")
        print(f"Поколение {gen + 1}")
        print(render(grid))
        living = sum(sum(row) for row in grid)
        print(f"Живых клеток: {living}")
        if living == 0:
            print("Колония вымерла.")
            break
        grid = step(grid)
        time.sleep(0.2 if interactive else 0)


if __name__ == "__main__":
    main()
