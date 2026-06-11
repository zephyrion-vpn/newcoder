import os


def main() -> None:
    directory = "/tmp/py_mkdir_demo"
    if os.path.isdir(directory):
        os.rmdir(directory)
    os.mkdir(directory)
    print(os.path.isdir(directory))


if __name__ == "__main__":
    main()
