from abc import ABC, abstractmethod

class Employee(ABC):

    company_name = "TechCorp"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self._salary = salary

    @abstractmethod
    def work(self):
        pass

    def show_info(self):
        print("\n==============================")
        print(f"Компания: {Employee.company_name}")
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Зарплата: {self._salary} руб.")
        print("==============================")

    def get_salary(self):
        return self._salary

    def increase_salary(self, amount):
        if amount > 0:
            self._salary += amount
            print(f"\nЗарплата увеличена на {amount} руб.")
        else:
            print("\nОшибка: сумма должна быть положительной.")

class Developer(Employee):

    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def work(self):
        print(f"\n{self.name} пишет код на {self.programming_language}.")

    def fix_bug(self):
        print(f"{self.name} исправляет ошибки в программе.")

    def show_info(self):
        super().show_info()
        print(f"Должность: Разработчик")
        print(f"Язык программирования: {self.programming_language}")

class Designer(Employee):

    def __init__(self, name, age, salary, design_tool):
        super().__init__(name, age, salary)
        self.design_tool = design_tool

    def work(self):
        print(f"\n{self.name} создает дизайн в {self.design_tool}.")

    def create_mockup(self):
        print(f"{self.name} разрабатывает макет интерфейса.")

    def show_info(self):
        super().show_info()
        print(f"Должность: Дизайнер")
        print(f"Инструмент: {self.design_tool}")
      
class Manager(Employee):

    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size

    def work(self):
        print(f"\n{self.name} управляет командой.")

    def hold_meeting(self):
        print(f"{self.name} проводит собрание команды.")

    def show_info(self):
        super().show_info()
        print(f"Должность: Менеджер")
        print(f"Количество сотрудников в команде: {self.team_size}")

def company_report(employees):

    print("\n========== ОТЧЕТ КОМПАНИИ ==========")

    total_salary = 0

    for employee in employees:
        employee.show_info()
        employee.work()
        total_salary += employee.get_salary()

    print(f"Общий фонд зарплат: {total_salary} руб.")
  


dev1 = Developer(
    name="Алексей",
    age=25,
    salary=120000,
    programming_language="Python"
)

designer1 = Designer(
    name="Мария",
    age=23,
    salary=90000,
    design_tool="Figma"
)

manager1 = Manager(
    name="Дмитрий",
    age=35,
    salary=150000,
    team_size=8
)


dev1.fix_bug()
designer1.create_mockup()
manager1.hold_meeting()

dev1.increase_salary(10000)

employees = [dev1, designer1, manager1]

company_report(employees)
