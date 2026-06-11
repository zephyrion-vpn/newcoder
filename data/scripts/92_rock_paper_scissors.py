import random

CHOICES = {"к": "Камень", "н": "Ножницы", "б": "Бумага"}
BEATS = {"к": "н", "н": "б", "б": "к"}


def read_choice(prompt: str) -> str:
    while True:
        choice = input(prompt).strip().lower()
        if choice in CHOICES:
            return choice
        print("Выберите: к (камень), н (ножницы), б (бумага).")


def main() -> None:
    player = read_choice("Ваш ход [к/н/б]: ")
    computer = random.choice(list(CHOICES))
    print(f"Компьютер: {CHOICES[computer]}")
    if player == computer:
        print("Ничья!")
    elif BEATS[player] == computer:
        print("Вы победили!")
    else:
        print("Компьютер победил.")


if __name__ == "__main__":
    main()
