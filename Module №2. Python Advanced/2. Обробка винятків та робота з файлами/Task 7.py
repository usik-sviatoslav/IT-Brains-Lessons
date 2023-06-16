
# Завдання №7. Реалізуйте програму, яка копіює вміст одного файлу в інший.

while True:
    try:
        input_1 = input("Введіть директорію файлу, вміст котрого треба скопіювати у інший файл: ")
        file_1 = open(input_1, "r")

        input_2 = input("Введіть директорію файлу куди треба скопіювати: ")
        file_2 = open(input_2, "r+")

        file_2.write(file_1.read())
        file_1.close()
        file_2.close()
        print("Вміст файлу скопійовано!\n")
    except FileNotFoundError:
        print("Файлу за даною директорією не знайдено!\n")
