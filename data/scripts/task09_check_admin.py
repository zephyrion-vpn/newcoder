import ctypes
import os
import sys


def is_admin() -> bool:
    if os.name == "nt":
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        except (AttributeError, OSError):
            return False
    return os.geteuid() == 0


def main() -> None:
    if is_admin():
        print("Скрипт запущен с правами администратора.")
        return
    print("Предупреждение: скрипт запущен без прав администратора.", file=sys.stderr)
    raise SystemExit(1)


if __name__ == "__main__":
    main()
