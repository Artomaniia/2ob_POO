// В Java полиморфизм требует явного объявления интерфейса
// или наследования. Без них код не скомпилируется.

interface Speakable {
    String speak();
}

class Dog implements Speakable {
    @Override
    public String speak() {
        return "Гав!";
    }
}

class Cat implements Speakable {
    @Override
    public String speak() {
        return "Мяу!";
    }
}

public class Main {
    // Метод принимает только объекты, реализующие интерфейс Speakable
    public static void makeSpeak(Speakable entity) {
        System.out.println(entity.speak());
    }

    public static void main(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();

        makeSpeak(dog);  // Гав!
        makeSpeak(cat);  // Мяу!

        // Попытка передать объект без реализации интерфейса
        // вызовет ошибку компиляции, в отличие от Python
    }
}
