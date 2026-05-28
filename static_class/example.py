class UnitConverter:
    """Статический класс для конвертации единиц."""

    def __new__(cls, *args, **kwargs):
        raise TypeError("UnitConverter — статический класс")

    @staticmethod
    def km_to_miles(km: float) -> float:
        return km * 0.621371

    @staticmethod
    def miles_to_km(miles: float) -> float:
        return miles / 0.621371

    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return c * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f: float) -> float:
        return (f - 32) * 5/9

    @classmethod
    def meters_to_feet(cls, m: float) -> float:
        """Можно использовать classmethod, если нужна поддержка наследования."""
        return m * 3.28084

print(UnitConverter.km_to_miles(10))           # 6.21371
print(UnitConverter.celsius_to_fahrenheit(25)) # 77.0
print(UnitConverter.meters_to_feet(5))         # 16.4042
