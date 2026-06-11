from __future__ import annotations

import os
import tempfile
from types import TracebackType
from typing import Optional, TextIO


class Logger:
    def __init__(self, path: str) -> None:
        self.path = path
        self._handle: Optional[TextIO] = None

    def __enter__(self) -> "Logger":
        self._handle = open(self.path, "a", encoding="utf-8")
        return self

    def log(self, message: str) -> None:
        if self._handle is None:
            raise RuntimeError("Logger используется вне контекстного менеджера.")
        self._handle.write(message + "\n")

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if self._handle is not None:
            self._handle.close()
            self._handle = None


def main() -> None:
    path = os.path.join(tempfile.gettempdir(), "app.log")
    with Logger(path) as logger:
        logger.log("Старт приложения")
        logger.log("Обработка данных")
    with open(path, encoding="utf-8") as handle:
        print(handle.read().strip())


if __name__ == "__main__":
    main()
