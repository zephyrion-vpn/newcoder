from pathlib import Path


def main() -> None:
    path = Path("/tmp") / "sub" / "file.txt"
    print(path)


if __name__ == "__main__":
    main()
