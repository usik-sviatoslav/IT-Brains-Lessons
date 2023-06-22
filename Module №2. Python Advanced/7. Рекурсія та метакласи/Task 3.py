
# Завдання №3. Напишіть рекурсивну функцію, яка перевертає вхідний рядок.


def reverse_str(string):
    if len(string) == 0:
        return string
    return string[len(string) - 1:] + reverse_str(string[:-1])


print(reverse_str("Hello"))
