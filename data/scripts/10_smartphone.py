from typing import Any


class Phone:
    def __init__(self, number: str, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.number = number

    def call(self, target: str) -> str:
        return f"Звонок с {self.number} на {target}"


class Camera:
    def __init__(self, megapixels: float, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.megapixels = megapixels

    def take_photo(self) -> str:
        return f"Фото на {self.megapixels} МП"


class Smartphone(Phone, Camera):
    def __init__(self, number: str, megapixels: float, model: str) -> None:
        super().__init__(number=number, megapixels=megapixels)
        self.model = model

    def __str__(self) -> str:
        return f"{self.model}: {self.number}, камера {self.megapixels} МП"


def main() -> None:
    phone = Smartphone("+7-900-000-00-00", 48, "СуперФон")
    print(phone)
    print(phone.call("+7-900-111-11-11"))
    print(phone.take_photo())
    print("MRO:", [cls.__name__ for cls in Smartphone.__mro__])


if __name__ == "__main__":
    main()
