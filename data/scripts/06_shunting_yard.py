OPERATORS = {
    "+": (1, "left"),
    "-": (1, "left"),
    "*": (2, "left"),
    "/": (2, "left"),
    "^": (3, "right"),
}


def tokenize(expression: str) -> list[str]:
    tokens: list[str] = []
    number = ""
    for char in expression:
        if char.isdigit() or char == ".":
            number += char
        else:
            if number:
                tokens.append(number)
                number = ""
            if char in OPERATORS or char in "()":
                tokens.append(char)
            elif char.isspace():
                continue
            else:
                raise ValueError(f"Недопустимый символ: {char!r}")
    if number:
        tokens.append(number)
    return tokens


def to_rpn(tokens: list[str]) -> list[str]:
    output: list[str] = []
    stack: list[str] = []
    for token in tokens:
        if token in OPERATORS:
            prec, assoc = OPERATORS[token]
            while stack and stack[-1] in OPERATORS:
                top_prec = OPERATORS[stack[-1]][0]
                if (assoc == "left" and prec <= top_prec) or (assoc == "right" and prec < top_prec):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Несбалансированные скобки.")
            stack.pop()
        else:
            output.append(token)
    while stack:
        if stack[-1] in "()":
            raise ValueError("Несбалансированные скобки.")
        output.append(stack.pop())
    return output


def eval_rpn(rpn: list[str]) -> float:
    stack: list[float] = []
    for token in rpn:
        if token in OPERATORS:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)
        else:
            stack.append(float(token))
    return stack[0]


def evaluate(expression: str) -> float:
    return eval_rpn(to_rpn(tokenize(expression)))


def main() -> None:
    for expr in ("3 + 5 * (2 - 8)", "2 ^ 3 ^ 2", "(1 + 2) * (3 + 4)", "10 / 4"):
        print(f"{expr} = {evaluate(expr)}")


if __name__ == "__main__":
    main()
