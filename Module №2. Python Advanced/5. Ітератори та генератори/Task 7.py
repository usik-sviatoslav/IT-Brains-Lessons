
# Завдання №7. Створіть ітератор, який перебирає всі парні числа з заданого діапазону.

class Iterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.index]
        if self.numbers[self.index] % 2 == 0:
            self.index += 2
            return result
        else:
            self.index += 1


print("Парні числа заданого діапазону")
num_1, num_2 = int(input("Перше число: ")), int(input("Друге число: "))
for i in Iterator(list(range(num_1, num_2 + 1))):
    print(i)
