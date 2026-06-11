import pickle


class UserSession:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self._password = password  # чувствительное
        self._cache: dict[str, object] = {}  # временное
        self.connection = object()  # несериализуемый ресурс

    def cache_value(self, key: str, value: object) -> None:
        self._cache[key] = value

    def __getstate__(self) -> dict[str, object]:
        state = self.__dict__.copy()
        state.pop("_password", None)
        state.pop("_cache", None)
        state.pop("connection", None)
        return state

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        self._password = None  # восстанавливаем пустыми
        self._cache = {}
        self.connection = object()


def main() -> None:
    session = UserSession("serega", "super-secret")
    session.cache_value("token", "abc123")

    blob = pickle.dumps(session)
    print(f"Пароль в байтах pickle: {b'super-secret' in blob}")
    print(f"Токен в байтах pickle: {b'abc123' in blob}")

    restored: UserSession = pickle.loads(blob)
    print(f"\nПосле восстановления:")
    print(f"   username: {restored.username}")
    print(f"   _password: {restored._password}")
    print(f"   _cache: {restored._cache}")
    print(f"   connection пересоздан: {restored.connection is not None}")


if __name__ == "__main__":
    main()
