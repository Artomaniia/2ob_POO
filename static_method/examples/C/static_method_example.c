/*
 * Статический метод — аналог на языке C
 *
 * В C нет классов и методов в том смысле, что есть в Python.
 * Аналогом статического метода в C являются обычные функции,
 * которые не принимают указатель на структуру (т.е. не зависят
 * от состояния объекта). Группировка достигается через соглашение
 * об именовании с префиксом "модуля".
 *
 * Ниже реализован аналог класса TemperatureConverter из Python-примера.
 */

#include <stdio.h>

/* === Аналог "класса" TemperatureConverter через префикс TC_ === */

/* Аналог @staticmethod: перевод из Цельсия в Фаренгейт */
double TC_celsius_to_fahrenheit(double celsius) {
    return celsius * 9.0 / 5.0 + 32.0;
}

/* Аналог @staticmethod: перевод из Фаренгейта в Цельсий */
double TC_fahrenheit_to_celsius(double fahrenheit) {
    return (fahrenheit - 32.0) * 5.0 / 9.0;
}

/* Аналог @staticmethod: перевод из Цельсия в Кельвины */
double TC_celsius_to_kelvin(double celsius) {
    return celsius + 273.15;
}

/* Аналог @staticmethod: перевод из Кельвинов в Цельсий */
double TC_kelvin_to_celsius(double kelvin) {
    return kelvin - 273.15;
}

/* Аналог @staticmethod: проверка допустимости значения в Кельвинах */
int TC_is_valid_kelvin(double kelvin) {
    return kelvin >= 0.0;
}

/* Аналог @staticmethod: словесное описание температуры */
const char* TC_describe_temperature(double celsius) {
    if (celsius < 0)    return "Мороз";
    if (celsius < 15)   return "Холодно";
    if (celsius < 25)   return "Комфортно";
    if (celsius < 35)   return "Тепло";
    return "Жара";
}

/* === Точка входа === */
int main() {
    double temp_c = 100.0;
    double temp_f = TC_celsius_to_fahrenheit(temp_c);
    double temp_k = TC_celsius_to_kelvin(temp_c);

    printf("%.1f C = %.1f F\n", temp_c, temp_f);   /* 100.0 C = 212.0 F */
    printf("%.1f C = %.2f K\n", temp_c, temp_k);   /* 100.0 C = 373.15 K */

    printf("32 F = %.1f C\n", TC_fahrenheit_to_celsius(32.0));   /* 0.0 */
    printf("0 K = %.2f C\n",  TC_kelvin_to_celsius(0.0));        /* -273.15 */

    /* Валидация */
    printf("300 K допустимо? %s\n", TC_is_valid_kelvin(300) ? "Да" : "Нет");
    printf("-5 K допустимо?  %s\n", TC_is_valid_kelvin(-5)  ? "Да" : "Нет");

    /* Описание температур */
    double temps[] = {-10.0, 10.0, 22.0, 30.0, 40.0};
    int n = sizeof(temps) / sizeof(temps[0]);
    for (int i = 0; i < n; i++) {
        printf("%.0f C — %s\n", temps[i], TC_describe_temperature(temps[i]));
    }

    return 0;
}
