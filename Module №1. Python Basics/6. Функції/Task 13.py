
# Завдання №13. Напишіть функцію, яка отримує речення як рядок і повертає кількість слів у цьому реченні.

def function_13(string):
    """ Функція рахує кількість слів у реченні """
    words = [str(i) for i in string.split()]
    count = 0
    for word in words:
        len(word)
        count += 1
    return count


input_string = input("Введіть речення: ")
print(function_13(input_string))
