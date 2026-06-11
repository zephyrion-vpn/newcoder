import os
import tempfile


def parse_ini(path: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    section = ""
    result[section] = {}
    with open(path, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith(("#", ";")):
                continue
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1].strip()
                result.setdefault(section, {})
            elif "=" in line:
                key, _, value = line.partition("=")
                result[section][key.strip()] = value.strip()
    if not result[""]:
        del result[""]
    return result


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "config.ini")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("[database]\nhost = localhost\nport = 5432\n\n[app]\ndebug = true\n")
    config = parse_ini(path)
    print(config)


if __name__ == "__main__":
    main()
