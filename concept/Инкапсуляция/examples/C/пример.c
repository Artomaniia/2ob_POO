#include <stdio.h>
#include <string.h>

/*
 * Демонстрация инкапсуляции на языке C.
 * В C нет встроенной поддержки ООП,
 * поэтому инкапсуляция реализуется через структуры и функции.
 */

typedef struct {
    char owner[50];
    double balance;
} BankAccount;


/*
 * Создание банковского счёта
 */
void init_account(BankAccount *account, const char *owner, double balance) {
    strcpy(account->owner, owner);
    account->balance = balance;
}


/*
 * Получение баланса
 */
double get_balance(BankAccount *account) {
    return account->balance;
}


/*
 * Пополнение счёта
 */
void deposit(BankAccount *account, double amount) {
    if (amount > 0) {
        account->balance += amount;
        printf("Счёт пополнен на %.2f\n", amount);
    } else {
        printf("Сумма должна быть положительной\n");
    }
}


/*
 * Снятие средств
 */
void withdraw(BankAccount *account, double amount) {
    if (amount > 0 && amount <= account->balance) {
        account->balance -= amount;
        printf("Снято %.2f\n", amount);
    } else {
        printf("Недостаточно средств\n");
    }
}


int main() {

    BankAccount account;

    init_account(&account, "Алексей", 1000);

    printf("Текущий баланс: %.2f\n", get_balance(&account));

    deposit(&account, 500);
    printf("Баланс после пополнения: %.2f\n", get_balance(&account));

    withdraw(&account, 300);
    printf("Баланс после снятия: %.2f\n", get_balance(&account));

    return 0;
}
