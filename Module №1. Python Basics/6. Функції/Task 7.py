
# Завдання №7. Напишіть функцію, яка приймає список чисел і повертає список, що містить лише парні числа.

def function_7(nums: list):
    """ Приймає список чисел і повертає список, що містить лише парні числа """
    two_digit_numbers = []
    for number in nums:
        if int(number) % 2 == 0:
            two_digit_numbers.append(number)

    return f"Список з парними числами: {two_digit_numbers}"


input_numbers = input("Введіть числа через пробіл: ").split()
print(f"Введений список: {input_numbers}")
print(function_7(input_numbers))
