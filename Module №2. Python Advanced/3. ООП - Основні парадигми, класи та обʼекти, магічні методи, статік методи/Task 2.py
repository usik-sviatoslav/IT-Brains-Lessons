
# Завдання №2. Розробіть клас BankAccount для представлення банківського рахунку. Додайте методи для зняття
# та поповнення коштів на рахунку. Використовуйте магічний метод __str__ для виведення інформації про рахунок.

class BankAccount:
    def __init__(self, firstname, lastname, email, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.balance = balance

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Не достатньо коштів на рахунку!")
        else:
            self.balance -= amount

    def info(self):
        return f"Ім'я: {self.firstname}\n" \
               f"Прізвище: {self.lastname}\n" \
               f"Баланс на рахунку: ${self.balance:_}\n".replace("_", ".")

    def __str__(self):
        return f"Баланс на рахунку: ${self.balance:_}\n".replace("_", ".")


print()
id2416907 = BankAccount("Святослав", "Усік", "usik.sviatoslav@gmail.com", 0)
print(id2416907.info())

deposit_amount = int(input("Поповнення рахунку: $"))
id2416907.deposit(deposit_amount)
print(id2416907)

withdraw_amount = int(input("Зняття з рахунку: $"))
id2416907.withdraw(withdraw_amount)
print(id2416907)
