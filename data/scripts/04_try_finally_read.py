import os
import tempfile
from typing import Optional


def read_file(path: str) -> Optional[str]:
    handle = None
    try:
        handle = open(path, encoding="utf-8")
        data = handle.read()
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return None
    else:
        print(f"Успешно прочитано символов: {len(data)}")
        return data
    finally:
        if handle is not None:
            handle.close()
            print("Файл закрыт.")


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "data.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("привет")
    print(repr(read_file(path)))
    print(repr(read_file("/нет/такого/файла.txt")))


if __name__ == "__main__":
    main()
