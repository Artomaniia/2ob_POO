# Перегрузка

**Автор:** Бойко Мария

## Что такое перегрузка?

**Перегрузка (Overloading)** — это возможность использовать одно и то же имя функции или метода для разных типов или количества аргументов.

## Пример в Python

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))      # 5
print(calc.add(2, 3, 4))   # 9
