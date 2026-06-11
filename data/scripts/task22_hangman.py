import random
import sys
from typing import Callable

_BS = chr(92)

HANGMAN = [
    "+---+\n|   |\n|\n|\n|\n=====",
    "+---+\n|   |\n|   O\n|\n|\n=====",
    "+---+\n|   |\n|   O\n|   |\n|\n=====",
    "+---+\n|   |\n|   O\n|  /|\n|\n=====",
    f"+---+\n|   |\n|   O\n|  /|{_BS}\n|\n=====",
    f"+---+\n|   |\n|   O\n|  /|{_BS}\n|  /\n=====",
    f"+---+\n|   |\n|   O\n|  /|{_BS}\n|  / {_BS}\n=====",
]

WORDS = ["python", "variable", "function", "algorithm", "iterator"]


def masked(word: str, guessed: set[str]) -> str:
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play(word: str, max_wrong: int = 6, reader: Callable[[str], str] = input) -> bool:
    guessed: set[str] = set()
    wrong = 0
    while wrong < max_wrong:
        print(HANGMAN[wrong])
        print(masked(word, guessed))
        if all(ch in guessed for ch in word):
            print("Вы выиграли!")
            return True
        letter = reader("Буква: ").strip().lower()
        if not letter:
            continue
        letter = letter[0]
        if letter in guessed:
            print("Уже было")
            continue
        guessed.add(letter)
        if letter not in word:
            wrong += 1
            print(f"Нет такой буквы. Ошибок: {wrong}/{max_wrong}")
    print(HANGMAN[min(wrong, len(HANGMAN) - 1)])
    print(f"Вы проиграли. Слово: {word}")
    return False


def _scripted(letters: list[str]) -> Callable[[str], str]:
    iterator = iter(letters)

    def reader(prompt: str = "") -> str:
        return next(iterator, "?")

    return reader


def main() -> None:
    word = random.choice(WORDS)
    if sys.stdin.isatty():
        play(word)
    else:
        print(f"[демо] загадано слово из {len(word)} букв")
        guesses = ["z"] + list(dict.fromkeys(word))
        play(word, reader=_scripted(guesses))


if __name__ == "__main__":
    main()
