
# Завдання №10. Напишіть функцію, яка приймає два рядки та повертає True, якщо вони є анаграмами
# (тобто містять однакові букви в різному порядку), і False - в іншому випадку.

def function_10(str_1, str_2):
    """ Функція аналізує дві вхідні строки та перевіряє чи є вони анаграмами """
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    # Порівнює довжину строк
    if len(str_1) != len(str_2):
        return False

    letter_count = {}

    # Підраховує кількість букв у першої строки, та додає дані у словник
    for letter in str_1:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Підраховує кількість букв у другої строки, та змінює словник
    for letter in str_2:
        if letter in letter_count:
            letter_count[letter] -= 1
        else:
            return False

    # Перевіряємо, чи всі значення в словнику рівні нулю
    for count in letter_count.values():
        if count != 0:
            return False

    return True


input_str_1 = input("Введіть перший рядок: ")
input_str_2 = input("Введіть другий рядок: ")

if function_10(input_str_1, input_str_2):
    print(f"Рядки '{input_str_1}' та '{input_str_2}' є анаграмами.")
else:
    print(f"Рядки '{input_str_1}' та '{input_str_2}' не є анаграмами.")
