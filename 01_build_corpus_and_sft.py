import argparse
import ast
import json
import random
import re
from pathlib import Path
from collections import Counter


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def safe_parse(code: str):
    try:
        return ast.parse(code)
    except SyntaxError:
        return None


def node_code(source: str, node) -> str:
    lines = source.splitlines()
    if hasattr(node, "lineno") and hasattr(node, "end_lineno"):
        return "\n".join(lines[node.lineno - 1:node.end_lineno])
    return ""


def args_of(fn):
    if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return []
    args = []
    for a in list(fn.args.posonlyargs) + list(fn.args.args) + list(fn.args.kwonlyargs):
        if a.arg not in ("self", "cls"):
            args.append(a.arg)
    if fn.args.vararg:
        args.append("*" + fn.args.vararg.arg)
    if fn.args.kwarg:
        args.append("**" + fn.args.kwarg.arg)
    return args


def call_names(node):
    names = []
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name):
                names.append(f.id)
            elif isinstance(f, ast.Attribute):
                names.append(f.attr)
    return names


def features(code: str, node=None):
    names = set(call_names(node)) if node else set()
    text = code.lower()
    feats = []
    if "socket" in text or names & {"recv", "send", "sendall", "bind", "listen", "accept", "connect"}:
        feats.append("сетевыми соединениями")
    if "async def " in code or "asyncio" in text:
        feats.append("асинхронным выполнением")
    if "threading" in text or names & {"Thread", "start", "join"}:
        feats.append("потоками")
    if "open(" in code or "pathlib" in text or names & {"read_text", "write_text", "rename", "unlink", "mkdir"}:
        feats.append("файлами")
    if names & {"print"}:
        feats.append("выводом в консоль")
    if names & {"input"}:
        feats.append("вводом пользователя")
    if node and any(isinstance(x, (ast.For, ast.While, ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)) for x in ast.walk(node)):
        feats.append("итерацией по данным")
    if node and any(isinstance(x, ast.If) for x in ast.walk(node)):
        feats.append("условной логикой")
    if node and any(isinstance(x, ast.Raise) for x in ast.walk(node)):
        feats.append("проверками и исключениями")
    return feats


def describe_return(expr):
    try:
        s = ast.unparse(expr)
    except Exception:
        s = "результат"
    if len(s) > 80:
        s = s[:77] + "..."
    if re.fullmatch(r"\w+ \+ \w+", s):
        return f"результат сложения `{s}`"
    return f"значение выражения `{s}`"


def explain_function(fn, code: str) -> str:
    name = fn.name
    args = args_of(fn)
    returns = [n.value for n in ast.walk(fn) if isinstance(n, ast.Return) and n.value is not None]
    calls = set(call_names(fn))
    feats = features(code, fn)
    prefix = "Асинхронная функция" if isinstance(fn, ast.AsyncFunctionDef) else "Функция"
    parts = []
    if name == "main":
        parts.append(f"{prefix} `main` является точкой входа скрипта и запускает основную логику.")
    else:
        parts.append(f"{prefix} `{name}` выполняет логику, связанную с {', '.join(feats[:2]) if feats else 'показанным фрагментом кода'}.")
    if args:
        parts.append("Она принимает аргументы: " + ", ".join(f"`{a}`" for a in args) + ".")
    else:
        parts.append("Она не принимает явных пользовательских аргументов.")
    if "input" in calls:
        parts.append("Во время работы она запрашивает ввод пользователя через `input`.")
    if "print" in calls:
        parts.append("Часть результата выводится через `print`.")
    if returns:
        parts.append("Функция возвращает " + ", ".join(describe_return(r) for r in returns[:2]) + ".")
    else:
        parts.append("Явного полезного значения она не возвращает." if ("print" in calls or "input" in calls) else "В коде нет явного возврата значения.")
    return " ".join(parts)


def explain_class(cls, code: str) -> str:
    attrs = set()
    methods = []
    for n in cls.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            methods.append(n.name)
            for x in ast.walk(n):
                if isinstance(x, ast.Attribute) and isinstance(x.value, ast.Name) and x.value.id == "self" and isinstance(x.ctx, ast.Store):
                    attrs.add(x.attr)
    parts = [f"Класс `{cls.name}` объединяет состояние объекта и методы для работы с ним."]
    if attrs:
        parts.append("Основное состояние хранится в атрибутах: " + ", ".join(f"`{a}`" for a in sorted(attrs)[:6]) + ".")
    public = [m for m in methods if not (m.startswith("_") and m not in ("__init__", "__enter__", "__exit__", "__aenter__", "__aexit__"))]
    if public:
        parts.append("Ключевые методы: " + ", ".join(f"`{m}`" for m in public[:6]) + ".")
    return " ".join(parts)


def task_input(task, difficulty, context, code, requirements, output_format):
    req = "".join(f"- {r}\n" for r in requirements)
    return f"""TASK: {task}
DIFFICULTY: {difficulty}

CONTEXT:
{context}

CODE:
{code}

REQUIREMENTS:
{req}
CONSTRAINTS:
- Do not change behavior unless the task asks for it
- Do not invent project behavior

OUTPUT_FORMAT:
{output_format}""".strip()


def make_reasoning(symbol, base_answer):
    return f"""Reasoning Summary:
- Architecture: Код оформлен как самостоятельный фрагмент `{symbol}` с явными входами, внутренней логикой и результатом или побочным эффектом.
- Invariants: Входные данные должны соответствовать проверкам в коде; результат должен следовать только из показанных выражений и ветвлений.
- Trace: Сначала подготавливаются входные значения, затем выполняется основная логика, после чего результат возвращается или выводится.
- Counterfactual: Более сложная архитектура добавила бы лишний слой абстракции и была бы неоправданна для такого размера фрагмента.

Answer:
{base_answer}"""


def make_tests(symbol, node):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = args_of(node)
        if len(args) == 2:
            return f"def test_{symbol}_basic():\n    result = {symbol}(1, 2)\n    assert result is not None"
        if len(args) == 1:
            return f"def test_{symbol}_basic():\n    result = {symbol}(1)\n    assert result is not None"
    return f"def test_{symbol}_exists():\n    assert {symbol} is not None"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scripts_dir", default="data/scripts")
    parser.add_argument("--out_dir", default="data/processed")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    random.seed(args.seed)
    scripts_dir = Path(args.scripts_dir)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    py_files = sorted(scripts_dir.rglob("*.py"))
    raw_chunks = []
    explain_texts = []
    examples = []
    idx = 1
    for path in py_files:
        code = read_text(path)
        rel = str(path.relative_to(scripts_dir)).replace("\\", "/")
        raw_chunks.append(f"<|file|>\n{rel}\n\n{code}\n<|end|>\n")
        tree = safe_parse(code)
        if not tree:
            continue
        nodes = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
        for node in nodes[:3]:
            symbol = node.name
            snippet = node_code(code, node) or code[:2000]
            if len(snippet) > 3500:
                snippet = snippet[:3500]
            answer = explain_class(node, snippet) if isinstance(node, ast.ClassDef) else explain_function(node, snippet)
            explain_texts.append(answer)
            examples.append({
                "id": f"example_{idx:06d}",
                "task_type": "explain_simple",
                "difficulty": "basic",
                "source": {"file_path": rel, "symbol": symbol, "language": "Python", "framework": "None"},
                "input": task_input("explain", "basic", f"Explain `{symbol}` from `{rel}`.", snippet, ["Explain what the code does", "Mention arguments and return value if present"], "answer_only"),
                "output": answer,
            })
            idx += 1
            node_len = len(snippet.splitlines())
            if node_len >= 10 or isinstance(node, ast.ClassDef):
                examples.append({
                    "id": f"example_{idx:06d}",
                    "task_type": "explain_with_reasoning",
                    "difficulty": "intermediate" if node_len < 35 else "advanced",
                    "source": {"file_path": rel, "symbol": symbol, "language": "Python", "framework": "None"},
                    "input": task_input("explain_with_reasoning", "intermediate", f"Explain the structure and behavior of `{symbol}`.", snippet, ["Explain architecture", "Explain invariants", "Explain trace briefly"], "reasoning_summary_then_answer"),
                    "output": make_reasoning(symbol, answer),
                })
                idx += 1
            if idx % 5 == 0:
                examples.append({
                    "id": f"example_{idx:06d}",
                    "task_type": "test_simple",
                    "difficulty": "basic",
                    "source": {"file_path": rel, "symbol": symbol, "language": "Python", "framework": "None"},
                    "input": task_input("test", "basic", f"Write a minimal test for `{symbol}`.", snippet, ["Create a small pytest-style test", "Keep it simple"], "test_code"),
                    "output": make_tests(symbol, node),
                })
                idx += 1
    random.shuffle(examples)
    examples = examples[:2500]
    for i, e in enumerate(examples, 1):
        e["id"] = f"example_{i:06d}"
    pretrain_parts = []
    pretrain_parts.extend(raw_chunks)
    for t in explain_texts:
        pretrain_parts.append(f"<|text|>\n{t}\n<|end|>\n")
    for e in examples:
        pretrain_parts.append(f"<|user|>\n{e['input']}\n<|assistant|>\n{e['output']}\n<|end|>\n")
    pretrain = "\n".join(pretrain_parts)
    (out / "pretrain_corpus.txt").write_text(pretrain, encoding="utf-8")
    (out / "tokenizer_corpus.txt").write_text(pretrain, encoding="utf-8")
    with (out / "sft_dataset.jsonl").open("w", encoding="utf-8") as f:
        for e in examples:
            f.write(json.dumps(e, ensure_ascii=False, separators=(",", ":")) + "\n")
    report = {
        "py_files": len(py_files),
        "sft_examples": len(examples),
        "task_counts": dict(Counter(e["task_type"] for e in examples)),
        "pretrain_chars": len(pretrain),
    }
    (out / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
