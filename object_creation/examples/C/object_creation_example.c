/*
 * Создание объектов — аналог на языке C
 *
 * В C нет классов, однако аналог "объекта" реализуется через структуры (struct).
 * Аналогом конструктора (__init__) служит функция-инициализатор,
 * а альтернативным конструкторам (@classmethod) соответствуют
 * вспомогательные функции-фабрики с соглашением именования по префиксу.
 *
 * Ниже реализован аналог класса Point из Python-примера.
 */

#include <stdio.h>
#include <math.h>

/* === Структура "класса" Point === */

typedef struct {
    double x;
    double y;
} Point;

/* Аналог __init__: стандартное создание точки по координатам */
Point point_create(double x, double y) {
    Point p;
    p.x = x;
    p.y = y;
    return p;
}

/* Аналог @classmethod from_tuple: создание из массива двух чисел */
Point point_from_array(double coords[2]) {
    return point_create(coords[0], coords[1]);
}

/* Аналог @classmethod from_string: создание из строки "x,y" */
Point point_from_string(const char *s) {
    double x, y;
    sscanf(s, "%lf,%lf", &x, &y);
    return point_create(x, y);
}

/* Аналог @classmethod origin: создание точки в начале координат */
Point point_origin(void) {
    return point_create(0.0, 0.0);
}

/* Аналог метода distance_to */
double point_distance(Point a, Point b) {
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
}

/* Аналог __repr__ */
void point_print(Point p) {
    printf("Point(%.1f, %.1f)\n", p.x, p.y);
}

/* Аналог __eq__ */
int point_equal(Point a, Point b) {
    return a.x == b.x && a.y == b.y;
}

/* === Точка входа === */
int main(void) {
    /* Аналог Point(3.0, 4.0) */
    Point p1 = point_create(3.0, 4.0);
    point_print(p1);                    /* Point(3.0, 4.0) */

    /* Аналог Point.from_tuple((1.0, 2.0)) */
    double coords[2] = {1.0, 2.0};
    Point p2 = point_from_array(coords);
    point_print(p2);                    /* Point(1.0, 2.0) */

    /* Аналог Point.from_string("5.0,7.5") */
    Point p3 = point_from_string("5.0,7.5");
    point_print(p3);                    /* Point(5.0, 7.5) */

    /* Аналог Point.origin() */
    Point p4 = point_origin();
    point_print(p4);                    /* Point(0.0, 0.0) */

    /* Расстояние */
    printf("Distance: %.1f\n", point_distance(p1, p4));  /* 5.0 */

    /* Сравнение */
    Point p1_copy = point_create(3.0, 4.0);
    printf("p1 == p1_copy: %s\n", point_equal(p1, p1_copy) ? "True" : "False"); /* True  */
    printf("p1 == p2:      %s\n", point_equal(p1, p2)      ? "True" : "False"); /* False */

    return 0;
}
