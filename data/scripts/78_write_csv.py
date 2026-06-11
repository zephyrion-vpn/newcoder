import csv

FILENAME = "books.csv"
BOOKS = [
    {"title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
]


def main() -> None:
    fieldnames = ["title", "author", "year"]
    with open(FILENAME, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(BOOKS)
    print(f"Данные записаны в {FILENAME}.")


if __name__ == "__main__":
    main()
