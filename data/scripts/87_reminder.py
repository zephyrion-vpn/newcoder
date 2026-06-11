import time

INTERVAL_SECONDS = 20 * 60
MESSAGE = "Пора размяться и попить воды!"


def main() -> None:
    print("Напоминание запущено. Нажмите Ctrl+C для выхода.")
    try:
        while True:
            time.sleep(INTERVAL_SECONDS)
            print(MESSAGE)
    except KeyboardInterrupt:
        print("\nНапоминание остановлено.")


if __name__ == "__main__":
    main()
