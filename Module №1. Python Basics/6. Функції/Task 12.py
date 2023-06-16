
# Завдання №12. Напишіть функцію, яка отримує необмежену кількість рядків як аргументи та
# повертає один об'єднаний рядок.

def function_12_1():
    """ Функція дає можливість вводити необмежену кількість рядків """
    print("Введіть рядки, наприклад вірш:")
    print("(Для завершення вводу натисніть Enter двічі)")
    strings = "".split()

    while True:
        next_string = input()
        if next_string == "":
            break
        strings += next_string + "\n"

    return strings


def function_12_2(*args):
    """ Функція об'єднує рядок та видаляє з нього розділові знаки """

    from re import split

    string = "".join(args)
    delimiters = "[,.;!? \n]"
    split_string = split(delimiters, string)
    new_string = "".join(split_string).lower()

    return new_string


print(function_12_2(*function_12_1()))
