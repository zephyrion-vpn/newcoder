from itertools import groupby


def group_by_parity(numbers: list[int]) -> dict[str, list[int]]:
    ordered = sorted(numbers, key=lambda x: x % 2)
    result: dict[str, list[int]] = {}
    for key, group in groupby(ordered, key=lambda x: x % 2):
        label = "чётные" if key == 0 else "нечётные"
        result[label] = list(group)
    return result


def main() -> None:
    print(group_by_parity([1, 2, 3, 4, 5, 6, 7]))
    print(group_by_parity([2, 4, 6]))


if __name__ == "__main__":
    main()
