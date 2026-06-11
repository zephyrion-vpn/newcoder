class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"«{self.title}» — {self.author} ({self.year})"


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_by_title(self, title: str) -> int:
        before = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        return before - len(self.books)

    def find_by_author(self, author: str) -> list[Book]:
        needle = author.lower()
        return [book for book in self.books if needle in book.author.lower()]


def main() -> None:
    library = Library()
    library.add_book(Book("1984", "Джордж Оруэлл", 1949))
    library.add_book(Book("Скотный двор", "Джордж Оруэлл", 1945))
    library.add_book(Book("Метаморфоза", "Франц Кафка", 1915))
    print("Книги Оруэлла:")
    for book in library.find_by_author("Оруэлл"):
        print(f"  {book}")
    removed = library.remove_by_title("1984")
    print(f"Удалено: {removed}")
    print(f"Осталось книг: {len(library.books)}")


if __name__ == "__main__":
    main()
