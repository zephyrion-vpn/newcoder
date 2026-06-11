from pathlib import Path

PREFIX = "backup_"


def add_prefix(directory: Path, prefix: str) -> list[tuple[str, str]]:
    renamed: list[tuple[str, str]] = []
    for file in sorted(directory.iterdir()):
        if not file.is_file() or file.name.startswith(prefix):
            continue
        target = file.with_name(prefix + file.name)
        if target.exists():
            print(f"Пропущено: '{target.name}' уже существует.")
            continue
        file.rename(target)
        renamed.append((file.name, target.name))
    return renamed


def main() -> None:
    raw = input("Введите путь к папке (Enter — текущая): ").strip()
    directory = Path(raw) if raw else Path.cwd()
    if not directory.is_dir():
        print("Указанная папка не существует.")
        return
    renamed = add_prefix(directory, PREFIX)
    if not renamed:
        print("Нечего переименовывать.")
        return
    for old, new in renamed:
        print(f"{old} -> {new}")


if __name__ == "__main__":
    main()
