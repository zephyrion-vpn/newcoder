import time


def main() -> None:
    input("Нажмите Enter для старта...")
    start = time.perf_counter()
    input("Нажмите Enter для остановки...")
    elapsed = time.perf_counter() - start
    print(f"Прошло: {elapsed:.2f} сек.")


if __name__ == "__main__":
    main()
