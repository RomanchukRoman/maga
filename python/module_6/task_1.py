class BankAccount:
    'Класс для управления банковским счетом.'
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner = owner
        self._balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        self._balance += float(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете.")
        self._balance -= float(amount)

    def get_balance(self):
        return(self._balance)

# Пример использования
try:
    acc = BankAccount("Тестовый Пользователь", 500)
    print(f"Баланс: {acc.get_balance()}")
    acc.deposit(150)
    print(f"Баланс после пополнения: {acc.get_balance()}")
    acc.withdraw(100)
    print(f"Баланс после снятия: {acc.get_balance()}")
    acc.withdraw(600)  # Эта операция должна вызвать ошибку
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    acc_invalid = BankAccount("Невалидный", -100)
except ValueError as e:
    print(f"Ошибка создания счета: {e}") 