
# Завдання №2. Напишіть генератор, який повертає послідовність чисел Фібоначчі.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


func = fibonacci(20)
for num in func:
    print(num)
