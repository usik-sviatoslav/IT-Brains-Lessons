
# Завдання №1. Обробіть виняток IndexError, коли програма намагається отримати доступ
# до неправильного індексу в списку.

products = ["Яблука", "Банани", "Мандарини", "Полуниця"]
while True:
    index_of_product = input("Введи номер товару: ")
    if index_of_product.isnumeric():
        try:
            print(products[int(index_of_product)], "\n")
        except IndexError:
            print("Товару за таким номером не існує.", "\n")
    else:
        continue
