def min_max(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)


if __name__ == "__main__":
    low, high = min_max([3, 1, 2])
    print(low, high)
