def run() -> None:
    print("Вводите команды (Ctrl+C или 'exit' для выхода).")
    processed = 0
    try:
        while True:
            try:
                command = input("> ")
            except EOFError:
                print("\nПолучен EOF, завершаю работу.")
                break
            command = command.strip()
            if command.lower() in {"exit", "quit"}:
                break
            if command:
                processed += 1
                print(f"Обработано: {command!r}")
    except KeyboardInterrupt:
        print("\nПолучен Ctrl+C, завершаю работу.")
    finally:
        print(f"Всего обработано команд: {processed}. До свидания!")


if __name__ == "__main__":
    run()
