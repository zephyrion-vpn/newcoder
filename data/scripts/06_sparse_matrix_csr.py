from __future__ import annotations


class CSRMatrix:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.values: list[float] = []
        self.col_indices: list[int] = []
        self.row_ptr: list[int] = [0] * (rows + 1)

    @classmethod
    def from_dense(cls, dense: list[list[float]]) -> "CSRMatrix":
        rows = len(dense)
        cols = len(dense[0]) if rows else 0
        matrix = cls(rows, cols)
        for r in range(rows):
            for c in range(cols):
                if dense[r][c] != 0:
                    matrix.values.append(dense[r][c])
                    matrix.col_indices.append(c)
            matrix.row_ptr[r + 1] = len(matrix.values)
        return matrix

    def to_dense(self) -> list[list[float]]:
        dense = [[0.0] * self.cols for _ in range(self.rows)]
        for r in range(self.rows):
            for idx in range(self.row_ptr[r], self.row_ptr[r + 1]):
                dense[r][self.col_indices[idx]] = self.values[idx]
        return dense

    def multiply(self, other: "CSRMatrix") -> "CSRMatrix":
        if self.cols != other.rows:
            raise ValueError("Несовместимые размеры.")
        result = CSRMatrix(self.rows, other.cols)
        for r in range(self.rows):
            accumulator: dict[int, float] = {}
            for idx in range(self.row_ptr[r], self.row_ptr[r + 1]):
                a_col = self.col_indices[idx]
                a_val = self.values[idx]
                for jdx in range(other.row_ptr[a_col], other.row_ptr[a_col + 1]):
                    b_col = other.col_indices[jdx]
                    accumulator[b_col] = accumulator.get(b_col, 0.0) + a_val * other.values[jdx]
            for c in sorted(accumulator):
                if accumulator[c] != 0:
                    result.values.append(accumulator[c])
                    result.col_indices.append(c)
            result.row_ptr[r + 1] = len(result.values)
        return result

    def nnz(self) -> int:
        return len(self.values)


def _dense_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    rows, inner, cols = len(a), len(b), len(b[0])
    result = [[0.0] * cols for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            if a[i][k]:
                for j in range(cols):
                    result[i][j] += a[i][k] * b[k][j]
    return result


def main() -> None:
    a = [
        [1, 0, 0, 2],
        [0, 3, 0, 0],
        [0, 0, 4, 0],
    ]
    b = [
        [0, 1],
        [5, 0],
        [0, 0],
        [0, 6],
    ]
    csr_a = CSRMatrix.from_dense(a)
    csr_b = CSRMatrix.from_dense(b)
    product = csr_a.multiply(csr_b)

    print(f"A: {csr_a.rows}x{csr_a.cols}, nnz={csr_a.nnz()} (из {csr_a.rows * csr_a.cols})")
    print(f"Результат CSR:  {product.to_dense()}")
    print(f"Эталон (dense): {_dense_multiply(a, b)}")
    print(f"Совпадает: {product.to_dense() == _dense_multiply(a, b)}")


if __name__ == "__main__":
    main()
