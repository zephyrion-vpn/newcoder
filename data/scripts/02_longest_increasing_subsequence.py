from bisect import bisect_left


def lis_length(numbers: list[int]) -> int:
    tails: list[int] = []
    for number in numbers:
        index = bisect_left(tails, number)
        if index == len(tails):
            tails.append(number)
        else:
            tails[index] = number
    return len(tails)


def main() -> None:
    print(lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lis_length([0, 1, 0, 3, 2, 3]))
    print(lis_length([7, 7, 7, 7]))
    print(lis_length([]))


if __name__ == "__main__":
    main()
