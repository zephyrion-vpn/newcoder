import os


def relative_path(source: str, target: str) -> str:
    return os.path.relpath(target, start=source)


def main() -> None:
    print(relative_path("/home/user/projects/app", "/home/user/projects/lib/utils"))
    print(relative_path("/home/user/docs", "/home/user/docs/2024/report.txt"))
    print(relative_path("/var/log", "/etc/config"))


if __name__ == "__main__":
    main()
