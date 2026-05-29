"""
Пример: перегрузка методов в Python
Автор: Бойко Мария
"""

class OverloadDemo:
    def show(self, *args):
        if len(args) == 1:
            print(f"Один аргумент: {args[0]}")
        elif len(args) == 2:
            print(f"Два аргумента: {args[0]} и {args[1]}")
        else:
            print(f"Аргументов: {len(args)} -> {args}")

    def greet(self, name, greeting="Привет"):
        print(f"{greeting}, {name}!")


demo = OverloadDemo()

demo.show(42)
demo.show(10, 20)
demo.show(1, 2, 3)

demo.greet("Анна")
demo.greet("Петр", "Здравствуйте")