
# Завдання №4. Реалізуйте функцію, яка ділить два числа, але обробляє помилку **`ZeroDivisionError`**,
# якщо друге число дорівнює нулю.

def divide_numbers():
    """ Функція ділить два числа і відстежує помилки """
    try:
        number_1 = int(input("Введи перше число: "))
        number_2 = int(input("Введи друге число: "))
        result = number_1 / number_2
        return f"{result}\n"
    except ValueError:
        return "Число не введено.\n"
    except ZeroDivisionError:
        return "На нуль ділити не можна!\n"


while True:
    print(divide_numbers())
