def main() -> None:
    text = "apple"
    print(bool(text) and text[0].lower() in "aeiou")


if __name__ == "__main__":
    main()
