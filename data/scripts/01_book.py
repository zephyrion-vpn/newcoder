from datetime import date


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def is_old(self) -> bool:
        return date.today().year - self.year > 50

    def __str__(self) -> str:
        return f"«{self.title}» — {self.author} ({self.year})"


def main() -> None:
    new_book = Book("Чистый код", "Роберт Мартин", 2008)
    old_book = Book("Война и мир", "Лев Толстой", 1869)
    print(new_book)
    print(f"Старая? {new_book.is_old()}")
    print(old_book)
    print(f"Старая? {old_book.is_old()}")


if __name__ == "__main__":
    main()
