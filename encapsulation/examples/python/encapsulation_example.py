class BankAccount:
    """
    Класс банковского счёта.

    Демонстрирует принцип инкапсуляции в Python.
    Поле __balance скрыто от прямого доступа извне.
    """

    def __init__(self, owner: str, balance: float):
        """
        Инициализация банковского счёта.

        :param owner: Владелец счёта
        :param balance: Начальный баланс
        """
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self) -> float:
        """
        Получение текущего баланса.

        :return: Текущий баланс счёта
        """
        return self.__balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счёта.

        :param amount: Сумма пополнения
        """
        if amount > 0:
            self.__balance += amount
            print(f"Счёт пополнен на {amount}")
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств со счёта.

        :param amount: Сумма снятия
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято {amount}")
        else:
            print("Недостаточно средств")


# Создание объекта банковского счёта
account = BankAccount("Алексей", 1000)

# Вывод текущего баланса
print(f"Текущий баланс: {account.balance}")

# Пополнение счёта
account.deposit(500)
print(f"Баланс после пополнения: {account.balance}")

# Снятие средств
account.withdraw(300)
print(f"Баланс после снятия: {account.balance}")

# Прямой доступ к скрытому полю невозможен
# print(account.__balance)  # AttributeError

