class StaticMath:
    """
    Статический класс для математических операций.
    Создание экземпляров запрещено.
    """

    # Статический атрибут (константа)
    PI = 3.14159

    def __new__(cls, *args, **kwargs):
        """Запрещаем создание объектов."""
        raise TypeError(f"Класс {cls.__name__} — статический, инстанцирование невозможно")

    @staticmethod
    def add(a, b):
        """Сложение."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Вычитание."""
        return a - b

    @staticmethod
    def circle_area(radius):
        """Площадь круга."""
        return StaticMath.PI * radius ** 2

    @classmethod
    def multiply(cls, a, b):
        """Умножение (используем classmethod для доступа к атрибутам класса, если нужно)."""
        return a * b

# Пример использования (без создания экземпляра)
if __name__ == "__main__":
    print(StaticMath.add(10, 5))          # 15
    print(StaticMath.subtract(10, 5))     # 5
    print(StaticMath.multiply(6, 7))      # 42
    print(StaticMath.circle_area(5))      # 78.53975
    print(StaticMath.PI)                  # 3.14159

    # Попытка создать объект вызовет ошибку:
    # obj = StaticMath()  # TypeError: класс StaticMath — статический...
