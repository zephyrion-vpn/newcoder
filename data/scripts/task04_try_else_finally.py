import os
import tempfile
from typing import TextIO


def read_file(path: str) -> str | None:
    handle: TextIO | None = None
    try:
        handle = open(path, encoding="utf-8")
        data = handle.read()
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return None
    else:
        print("Чтение успешно")
        return data
    finally:
        if handle is not None:
            handle.close()
            print("Файл закрыт")


def main() -> None:
    path = tempfile.mktemp(suffix=".txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("привет")
    print("Содержимое:", read_file(path))
    os.remove(path)
    print("---")
    print("Результат:", read_file("/нет/такого/файла.txt"))


if __name__ == "__main__":
    main()
