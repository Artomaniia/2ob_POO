import threading
import time

# 1. Базовый (не потокобезопасный) класс счётчика
class SimpleCounter:
    """Обычный счётчик без синхронизации."""
    def __init__(self, initial=0):
        self._value = initial

    def increment(self):
        self._value += 1
        return self._value

    def decrement(self):
        self._value -= 1
        return self._value

    def get_value(self):
        return self._value


# 2. Класс-миксин, добавляющий потокобезопасность
class ThreadSafeMixin:
    """
    Миксин для потокобезопасного доступа к счётчику.
    Требует, чтобы класс-потомок реализовывал методы:
    increment(), decrement(), get_value().
    Сам по себе этот класс не предназначен для прямого использования.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lock = threading.Lock()   # блокировка для синхронизации

    def increment(self):
        with self._lock:
            return super().increment()

    def decrement(self):
        with self._lock:
            return super().decrement()

    def get_value(self):
        with self._lock:
            return super().get_value()


# 3. Итоговый класс – комбинация миксина и базового счётчика
class ThreadSafeCounter(ThreadSafeMixin, SimpleCounter):
    """Потокобезопасный счётчик, собранный из миксина и базовой реализации."""
    pass


# ---------- Демонстрация работы ----------
if __name__ == "__main__":
    counter = ThreadSafeCounter(initial=0)

    def worker(updates):
        for _ in range(updates):
            counter.increment()
            time.sleep(0.0001)  # маленькая задержка для увеличения шанса race condition

    threads = []
    num_threads = 5
    increments_per_thread = 1000

    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(increments_per_thread,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Ожидаемое значение: {num_threads * increments_per_thread}")
    print(f"Реальное значение счётчика: {counter.get_value()}")