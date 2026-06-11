import sys


def process(command: str) -> str:
    return f"выполнено: {command.strip()}"


def run_loop(reader=input) -> int:
    processed = 0
    print("Вводите команды (Ctrl+C для выхода, 'quit' тоже завершает):")
    try:
        while True:
            try:
                line = reader("> ")
            except EOFError:
                print("\n[EOF] завершаю работу.")
                break
            if line.strip().lower() in {"quit", "exit"}:
                print("Получена команда выхода.")
                break
            if not line.strip():
                continue
            print(process(line))
            processed += 1
    except KeyboardInterrupt:
        print("\n[Ctrl+C] Корректное завершение по прерыванию.")
    finally:
        print(f"Всего обработано команд: {processed}. Ресурсы освобождены.")
    return processed


def main() -> None:
    if sys.stdin.isatty():
        run_loop()
        return
    # Демо-режим: имитируем ввод и прерывание Ctrl+C.
    commands = iter(["первая", "вторая", KeyboardInterrupt])

    def fake_reader(prompt: str) -> str:
        item = next(commands)
        if item is KeyboardInterrupt:
            print(f"{prompt}^C")
            raise KeyboardInterrupt
        print(f"{prompt}{item}")
        return item

    run_loop(reader=fake_reader)


if __name__ == "__main__":
    main()
