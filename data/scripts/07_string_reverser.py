class StringReverser:
    def __init__(self, text: str) -> None:
        self.text = text

    def __call__(self) -> str:
        return self.text[::-1]


def main() -> None:
    reverser = StringReverser("Привет")
    print(reverser())
    print(StringReverser("hello")())


if __name__ == "__main__":
    main()
