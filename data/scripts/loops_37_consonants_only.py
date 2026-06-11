def main() -> None:
    text = "education"
    for char in text:
        if char.isalpha() and char.lower() not in "aeiou":
            print(char)


if __name__ == "__main__":
    main()
