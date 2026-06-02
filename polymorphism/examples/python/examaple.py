# Демонстрация двух видов полиморфизма:
# 1. Классический — через наследование
# 2. Pythonic way — через утиную типизацию

# === Полиморфизм через наследование ===
class Animal:
    def speak(self):
        raise NotImplementedError("Подкласс должен реализовать этот метод")

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

# Единая функция, работающая с любым Animal
def make_animal_speak(animal: Animal):
    print(animal.speak())

# === Полиморфизм через утиную типизацию ===
class Car:
    """Этот класс не наследуется от Animal, но имеет метод speak."""
    def speak(self):
        return "Бип-бип!"

# Та же функция работает с любым объектом, имеющим метод speak
def make_anything_speak(entity):
    print(entity.speak())

# Использование
dog = Dog()
cat = Cat()
car = Car()

make_animal_speak(dog)   # Гав!
make_animal_speak(cat)   # Мяу!
make_anything_speak(car) # Бип-бип! — работает благодаря утиной типизации
