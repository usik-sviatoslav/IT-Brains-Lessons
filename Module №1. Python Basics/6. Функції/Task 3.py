
# Завдання №3. Напишіть функцію, яка приймає список чисел і повертає найбільше число зі списку.
# Функцію max використовувати не можна.

def function_3(nums: list):
    """ Функція повертає найбільше число зі списку """
    if not len(nums):
        return "Нічого не введено"
    result = nums[0]
    for number in nums:
        if number > result:
            result = number
    return "Найбільше число зі списку: " + str(result)


input_numbers = input("Введіть числа через пробіл: ")

numbers = []
for i in input_numbers.split():
    numbers.append(int(i))

print(function_3(numbers))
