import os
import random
import time

WIDTH = 20
HEIGHT = 20
DELAY = 0.2


def random_grid(width: int, height: int) -> list[list[int]]:
    return [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]


def _count_neighbors(grid: list[list[int]], x: int, y: int) -> int:
    height, width = len(grid), len(grid[0])
    return sum(
        grid[(y + dy) % height][(x + dx) % width]
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)
        if (dx, dy) != (0, 0)
    )


def step(grid: list[list[int]]) -> list[list[int]]:
    height, width = len(grid), len(grid[0])
    return [
        [
            int(
                _count_neighbors(grid, x, y) == 3
                or (grid[y][x] == 1 and _count_neighbors(grid, x, y) == 2)
            )
            for x in range(width)
        ]
        for y in range(height)
    ]


def render(grid: list[list[int]]) -> str:
    return "\n".join("".join("█" if cell else " " for cell in row) for row in grid)


def main() -> None:
    grid = random_grid(WIDTH, HEIGHT)
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(render(grid))
            grid = step(grid)
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
