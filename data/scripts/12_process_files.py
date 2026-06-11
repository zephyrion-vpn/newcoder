import os
import tempfile
from pathlib import Path


def process_files(paths: list[Path]) -> tuple[dict[str, int], list[str]]:
    results: dict[str, int] = {}
    failed_files: list[str] = []
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as handle:
                results[str(path.name)] = len(handle.read())
        except (OSError, UnicodeDecodeError) as error:
            failed_files.append(f"{path.name} ({type(error).__name__})")
            continue
    return results, failed_files


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    good1 = tmp / "good1.txt"
    good1.write_text("привет", encoding="utf-8")
    good2 = tmp / "good2.txt"
    good2.write_text("hello world", encoding="utf-8")
    binary = tmp / "binary.bin"
    binary.write_bytes(b"\xff\xfe\x00\x01\x80")
    missing = tmp / "does_not_exist.txt"

    results, failed = process_files([good1, good2, binary, missing])
    print("Успешно прочитано:")
    for name, size in results.items():
        print(f"   {name}: {size} символов")
    print("\nНе удалось прочитать:")
    for name in failed:
        print(f"   {name}")
    print(f"\nВсего ошибок: {len(failed)}, обработка не прервалась.")


if __name__ == "__main__":
    main()
