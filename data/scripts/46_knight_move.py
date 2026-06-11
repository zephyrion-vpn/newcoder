def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")


def is_knight_move(x1: int, y1: int, x2: int, y2: int) -> bool:
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return {dx, dy} == {1, 2}


def main() -> None:
    x1 = read_int("x1: ")
    y1 = read_int("y1: ")
    x2 = read_int("x2: ")
    y2 = read_int("y2: ")
    print("Конь может сделать такой ход." if is_knight_move(x1, y1, x2, y2) else "Такой ход невозможен.")


if __name__ == "__main__":
    main()
