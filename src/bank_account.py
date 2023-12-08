class BankAccount:
    """
    __account_numbers - зберігає всі унікальні номери рахунків
    account_id - індекс в масиві account_numbers,
        що визначає номер створеного рахунку
    balance - поточний баланс
    """
    __account_numbers = []

    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def get_account_number(self):
        """
        Повертає номер рахунку
        """
        return self.__account_numbers[self.account_id]

    def get_balance(self):
        """
        Повертає баланс на рахунку
        """
        return self.balance

    def deposit(self, amount):
        """
        Приймає суму внесення і додає її до балансу рахунку
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Приймає суму зняття і відповідно зменшує балансу рахунку,
        якщо на рахунку достатньо коштів
        """
        if self.balance >= amount:
            self.balance -= amount
            print(f"Операція успішна: -{amount}грн., "
                  f"залишок на рахунку: {self.balance}грн.")
        else:
            print("Недостатньо коштів на рахунку. "
                  f"Ваш рахунок: {self.balance}грн.")

    @staticmethod
    def create_account(account_number, start_balance):
        """
        Приймає номер рахунку та початковий баланс, створює та повертає
        об'єкт класу BankAccount, якщо переданий номер рахунку є унікальним.
        Інакше повертає None.
        """
        if account_number not in BankAccount.__account_numbers:
            BankAccount.__account_numbers.append(account_number)
            account_id = len(BankAccount.__account_numbers) - 1
            return BankAccount(account_id, start_balance)
        else:
            print("Номер рахунку не унікальний, введіть інший номер")
            return None


if __name__ == "__main__":
    account1 = BankAccount.create_account("12157", 25000)
    account2 = BankAccount.create_account("75368", 60000)

    print(account1.get_account_number())
    print(account1.get_balance())

    print(account1.deposit(2000))
    print(account1.withdraw(5000))

    print(account2.withdraw(65000))
