from __future__ import annotations

from abc import ABC, abstractmethod


class Request:
    def __init__(self, path: str, headers: dict[str, str], body: dict) -> None:
        self.path = path
        self.headers = headers
        self.body = body
        self.trace: list[str] = []


class Handler(ABC):
    def __init__(self) -> None:
        self._next: Handler | None = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler

    def handle(self, request: Request) -> str:
        result = self.process(request)
        if result is not None:
            return result
        if self._next is not None:
            return self._next.handle(request)
        return "200 OK"

    @abstractmethod
    def process(self, request: Request) -> str | None: ...


class AuthMiddleware(Handler):
    def process(self, request: Request) -> str | None:
        request.trace.append("auth")
        if request.headers.get("Authorization") != "Bearer token":
            return "401 Unauthorized"
        return None


class LoggingMiddleware(Handler):
    def process(self, request: Request) -> str | None:
        request.trace.append("logging")
        return None


class ValidationMiddleware(Handler):
    def process(self, request: Request) -> str | None:
        request.trace.append("validation")
        if "name" not in request.body:
            return "400 Bad Request"
        return None


class FinalHandler(Handler):
    def process(self, request: Request) -> str | None:
        request.trace.append("handler")
        return f"200 OK: Привет, {request.body['name']}"


def build_chain() -> Handler:
    auth = AuthMiddleware()
    auth.set_next(LoggingMiddleware()).set_next(ValidationMiddleware()).set_next(FinalHandler())
    return auth


def main() -> None:
    chain = build_chain()
    ok = Request("/api", {"Authorization": "Bearer token"}, {"name": "Serega"})
    print("Успешный:", chain.handle(ok), "| trace:", ok.trace)

    no_auth = Request("/api", {}, {"name": "X"})
    print("Без авторизации:", chain.handle(no_auth), "| trace:", no_auth.trace)

    bad = Request("/api", {"Authorization": "Bearer token"}, {})
    print("Невалидный:", chain.handle(bad), "| trace:", bad.trace)


if __name__ == "__main__":
    main()
