class User:
    def __init__(self, name: str, age: int):
        self._name = name      # защищённое имя (соглашение)
        self._age = age        # защищённое поле

    # Getter
    @property
    def name(self) -> str:
        """Возвращает имя пользователя."""
        return self._name.capitalize()

    # Setter
    @name.setter
    def name(self, value: str):
        """Устанавливает имя с валидацией."""
        if not value or not isinstance(value, str):
            raise ValueError("Имя должно быть непустой строкой")
        self._name = value.strip()

    # Getter для возраста
    @property
    def age(self) -> int:
        return self._age

    # Setter с валидацией
    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or value < 0 or value > 120:
            raise ValueError("Возраст должен быть целым числом от 0 до 120")
        self._age = value

    # Deleter
    @age.deleter
    def age(self):
        """Удаляет информацию о возрасте (например, по просьбе пользователя)."""
        print(f"Информация о возрасте пользователя {self._name} удалена.")
        del self._age
