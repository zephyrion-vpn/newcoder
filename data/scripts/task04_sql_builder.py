from __future__ import annotations


class QueryBuilder:
    def __init__(self) -> None:
        self._table = ""
        self._columns: list[str] = []
        self._conditions: list[str] = []
        self._order_by: list[str] = []
        self._limit: int | None = None
        self._selected = False

    def select(self, *columns: str) -> QueryBuilder:
        if self._selected:
            raise RuntimeError("select() уже вызван")
        self._columns = list(columns) or ["*"]
        self._selected = True
        return self

    def from_table(self, table: str) -> QueryBuilder:
        self._require_select()
        self._table = table
        return self

    def where(self, condition: str) -> QueryBuilder:
        self._require_select()
        self._conditions.append(condition)
        return self

    def order_by(self, *columns: str) -> QueryBuilder:
        self._require_select()
        self._order_by.extend(columns)
        return self

    def limit(self, count: int) -> QueryBuilder:
        self._require_select()
        if count <= 0:
            raise ValueError("limit должен быть положительным")
        self._limit = count
        return self

    def build(self) -> str:
        if not self._selected:
            raise RuntimeError("Сначала вызовите select()")
        if not self._table:
            raise RuntimeError("Не указана таблица (from_table)")
        parts = [f"SELECT {', '.join(self._columns)}", f"FROM {self._table}"]
        if self._conditions:
            parts.append("WHERE " + " AND ".join(self._conditions))
        if self._order_by:
            parts.append("ORDER BY " + ", ".join(self._order_by))
        if self._limit is not None:
            parts.append(f"LIMIT {self._limit}")
        return "\n".join(parts)

    def _require_select(self) -> None:
        if not self._selected:
            raise RuntimeError("Сначала вызовите select()")


def main() -> None:
    query = (
        QueryBuilder()
        .select("id", "name", "price")
        .from_table("products")
        .where("price > 100")
        .where("in_stock = TRUE")
        .order_by("price DESC")
        .limit(10)
        .build()
    )
    print(query)
    try:
        QueryBuilder().from_table("products")
    except RuntimeError as error:
        print("Ошибка порядка:", error)


if __name__ == "__main__":
    main()
