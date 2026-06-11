def read_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")
            continue
        if value <= 0:
            print("Значение должно быть положительным.")
            continue
        return value


def classify(bmi: float) -> str:
    if bmi < 18.5:
        return "Недостаток массы"
    if bmi < 25:
        return "Норма"
    if bmi < 30:
        return "Избыточная масса"
    return "Ожирение"


def main() -> None:
    weight = read_positive_number("Вес (кг): ")
    height = read_positive_number("Рост (м): ")
    bmi = weight / height ** 2
    print(f"ИМТ: {bmi:.1f} — {classify(bmi)}")


if __name__ == "__main__":
    main()
