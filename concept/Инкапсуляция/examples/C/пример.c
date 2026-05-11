#include <stdio.h>
#include <string.h>

/*
 * Демонстрация инкапсуляции на языке C.
 *
 * В языке C отсутствуют встроенные механизмы
 * объектно-ориентированного программирования,
 * поэтому инкапсуляция реализуется через структуры
 * и функции для работы с данными.
 */


/*
 * Структура банковского счёта.
 */
typedef struct {
    char owner[50];
    double balance;
} BankAccount;


/*
 * Инициализация банковского счёта.
 *
 * account — указатель на структуру счёта
 * owner — имя владельца
 * balance — начальный баланс
 */
void init_account(
    BankAccount *account,
    const char *owner,
    double balance
) {
    strcpy(account->owner, owner);
    account->balance = balance;
}


/*
 * Получение текущего баланса.
 *
 * Возвращает значение баланса счёта.
 */
double get_balance(BankAccount *account) {
    return account->balance;
}


/*
 * Пополнение банковского счёта.
 *
 * amount — сумма пополнения.
 */
void deposit(BankAccount *account, double amount) {

    if (amount > 0) {
        account->balance += amount;

        printf(
            "Счёт пополнен на %.2f\n",
            amount
        );
    } else {
        printf(
            "Сумма должна быть положительной\n"
        );
    }
}


/*
 * Снятие средств со счёта.
 *
 * amount — сумма снятия.
 */
void withdraw(BankAccount *account, double amount) {

    if (
        amount > 0 &&
        amount <= account->balance
    ) {
        account->balance -= amount;

        printf(
            "Снято %.2f\n",
            amount
        );
    } else {
        printf(
            "Недостаточно средств\n"
        );
    }
}


/*
 * Точка входа в программу.
 */
int main() {

    /* Создание банковского счёта */
    BankAccount account;

    /* Инициализация счёта */
    init_account(
        &account,
        "Алексей",
        1000
    );

    /* Вывод текущего баланса */
    printf(
        "Текущий баланс: %.2f\n",
        get_balance(&account)
    );

    /* Пополнение счёта */
    deposit(&account, 500);

    printf(
        "Баланс после пополнения: %.2f\n",
        get_balance(&account)
    );

    /* Снятие средств */
    withdraw(&account, 300);

    printf(
        "Баланс после снятия: %.2f\n",
        get_balance(&account)
    );

    return 0;
}
