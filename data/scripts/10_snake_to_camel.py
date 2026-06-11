import re


def snake_to_camel(text: str) -> str:
    return re.sub(r"_+([a-zA-Z0-9])", lambda m: m.group(1).upper(), text)


def main() -> None:
    for value in ["snake_case", "my_variable_name", "already", "with__double", "trailing_"]:
        print(f"{value} -> {snake_to_camel(value)}")


if __name__ == "__main__":
    main()
