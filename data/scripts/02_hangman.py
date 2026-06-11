import random

HANGMAN_STAGES = [
    """
  +---+
      |
      |
      |
     ===""",
    """
  +---+
  O   |
      |
      |
     ===""",
    """
  +---+
  O   |
  |   |
      |
     ===""",
    """
  +---+
  O   |
 /|   |
      |
     ===""",
    """
  +---+
  O   |
 /|\\  |
      |
     ===""",
    """
  +---+
  O   |
 /|\\  |
 /    |
     ===""",
    """
  +---+
  O   |
 /|\\  |
 / \\  |
     ===""",
]

WORDS = ["python", "программа", "компьютер", "алгоритм", "функция"]


def play(word: str | None = None) -> None:
    word = (word or random.choice(WORDS)).lower()
    guessed: set[str] = set()
    wrong = 0
    max_wrong = len(HANGMAN_STAGES) - 1

    while wrong < max_wrong:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(HANGMAN_STAGES[wrong])
        print(f"Слово: {display}")
        if all(c in guessed for c in word):
            print("Победа! Вы угадали слово.")
            return
        try:
            letter = input("Буква: ").strip().lower()
        except EOFError:
            print("\nИгра прервана.")
            return
        if not letter or len(letter) != 1:
            print("Введите одну букву.")
            continue
        if letter in guessed:
            print("Уже было.")
            continue
        guessed.add(letter)
        if letter not in word:
            wrong += 1
            print("Неверно!")

    print(HANGMAN_STAGES[wrong])
    print(f"Поражение! Загаданное слово: {word}")


def main() -> None:
    play()


if __name__ == "__main__":
    main()
