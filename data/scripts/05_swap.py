def read_value(prompt: str) -> str:
    return input(prompt).strip()


def main() -> None:
    a = read_value("Введите значение a: ")
    b = read_value("Введите значение b: ")
    print(f"До обмена: a = {a}, b = {b}")

    temp = a
    a = b
    b = temp
    print(f"После обмена через третью переменную: a = {a}, b = {b}")

    a, b = b, a
    print(f"После обмена без третьей переменной: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
