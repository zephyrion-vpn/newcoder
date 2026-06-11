import sys

RULES: dict[str, str] = {
    "привет": "здравствуй",
    "здравствуйте": "здравствуй",
    "пока": "до встречи",
    "как дела": "хорошо, спасибо!",
    "как тебя зовут": "я простой бот",
}

EXIT_WORDS = {"пока", "exit", "quit"}


def get_response(message: str) -> str:
    return RULES.get(message.strip().lower(), "я не понимаю")


def run_chat(reader=input) -> None:
    print("Бот: здравствуй! (напишите 'пока' для выхода)")
    while True:
        try:
            message = reader("Вы: ")
        except EOFError:
            print("\nБот: до встречи")
            return
        print(f"Бот: {get_response(message)}")
        if message.strip().lower() in EXIT_WORDS:
            return


def main() -> None:
    if sys.stdin.isatty():
        run_chat()
        return
    samples = iter(["Привет", "Как дела", "Расскажи анекдот", "Пока"])

    def fake_reader(prompt: str) -> str:
        value = next(samples)
        print(f"{prompt}{value}")
        return value

    run_chat(reader=fake_reader)


if __name__ == "__main__":
    main()
