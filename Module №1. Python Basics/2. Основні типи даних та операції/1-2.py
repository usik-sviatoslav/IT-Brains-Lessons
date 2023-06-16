while True:
    print()
    task = int(input("Введіть номер завдання: "))
    if task == 0:
        break

    # Завдання №1
    elif task == 1:
        print("Завдання №1")

        greeting = "Hello, "
        name = "Sviatoslav"
        print(greeting+name)
        print()

    # Завдання №2
    elif task == 2:
        print("Завдання №2")

        number1 = 20
        x = number1
        number2 = 6
        y = number2
        number3 = x + y
        number4 = x - y
        number5 = x * y
        number6 = x / y
        number7 = x ** y
        number8 = x // y
        number9 = x % y
        print(number3, number4, number5, number6, number7, number8, number9, sep="; ")
        print()

    # Завдання №3
    elif task == 3:
        print("Завдання №3")

        value = input("Введіть число: ")
        if value.isnumeric():
            value = int(value)
            print("Тип даних —", type(value), "\n")
        else:
            print("Ви ввели текст, замість числа", "\n" "Тип даних —", type(value), "\n")

    # Завдання №4
    elif task == 4:
        print("Завдання №4")

        value_1 = input("Введіть число: ")
        if value_1.isnumeric():
            value_1 = int(value_1)
        else:
            print("Ви ввели текст, замість числа", "\n")

        value_2 = input("Введіть друге число: ")
        if value_2.isnumeric():
            value_2 = int(value_2)
            print("Результат:", "\n")
        else:
            print("Ви ввели текст, замість числа", "\n")

        print("Додавання =", value_1 + value_2)
        print("Віднімання =", value_1 - value_2)
        print("Множення =", value_1 * value_2)
        print("Ділення =", value_1 / value_2)
        print("Возведення у ступінь =", value_1 ** value_2)
        print("Цілочисленне ділення =", value_1 // value_2)
        print("Остача при діленні =", value_1 % value_2)
        print()

    # Завдання №5
    elif task == 5:
        print("Завдання №5")
        import datetime

        username = input("Введіть своє ім'я: ")
        birth_year = int(input("Введіть свій рік народження: "))
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        print("Привіт, " + username + "! Тобі зараз " + str(age) + " років.")
        print()

    # Завдання №---
    elif task >= 6:
        print("Святослав, таких завдань ти ще не робив!", "\n")
        