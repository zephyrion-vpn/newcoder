from __future__ import annotations

import re
from typing import Any

USERS = {
    1: {"id": 1, "name": "Alice", "post_ids": [10, 11]},
    2: {"id": 2, "name": "Bob", "post_ids": [12]},
}
POSTS = {
    10: {"id": 10, "title": "Привет мир", "author_id": 1},
    11: {"id": 11, "title": "Python рокс", "author_id": 1},
    12: {"id": 12, "title": "GraphQL", "author_id": 2},
}


def _parse_fields(block: str) -> dict[str, Any]:
    block = block.strip()
    if block.startswith("{"):
        block = block[1:-1]  # убираем обрамляющие скобки
    fields: dict[str, Any] = {}
    tokens = re.findall(r"\w+|\{|\}", block)
    stack: list[dict[str, Any]] = [fields]
    pending: str | None = None
    for token in tokens:
        if token == "{":
            new: dict[str, Any] = {}
            stack[-1][pending] = new
            stack.append(new)
        elif token == "}":
            stack.pop()
        else:
            stack[-1][token] = None
            pending = token
    return fields


def _resolve_user(user: dict, fields: dict[str, Any]) -> dict:
    result: dict[str, Any] = {}
    for field, subfields in fields.items():
        if field == "posts":
            result["posts"] = [
                _resolve_post(POSTS[pid], subfields or {"id": None, "title": None})
                for pid in user["post_ids"]
            ]
        elif field in user:
            result[field] = user[field]
    return result


def _resolve_post(post: dict, fields: dict[str, Any]) -> dict:
    result: dict[str, Any] = {}
    for field, subfields in fields.items():
        if field == "author":
            result["author"] = _resolve_user(USERS[post["author_id"]], subfields or {"name": None})
        elif field in post:
            result[field] = post[field]
    return result


def execute(query: str) -> dict:
    match = re.search(r"user\s*\(\s*id\s*:\s*(\d+)\s*\)\s*(\{.*\})", query, re.DOTALL)
    if not match:
        raise ValueError("Поддерживается только user(id: N) { ... }")
    user_id = int(match.group(1))
    fields = _parse_fields(match.group(2))
    if user_id not in USERS:
        return {"data": {"user": None}}
    return {"data": {"user": _resolve_user(USERS[user_id], fields)}}


def main() -> None:
    import json

    query = """
    user(id: 1) {
        name
        posts {
            title
            author { name }
        }
    }
    """
    result = execute(query)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
