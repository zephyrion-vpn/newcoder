import os
import sys


def is_admin() -> bool:
    if os.name == "nt":
        import ctypes

        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False
    return os.getuid() == 0


def main() -> None:
    if is_admin():
        print("Скрипт запущен с правами администратора (root)")
    else:
        print("Предупреждение: нет прав администратора", file=sys.stderr)


if __name__ == "__main__":
    main()
