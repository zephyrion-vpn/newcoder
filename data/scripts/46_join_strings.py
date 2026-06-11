def join_all(*parts: str) -> str:
    return " ".join(parts)


if __name__ == "__main__":
    print(join_all("Python", "is", "fun"))
