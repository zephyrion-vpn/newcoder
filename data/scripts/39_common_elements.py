def common(first: list[int], second: list[int]) -> list[int]:
    return sorted(set(first) & set(second))


if __name__ == "__main__":
    print(common([1, 2, 3], [2, 3, 4]))
