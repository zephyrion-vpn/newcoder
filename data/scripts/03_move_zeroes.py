def move_zeroes(numbers: list[int]) -> list[int]:
    non_zero = [number for number in numbers if number != 0]
    zero_count = len(numbers) - len(non_zero)
    return non_zero + [0] * zero_count


def move_zeroes_inplace(numbers: list[int]) -> None:
    insert_at = 0
    for index, number in enumerate(numbers):
        if number != 0:
            numbers[insert_at], numbers[index] = numbers[index], numbers[insert_at]
            insert_at += 1


def main() -> None:
    print(move_zeroes([0, 1, 0, 3, 12]))
    print(move_zeroes([0, 0, 1]))
    data = [1, 0, 2, 0, 0, 3]
    move_zeroes_inplace(data)
    print(data)


if __name__ == "__main__":
    main()
