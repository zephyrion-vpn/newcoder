def solve_n_queens(n: int) -> list[tuple[int, ...]]:
    if n < 0:
        raise ValueError("Размер доски не может быть отрицательным.")
    solutions: list[tuple[int, ...]] = []
    placement: list[int] = []
    full = (1 << n) - 1

    def backtrack(columns: int, diag1: int, diag2: int) -> None:
        if len(placement) == n:
            solutions.append(tuple(placement))
            return
        available = full & ~(columns | diag1 | diag2)
        while available:
            bit = available & -available
            available ^= bit
            placement.append(bit.bit_length() - 1)
            backtrack(columns | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1)
            placement.pop()

    backtrack(0, 0, 0)
    return solutions


def render_board(solution: tuple[int, ...]) -> str:
    size = len(solution)
    return "\n".join(
        "".join("♛" if col == queen else "." for col in range(size))
        for queen in solution
    )


def main() -> None:
    n = 8
    solutions = solve_n_queens(n)
    print(f"N = {n}: найдено решений: {len(solutions)}")
    print("\nПример решения:")
    print(render_board(solutions[0]))


if __name__ == "__main__":
    main()
