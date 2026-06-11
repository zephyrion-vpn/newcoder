import os
import tempfile
from pathlib import Path


def inspect_symlink(path: Path) -> str:
    if not path.is_symlink():
        return f"{path.name}: не является символической ссылкой"
    target = os.readlink(path)
    resolved = path.resolve()
    status = "(существует)" if resolved.exists() else "(битая ссылка)"
    return f"{path.name}: симлинк -> {target} {status}"


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    real = tmp / "real_file.txt"
    real.write_text("содержимое", encoding="utf-8")

    link = tmp / "link_to_file"
    try:
        link.symlink_to(real)
        has_symlink = True
    except (OSError, NotImplementedError):
        has_symlink = False
        print("Симлинки недоступны в этой среде.")

    print(inspect_symlink(real))
    if has_symlink:
        print(inspect_symlink(link))


if __name__ == "__main__":
    main()
