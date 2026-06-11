import random
from collections import defaultdict

MOVIES = (
    ("Начало", "фантастика"),
    ("Матрица", "фантастика"),
    ("Интерстеллар", "фантастика"),
    ("Прибытие", "фантастика"),
    ("Крёстный отец", "драма"),
    ("Форрест Гамп", "драма"),
    ("Зелёная миля", "драма"),
    ("Джокер", "драма"),
    ("Мальчишник в Вегасе", "комедия"),
    ("Маска", "комедия"),
    ("Однажды в Голливуде", "комедия"),
    ("Оно", "ужасы"),
    ("Сияние", "ужасы"),
    ("Заклятие", "ужасы"),
)


def build_genre_index(movies: tuple[tuple[str, str], ...]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for title, genre in movies:
        index[genre].append(title)
    return index


def recommend(
    watched: list[tuple[str, str]],
    movies: tuple[tuple[str, str], ...] = MOVIES,
    count: int = 3,
) -> list[str]:
    index = build_genre_index(movies)
    watched_titles = {title for title, _ in watched}
    candidates = list(
        dict.fromkeys(
            title
            for _, genre in watched
            for title in index.get(genre, [])
            if title not in watched_titles
        )
    )
    return random.sample(candidates, min(count, len(candidates)))


def main() -> None:
    watched = [("Матрица", "фантастика"), ("Крёстный отец", "драма")]
    recommendations = recommend(watched)
    if not recommendations:
        print("Нет подходящих рекомендаций.")
        return
    print("Рекомендуем посмотреть:")
    for title in recommendations:
        print(f"  - {title}")


if __name__ == "__main__":
    main()
