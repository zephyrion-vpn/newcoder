from __future__ import annotations

try:
    import time
    from fastapi import Depends, FastAPI, HTTPException, Request  # type: ignore
    from pydantic import BaseModel, Field, field_validator  # type: ignore
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False


if HAS_FASTAPI:
    app = FastAPI(title="Демо API")

    class Item(BaseModel):
        name: str = Field(min_length=2, max_length=50)
        price: float = Field(gt=0)
        tags: list[str] = Field(default_factory=list)

        @field_validator("tags")
        @classmethod
        def unique_tags(cls, value: list[str]) -> list[str]:
            if len(value) != len(set(value)):
                raise ValueError("Теги должны быть уникальны.")
            return value

    _db: dict[int, Item] = {}

    def get_db() -> dict[int, Item]:
        return _db

    @app.middleware("http")
    async def add_timing(request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed = (time.perf_counter() - start) * 1000
        response.headers["X-Process-Time-ms"] = f"{elapsed:.2f}"
        return response

    @app.post("/items/{item_id}")
    def create_item(item_id: int, item: Item, db: dict = Depends(get_db)) -> dict:
        if item_id in db:
            raise HTTPException(status_code=409, detail="Уже существует.")
        db[item_id] = item
        return {"id": item_id, "item": item.model_dump()}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, db: dict = Depends(get_db)) -> dict:
        if item_id not in db:
            raise HTTPException(status_code=404, detail="Не найдено.")
        return {"id": item_id, "item": db[item_id].model_dump()}


def main() -> None:
    print(f"FastAPI доступен: {HAS_FASTAPI}")
    if not HAS_FASTAPI:
        print("Для запуска установите: pip install fastapi uvicorn")
        print("Запуск: uvicorn 04_fastapi_rest:app --reload")
        return
    print("Приложение создано. Запуск: uvicorn 04_fastapi_rest:app --reload")
    print("Эндпоинты: POST /items/{id}, GET /items/{id}; middleware добавляет X-Process-Time-ms")


if __name__ == "__main__":
    main()
