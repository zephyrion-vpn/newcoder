from pathlib import Path


def main() -> None:
    path = "/tmp/py_create_demo.txt"
    with open(path, "w", encoding="utf-8") as file:
        file.write("created")
    print(Path(path).exists())


if __name__ == "__main__":
    main()
