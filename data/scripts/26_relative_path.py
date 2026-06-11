import os.path


def relative_between(from_dir: str, to_dir: str) -> str:
    return os.path.relpath(to_dir, start=from_dir)


def main() -> None:
    cases = [
        ("/home/user/projects/app", "/home/user/projects/lib"),
        ("/home/user/projects/app/src", "/home/user/docs"),
        ("/var/www/html", "/var/www/html/static/css"),
        ("/a/b/c", "/a/b/c"),
    ]
    for from_dir, to_dir in cases:
        rel = relative_between(from_dir, to_dir)
        print(f"от {from_dir}")
        print(f"  до {to_dir}")
        print(f"  = {rel}\n")


if __name__ == "__main__":
    main()
