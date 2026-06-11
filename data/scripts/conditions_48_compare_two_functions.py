def main() -> None:
    def first() -> int:
        return sum([1, 2, 3])

    def second() -> int:
        return max([2, 6, 4])

    print(first() == second())


if __name__ == "__main__":
    main()
