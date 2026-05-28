class Point:
    """Точка на плоскости с координатами x и y."""

    def __init__(self, x: float, y: float) -> None:
        """Стандартный конструктор — задаёт координаты точки."""
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords: tuple) -> "Point":
        """Создать точку из кортежа (x, y)."""
        return cls(coords[0], coords[1])

    @classmethod
    def from_string(cls, s: str) -> "Point":
        """Создать точку из строки формата 'x,y', например '3.0,4.5'."""
        x, y = map(float, s.split(","))
        return cls(x, y)

    @classmethod
    def origin(cls) -> "Point":
        """Создать точку в начале координат (0, 0)."""
        return cls(0.0, 0.0)

    def distance_to(self, other: "Point") -> float:
        """Вернуть расстояние от этой точки до другой (теорема Пифагора)."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


# ── Стандартный конструктор __init__ ────────────────────────────────────────

p1 = Point(3.0, 4.0)
print(p1)                       # Point(3.0, 4.0)

# ── Фабричный конструктор: from_tuple ───────────────────────────────────────

p2 = Point.from_tuple((1.0, 2.0))
print(p2)                       # Point(1.0, 2.0)

# ── Фабричный конструктор: from_string ──────────────────────────────────────

p3 = Point.from_string("5.0,7.5")
print(p3)                       # Point(5.0, 7.5)

# ── Именованный конструктор: origin ─────────────────────────────────────────

p4 = Point.origin()
print(p4)                       # Point(0.0, 0.0)

# ── Методы объекта ──────────────────────────────────────────────────────────

print(p1.distance_to(p4))       # 5.0  (3² + 4² = 5²)
print(p1 == Point(3.0, 4.0))    # True
print(p1 == p2)                 # False
