import random
from collections import Counter

MOVIE_DB: dict[str, list[str]] = {
    "фантастика": ["Интерстеллар", "Матрица", "Начало́", "Бегущий по лезвию", "Прибытие", "Дюна"],
    "драма": ["Зелёная миля", "Побег из Шоушенка", "Форрест Гамп", "Бойцовский клуб", "Заводной апельсин"],
    "комедия": ["Маска", "День сурка", "Однажды в Вегасе", "Эйс Вентура", "Брус Всемогущий"],
    "триллер": ["Молчание ягнят", "Семь", "Остров проклятых", "Исчезнувшая", "Престиж"],
}


def recommend(watched: list[str], db: dict[str, list[str]], k: int = 3) -> list[str]:
    genre_counts = Counter(genre for genre in watched if genre in db)
    if not genre_counts:
        raise ValueError("нет известных жанров в истории просмотров")
    favorite_genre = genre_counts.most_common(1)[0][0]
    pool = list(db[favorite_genre])
    random.shuffle(pool)
    return pool[:k]


def main() -> None:
    random.seed(42)
    watched = ["фантастика", "драма", "фантастика"]
    print(f"История просмотров (жанры): {watched}")
    recommendations = recommend(watched, MOVIE_DB)
    print("Рекомендуем (тот же любимый жанр):")
    for i, movie in enumerate(recommendations, 1):
        print(f"   {i}. {movie}")


if __name__ == "__main__":
    main()
