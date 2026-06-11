def find_pair(numbers: list[int], target: int) -> tuple[int, int] | None:
    seen: set[int] = set()
    for number in numbers:
        if target - number in seen:
            return (target - number, number)
        seen.add(number)
    return None


def main() -> None:
    print(find_pair([2, 7, 11, 15], 9))


if __name__ == "__main__":
    main()
