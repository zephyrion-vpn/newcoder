def main() -> None:
    text = "one two three four"
    count = 0
    for word in text.split():
        count += 1
    print(count)


if __name__ == "__main__":
    main()
