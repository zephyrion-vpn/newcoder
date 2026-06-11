import random

FILENAME = "phrases.txt"
PHRASES = [
    "Сегодня отличный день для кода.",
    "Python делает программирование проще.",
    "Чистый код — забота о будущем.",
    "Практика важнее теории.",
    "Ошибки — это часть обучения.",
    "Никогда не сдавайся перед багом.",
    "Простота — высшая форма сложности.",
]


def main() -> None:
    chosen = random.sample(PHRASES, 5)
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write("\n".join(chosen) + "\n")
    print(f"Записано 5 фраз в файл {FILENAME}.")


if __name__ == "__main__":
    main()
