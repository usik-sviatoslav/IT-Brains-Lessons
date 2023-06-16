# # # Завдання №1
# print("Завдання №1")
# while True:
#     number = int(input("Введіть число: "))
#     if number % 2 == 0:
#         print(f"Число {number} - парне", "\n")
#     else:
#         print(f"Число {number} - непарне", "\n")
#
#
# # # Завдання №2
# print("Завдання №2")
# while True:
#     number_1 = int(input("Введіть перше число: "))
#     number_2 = int(input("Введіть друге число: "))
#     if number_1 > number_2:
#         print(f"{number_1} більше за {number_2}", "\n")
#     elif number_1 < number_2:
#         print(f"{number_2} більше за {number_1}", "\n")
#     else:
#         print(f"{number_1} дорівнює {number_2}", "\n")
#
#
# # # Завдання №3
# print("Завдання №3")
# while True:
#     water_temperature = int(input("Введіть температуру води: "))
#     if water_temperature >= 100:
#         print("Кип'яток", "\n")
#     elif water_temperature >= 45:
#         print("Гаряча", "\n")
#     elif water_temperature >= 20:
#         print("Тепла", "\n")
#     else:
#         print("Холодна", "\n")
#
#
# # # Завдання №4
# print("Завдання №4")
# while True:
#     value = int(input("Введіть число кратне 5: "))
#     if value % 5 == 0:
#         print(f"Так, число {value} кратне 5", "\n")
#     else:
#         print(f"Число {value} не кратне 5", "\n")
#
#
# # # Завдання №5
# print("Завдання №5")
# days_in_month = [
#     (1, "У січні 31 день"),
#     (2, "У лютому 28 день"),
#     (3, "У березні 31 день"),
#     (4, "У квітні 30 день"),
#     (5, "У травні 31 день"),
#     (6, "У червні 30 день"),
#     (7, "У липні 31 день"),
#     (8, "У серпні 31 день"),
#     (9, "У вересні 30 день"),
#     (10, "У жовтні 31 день"),
#     (11, "У листопаді 30 день"),
#     (12, "У грудні 31 день"),
# ]
#
#
# def get_days_in_month(month: int) -> str:
#     for value in days_in_month:
#         if month == value[0]:
#             return value[1]
#
#
# while True:
#     try:
#         month_number = int(input("Введіть число місяця: "))
#         if 12 >= month_number >= 1:
#             break
#         else:
#             print("Число повинно бути від 1 до 12", "\n")
#     except ValueError:
#         print("Помилка: введіть ціле число", "\n")
#
# days_in_month = get_days_in_month(month_number)
# print(days_in_month)
#
#
# # # Завдання №6
#
# print("Завдання №6")
# while True:
#     number_of_year = input("Введіть число року: ")
#     while len(number_of_year) != 4 or not number_of_year.isdigit():
#         number_of_year = input("Помилка! Введіть 4-х значне число: ")
#
#     if int(number_of_year) % 4 == 0:
#         print(f"{number_of_year} високосний рік", "\n")
#     else:
#         print(f"{number_of_year} не є високосним роком", "\n")
#
#
# print("Завдання №6")
#
# while True:
#     number_of_year = input("Введіть число року: ")
#     while len(number_of_year) != 4 or not number_of_year.isdigit():
#         number_of_year = input("Помилка! Введіть ціле 4-х значне число: ")
#
#     if int(number_of_year) % 4 == 0:
#         print(f"{number_of_year} високосний рік", "\n")
#         print("Продовжити?")
#         question = input("Натисни \"Enter\" або напиши \"exit\" для виходу ")
#         if question == "":
#             print()
#             continue
#         elif question == "exit":
#             print("Ви вийшли з програми")
#             break
#     else:
#         print(f"{number_of_year} не є високосним роком", "\n")
#
#
# # # Завдання №7
# print("Завдання №7")
#
# while True:
#     number_1 = input("Введіть перше число: ")
#     while number_1:
#         if number_1.isalpha():
#             number_1 = input("Помилка! Ви ввели текст замість числа. Введіть число: ")
#         elif number_1.replace(".", "", 1).isdigit():
#             number_1 = float(number_1)
#             break
#         else:
#             number_1 = input("Помилка! Ви ввели оператор замість числа. Введіть число: ")
#
#     number_2 = input("Введіть друге число: ")
#     while number_2:
#         if number_2.isalpha():
#             number_2 = input("Помилка! Ви ввели текст замість числа. Введіть число: ")
#         elif number_2.replace(".", "", 1).isdigit():
#             number_2 = float(number_2)
#             break
#         else:
#             number_2 = input("Помилка! Ви ввели оператор замість числа. Введіть число: ")
#
#     operator = input("Введіть оператор: ")
#     while operator:
#         if operator.isalpha():
#             operator = input("Помилка! Ви ввели текст замість оператору. Введіть оператор: ")
#         elif operator.isdigit():
#             operator = input("Помилка! Ви ввели число замість оператору. Введіть оператор: ")
#         elif operator == "+":
#             print(f"{number_1} {operator} {number_2} =", number_1 + number_2)
#             break
#         elif operator == "-":
#             print(f"{number_1} {operator} {number_2} =", number_1 - number_2)
#             break
#         elif operator == "*":
#             print(f"{number_1} {operator} {number_2} =", number_1 * number_2)
#             break
#         elif operator == "/" and number_2 != 0:
#             print(f"{number_1} {operator} {number_2} =", number_1 / number_2)
#             break
#         elif operator == "/" and number_2 == 0:
#             print("Помилка! Неможливо ділити на нуль.")
#             break
#         else:
#             operator = input("Помилка! Введіть інший оператор: ")
#     print()
