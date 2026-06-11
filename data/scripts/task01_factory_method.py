from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    @abstractmethod
    def parse(self, raw: str) -> dict[str, Any]:
        ...


class JsonParser(Parser):
    def parse(self, raw: str) -> dict[str, Any]:
        import json

        return json.loads(raw)


class XmlParser(Parser):
    def parse(self, raw: str) -> dict[str, Any]:
        import xml.etree.ElementTree as ElementTree

        root = ElementTree.fromstring(raw)
        return {child.tag: child.text for child in root}


class YamlParser(Parser):
    def parse(self, raw: str) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for line in raw.strip().splitlines():
            if not line.strip() or ":" not in line:
                continue
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip()
        return result


def create_parser(fmt: str) -> Parser:
    parsers: dict[str, type[Parser]] = {
        "json": JsonParser,
        "xml": XmlParser,
        "yaml": YamlParser,
    }
    try:
        return parsers[fmt.lower()]()
    except KeyError:
        raise ValueError(f"Неизвестный формат: {fmt}") from None


def main() -> None:
    samples = {
        "json": '{"name": "Анна", "age": 30}',
        "xml": "<user><name>Анна</name><age>30</age></user>",
        "yaml": "name: Анна\nage: 30",
    }
    for fmt, raw in samples.items():
        parser = create_parser(fmt)
        print(f"{fmt}: {parser.parse(raw)}")


if __name__ == "__main__":
    main()
