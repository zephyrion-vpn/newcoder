from abc import ABC, abstractmethod


class Document:
    def __init__(self) -> None:
        self.text = ""


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...

    @abstractmethod
    def undo(self) -> None:
        ...


class InsertText(Command):
    def __init__(self, document: Document, text: str) -> None:
        self._document = document
        self._text = text

    def execute(self) -> None:
        self._document.text += self._text

    def undo(self) -> None:
        self._document.text = self._document.text[: -len(self._text)]


class DeleteLast(Command):
    def __init__(self, document: Document, count: int) -> None:
        self._document = document
        self._count = count
        self._removed = ""

    def execute(self) -> None:
        self._removed = self._document.text[-self._count :]
        self._document.text = self._document.text[: -self._count]

    def undo(self) -> None:
        self._document.text += self._removed


class Editor:
    def __init__(self, document: Document) -> None:
        self._document = document
        self._history: list[Command] = []

    def run(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo(self) -> None:
        if self._history:
            self._history.pop().undo()


def main() -> None:
    document = Document()
    editor = Editor(document)
    editor.run(InsertText(document, "Привет"))
    editor.run(InsertText(document, ", мир"))
    print("После ввода:", document.text)
    editor.run(DeleteLast(document, 4))
    print("После удаления:", document.text)
    editor.undo()
    print("После undo:", document.text)
    editor.undo()
    print("После undo:", document.text)


if __name__ == "__main__":
    main()
