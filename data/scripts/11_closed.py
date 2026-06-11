def main() -> None:
    path = "/tmp/py_closed_demo.txt"
    file = open(path, "w", encoding="utf-8")
    print(file.closed)
    file.close()
    print(file.closed)


if __name__ == "__main__":
    main()
