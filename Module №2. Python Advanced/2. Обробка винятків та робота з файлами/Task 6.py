
# Завдання №6. Створіть функцію, яка приймає рядок від користувача та записує його у файл.

def record_data(file_name):
    """ Функція записує дані у файл"""
    try:
        file = open(file_name, "r+")
        file.seek(0)
        print(file.read())
        try:
            file.write("\n")
            file.write(unlimited_rows())
        finally:
            print("Зміни записано!\n")
            file.close()
    except FileNotFoundError:
        print("Файлу за даною директорією не знайдено!\n")


def unlimited_rows():
    """ Функція дає можливість вводити необмежену кількість рядків """
    strings = ""

    while True:
        next_string = input()
        if next_string == "":
            break
        strings += next_string + "\n"

    return strings


while True:
    file_path = input("Введи шлях до файлу: ")
    record_data(file_path)
