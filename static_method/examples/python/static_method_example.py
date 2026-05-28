class TemperatureConverter:
    """
    Класс для конвертации температур между различными шкалами.

    Демонстрирует использование статических методов в Python.
    Все методы объявлены как @staticmethod — они не зависят
    от состояния экземпляра или класса.
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Перевод температуры из Цельсия в Фаренгейт.

        :param celsius: Температура в градусах Цельсия
        :return: Температура в градусах Фаренгейта
        """
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Перевод температуры из Фаренгейта в Цельсий.

        :param fahrenheit: Температура в градусах Фаренгейта
        :return: Температура в градусах Цельсия
        """
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """
        Перевод температуры из Цельсия в Кельвины.

        :param celsius: Температура в градусах Цельсия
        :return: Температура в Кельвинах
        """
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """
        Перевод температуры из Кельвинов в Цельсий.

        :param kelvin: Температура в Кельвинах
        :return: Температура в градусах Цельсия
        """
        return kelvin - 273.15

    @staticmethod
    def is_valid_kelvin(kelvin: float) -> bool:
        """
        Проверка допустимости значения в Кельвинах.

        :param kelvin: Проверяемое значение
        :return: True, если значение >= 0 (не ниже абсолютного нуля)
        """
        return kelvin >= 0

    @staticmethod
    def describe_temperature(celsius: float) -> str:
        """
        Словесное описание температуры.

        :param celsius: Температура в градусах Цельсия
        :return: Текстовое описание
        """
        if celsius < 0:
            return "Мороз"
        elif celsius < 15:
            return "Холодно"
        elif celsius < 25:
            return "Комфортно"
        elif celsius < 35:
            return "Тепло"
        else:
            return "Жара"


# ── Вызов через имя класса (без создания объекта) ──────────────────────────

temp_c = 100.0
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
temp_k = TemperatureConverter.celsius_to_kelvin(temp_c)

print(f"{temp_c}°C = {temp_f}°F")           # 100.0°C = 212.0°F
print(f"{temp_c}°C = {temp_k} K")           # 100.0°C = 373.15 K

print(TemperatureConverter.fahrenheit_to_celsius(32))   # 0.0
print(TemperatureConverter.kelvin_to_celsius(0))        # -273.15

# ── Валидация ───────────────────────────────────────────────────────────────

print(TemperatureConverter.is_valid_kelvin(300))   # True
print(TemperatureConverter.is_valid_kelvin(-5))    # False

# ── Описание температуры ────────────────────────────────────────────────────

for t in [-10, 10, 22, 30, 40]:
    desc = TemperatureConverter.describe_temperature(t)
    print(f"{t}°C — {desc}")

# ── Вызов через экземпляр (работает, но не рекомендуется) ──────────────────

converter = TemperatureConverter()
print(converter.celsius_to_fahrenheit(0))   # 32.0

# Статический метод не имеет доступа к self или cls
# Он работает как обычная функция внутри пространства имён класса

