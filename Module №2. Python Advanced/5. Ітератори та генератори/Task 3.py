
# Завдання №3. Створіть ітератор який буде приймати рядок та кожен виклик методу next()
# буде повертати наступний символ рядка.

class Iterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        letter = self.string[self.index]
        self.index += 1
        return letter


line = Iterator(input("Введіть текст: "))
for i in line:
    print(i)
