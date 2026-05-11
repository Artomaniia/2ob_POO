class BankAccount:
    """
    Класс банковского счёта.
    Демонстрирует принцип инкапсуляции.
    """

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self) -> float:
        """
        Геттер для получения баланса.
        """
        return self.__balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счёта.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Счёт пополнен на {amount}")
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств со счёта.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято {amount}")
        else:
            print("Недостаточно средств")


account = BankAccount("Алексей", 1000)

print(f"Текущий баланс: {account.balance}")

account.deposit(500)
print(f"Баланс после пополнения: {account.balance}")

account.withdraw(300)
print(f"Баланс после снятия: {account.balance}")

# Прямой доступ запрещён
# print(account.__balance)  # Ошибка
