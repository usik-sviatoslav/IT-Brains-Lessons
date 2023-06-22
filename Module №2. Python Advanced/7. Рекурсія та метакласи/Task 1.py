
# Завдання №1. Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.


def sum_digits(n):
    d_list = [int(i) for i in str(n)]
    return f"Сума чисел = {recursion(d_list, 0)}"


def recursion(d_list, result):
    if len(d_list) == 1:
        result += d_list.pop()
        return result
    result += d_list.pop()
    return recursion(d_list, result)


print(sum_digits(12345))
