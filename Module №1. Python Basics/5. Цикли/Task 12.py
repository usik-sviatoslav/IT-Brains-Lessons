
# Завдання №12. Напишіть програму, яка обчислює факторіал заданого числа.

while True:
    number = int(input("Введіть число: "))
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"{number}! = {result}", "\n")
