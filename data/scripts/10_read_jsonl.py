import json
import os
import tempfile
from typing import Any, Iterator


def read_jsonl(path: str) -> Iterator[dict[str, Any]]:
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def main() -> None:
    path = os.path.join(tempfile.gettempdir(), "demo.jsonl")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write('{"id": 1, "name": "Анна"}\n')
        handle.write('\n')
        handle.write('{"id": 2, "name": "Борис"}\n')
    for record in read_jsonl(path):
        print(record)


if __name__ == "__main__":
    main()
