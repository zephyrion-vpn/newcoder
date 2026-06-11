def main() -> None:
    left = [1, 2, 3]
    right = ["a", "b", "c"]
    for number, letter in zip(left, right):
        print(number, letter)


if __name__ == "__main__":
    main()
