
# Завдання №6. Напишіть функцію, яка обчислює факторіал заданого числа і повертає результат.

def function_6(number):
    """ Функція обчислює факторіал """
    while True:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result


while True:
    input_number = int(input("Введіть число: "))
    if input_number < 0:
        print("Помилка. Факторіал від від'ємного числа не обчислюється")
        break
    print(function_6(input_number), "\n")
