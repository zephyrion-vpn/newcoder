import os
import tempfile


def unique_temp_file(directory: str, prefix: str = "tmp_", suffix: str = ".dat") -> str:
    os.makedirs(directory, exist_ok=True)
    fd, path = tempfile.mkstemp(prefix=prefix, suffix=suffix, dir=directory)
    os.close(fd)
    return path


def main() -> None:
    directory = tempfile.mkdtemp()
    first = unique_temp_file(directory)
    second = unique_temp_file(directory)
    print(f"Создан 1: {os.path.basename(first)}")
    print(f"Создан 2: {os.path.basename(second)}")
    print(f"Имена различны: {first != second}")
    print(f"Оба существуют: {os.path.exists(first) and os.path.exists(second)}")


if __name__ == "__main__":
    main()
