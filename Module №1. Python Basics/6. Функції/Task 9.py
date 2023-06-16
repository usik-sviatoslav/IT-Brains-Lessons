
# Завдання №9. Напишіть функцію, яка приймає список чисел і повертає новий список, в якому всі числа помножені на 2.

def function_9(nums):
    """ Функція повертає новий список в якому всі числа будуть помножені на 2 """
    result = []
    for number in nums:
        number *= 2
        result.append(number)
    return result


input_numbers = input("Введіть числа через пробіл: ")
numbers = [int(i) for i in input_numbers.split()]
print(function_9(numbers))
