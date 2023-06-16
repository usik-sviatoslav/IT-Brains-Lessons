
# Завдання №14. Напишіть функцію, яка отримує на вхід рядок і повертає словник, що містить кількість
# символів у рядку. Для підрахунку кількості символів у рядку метод count використовувати НЕ дозволяється.

def function_14(string):
    """ Функція рахує кількість кожного символу у рядку """
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


input_string = input("Введіть речення: ")
print(function_14(input_string))
