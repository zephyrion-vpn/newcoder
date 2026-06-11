from __future__ import annotations


class Matrix:
    def __init__(self, rows: list[list[float]]) -> None:
        if not rows or not all(rows):
            raise ValueError("Матрица не может быть пустой.")
        width = len(rows[0])
        if any(len(row) != width for row in rows):
            raise ValueError("Все строки должны быть одинаковой длины.")
        self.rows = [list(row) for row in rows]

    def scale(self, factor: float) -> "Matrix":
        return Matrix([[value * factor for value in row] for row in self.rows])

    def __str__(self) -> str:
        return "\n".join(" ".join(str(value) for value in row) for row in self.rows)


def main() -> None:
    matrix = Matrix([[1, 2, 3], [4, 5, 6]])
    print("Исходная:")
    print(matrix)
    print("Умноженная на 2:")
    print(matrix.scale(2))


if __name__ == "__main__":
    main()
