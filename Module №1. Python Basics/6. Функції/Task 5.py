
# Завдання №5. Напишіть функцію, яка перевіряє, чи є задане число простим, і повертає True або False.

def function_5(number: int):
    """ Функція перевіряє числа, чи є вони простими """
    if number == 1 or number < 0:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


while True:
    input_number = int(input("Введіть число, я перевіряю, чи є число простим: "))
    if input_number == 0:
        print("Ви вийшли із програми")
        break
    else:
        print(function_5(input_number))
