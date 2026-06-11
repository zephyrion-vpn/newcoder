from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    text: str
    options: list[str]
    answer: int


QUIZ = [
    Question("Столица Франции?", ["Лондон", "Париж", "Берлин"], 2),
    Question("Сколько будет 7 × 8?", ["54", "56", "64"], 2),
    Question("Язык с логотипом-змеёй?", ["Python", "Ruby", "Go"], 1),
    Question("Сколько планет в Солнечной системе?", ["7", "8", "9"], 2),
    Question("Химический символ воды?", ["H2O", "CO2", "O2"], 1),
]


def ask(question: Question) -> bool:
    print(question.text)
    for index, option in enumerate(question.options, start=1):
        print(f"  {index}. {option}")
    while True:
        raw = input("Ваш ответ (номер): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(question.options):
            return int(raw) == question.answer
        print(f"Введите номер от 1 до {len(question.options)}.")


def main() -> None:
    score = sum(1 for question in QUIZ if ask(question))
    print(f"\nИтог: {score} из {len(QUIZ)}.")


if __name__ == "__main__":
    main()
