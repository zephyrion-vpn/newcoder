import os
import tempfile


def parse_ini(path: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    section = ""
    result[section] = {}
    with open(path, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line[0] in ("#", ";"):
                continue
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1].strip()
                result.setdefault(section, {})
            elif "=" in line:
                key, _, value = line.partition("=")
                result.setdefault(section, {})[key.strip()] = value.strip()
    if not result[""]:
        del result[""]
    return result


def main() -> None:
    path = tempfile.mktemp(suffix=".ini")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(
            "; комментарий\n"
            "[database]\n"
            "host = localhost\n"
            "port = 5432\n"
            "\n"
            "[app]\n"
            "name = demo\n"
            "debug = true\n"
        )
    config = parse_ini(path)
    for section, values in config.items():
        print(f"[{section}] -> {values}")
    os.remove(path)


if __name__ == "__main__":
    main()
