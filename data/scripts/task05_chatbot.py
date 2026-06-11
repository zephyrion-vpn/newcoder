import sys

RULES = {
    "привет": "здравствуй",
    "пока": "до встречи",
}
EXIT_WORD = "пока"


def respond(message: str) -> str:
    return RULES.get(message.strip().lower(), "я не понимаю")


def main() -> None:
    print("Чат-бот запущен. Напишите «пока» для выхода.")
    while True:
        try:
            message = input("Вы: ")
        except (EOFError, KeyboardInterrupt):
            print()
            return
        print(f"Бот: {respond(message)}")
        if message.strip().lower() == EXIT_WORD:
            return


if __name__ == "__main__":
    main()
