def main() -> None:
    sequence = []
    current, following = 0, 1
    while len(sequence) < 10:
        sequence.append(current)
        current, following = following, current + following
    print(sequence)


if __name__ == "__main__":
    main()
