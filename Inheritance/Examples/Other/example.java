import java.util.ArrayList;
import java.util.List;

abstract class Employee {
    protected String name;
    protected int age;
    protected double salary;

    public Employee(String name, int age, double salary) {
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    // Абстрактный метод (обязателен для переопределения)
    public abstract void work();

    public void showInfo() {
        System.out.println("\n========================");
        System.out.println("Имя: " + name);
        System.out.println("Возраст: " + age);
        System.out.println("Зарплата: " + salary);
    }

    public double getSalary() {
        return salary;
    }

    public void raiseSalary(double amount) {
        if (amount > 0) {
            salary += amount;
            System.out.println(name + " получил повышение на " + amount);
        }
    }
}


class Developer extends Employee {
    private String language;

    public Developer(String name, int age, double salary, String language) {
        super(name, age, salary);
        this.language = language;
    }

    @Override
    public void work() {
        System.out.println(name + " пишет код на " + language);
    }

    public void fixBug() {
        System.out.println(name + " исправляет баги");
    }

    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("Должность: Разработчик");
        System.out.println("Язык: " + language);
    }
}

class Designer extends Employee {
    private String tool;

    public Designer(String name, int age, double salary, String tool) {
        super(name, age, salary);
        this.tool = tool;
    }

    @Override
    public void work() {
        System.out.println(name + " создаёт дизайн в " + tool);
    }

    public void createMockup() {
        System.out.println(name + " делает макет интерфейса");
    }

    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("Должность: Дизайнер");
        System.out.println("Инструмент: " + tool);
    }
}


class Manager extends Employee {
    private int teamSize;

    public Manager(String name, int age, double salary, int teamSize) {
        super(name, age, salary);
        this.teamSize = teamSize;
    }

    @Override
    public void work() {
        System.out.println(name + " управляет командой из " + teamSize + " человек");
    }

    public void holdMeeting() {
        System.out.println(name + " проводит собрание");
    }

    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("Должность: Менеджер");
        System.out.println("Размер команды: " + teamSize);
    }
}

public class Main {
    public static void main(String[] args) {

        List<Employee> employees = new ArrayList<>();

        employees.add(new Developer("Алексей", 25, 120000, "Java"));
        employees.add(new Designer("Мария", 23, 90000, "Figma"));
        employees.add(new Manager("Дмитрий", 35, 150000, 10));

        // Полиморфизм + наследование
        double totalSalary = 0;

        for (Employee e : employees) {
            e.showInfo();
            e.work();
            totalSalary += e.getSalary();
        }

        System.out.println("\n========================");
        System.out.println("Общий фонд зарплат: " + totalSalary);
    }
}
