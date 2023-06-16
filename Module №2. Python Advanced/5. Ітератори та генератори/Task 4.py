
# Завдання №4. Напишіть генератор, який видає послідовність квадратів чисел від 1 до N.

def sqrt(n):
    for i in range(1, n + 1):
        yield i ** 2


num = int(input("Послідовність квадратів чисел від 1 до "))
for number in sqrt(num):
    print(number)
