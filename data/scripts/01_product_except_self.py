def product_except_self(numbers: list[int]) -> list[int]:
    n = len(numbers)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= numbers[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= numbers[i]
    return result


def main() -> None:
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([2, 3, 4, 5]))
    print(product_except_self([0, 4, 5]))
    print(product_except_self([0, 0, 5]))
    print(product_except_self([]))


if __name__ == "__main__":
    main()
