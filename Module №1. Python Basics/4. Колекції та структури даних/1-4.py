# У вас є два словники, dict1 і dict2, кожен з яких містить інформацію про людей.
# dict1 має ключі ім'я, прізвище та вік, а dict2 має ключі телефон, email та стать.
# Напишіть функцію, яка об'єднує ці два словники в один словник для кожної людини,
# зберігаючи всю інформацію в одному місці.


# Завдання №1
print("Завдання №1")
dict1 = {
    "name": "Sviatoslav",
    "lastname": "Usik",
    "age": 23,
}
dict2 = {
    "phone": "+380662416907",
    "email": "usik.sviatoslv.qa@gmail.com",
    "sex": "Male",
}
dict1.update(dict2)
print(dict1)


# У вас є список чисел, вам потрібно створити новий список,
# який буде мати лише унікальні значення зі списку 1


# Завдання №2
print("Завдання №2")

list_1 = [3, 7, 2, 4, 3, 7, 2, 6, 7, 3]
unique_list = list(set(list_1))

print(list_1)
print(unique_list)


# У вас є 2 кортежі, ваша задача повернути кортеж у якому є лише ті елементи,
# які є у першому кортежі та немає у другому


# Завдання №3
print("Завдання №3")

tuple_1 = (4, 2, 5, 6, 8)
tuple_2 = (1, 6, 4, 2, 9)
tuple_new = tuple(set(tuple_1).symmetric_difference(set(tuple_2)))

print(tuple_new)


"""
----- Додаткова перевірка знань -----

List (Список):
1. Створіть пустий список і додайте до нього 5 різних цілих чисел. Виведіть цей список.
2. Знайдіть найбільше і найменше число в списку і виведіть їх.
3. Заповніть список рядками, введеними користувачем, доки він не введе слово "stop". Потім виведіть отриманий список.

Tuple (Кортеж):
1. Створіть кортеж, що містить декілька назв кольорів. Виведіть його.
2. Змініть один елемент кортежу на нове значення і виведіть оновлений кортеж.
3. Знайдіть кількість входжень певного значення в кортежі.

Dict (Словник):
1. Створіть словник, де ключами будуть назви фруктів, а значеннями - кількість цих фруктів. Виведіть словник.
2. Додайте новий елемент до словника.
3. Видаліть елемент зі словника за ключем.

Set (Множина):
1. Створіть дві множини з числами. Об'єднайте їх і виведіть результат.
2. Знайдіть перетин двох множин і виведіть результат.
3. Додайте новий елемент до множини.

"""


# List (Список):
# Завдання №1
list_1 = []
print(list_1)
list_update = [1, 5, 9, 7, 4]
list_1 = list(list_update)
print(list_1)

# Завдання №2
list_1 = [1, 21, 59, -45, 86, -46, 52]
print(min(list_1))
print(max(list_1))

# Завдання №3
list_1 = []
while True:
    list_from_user = input("Запиши щось у список: ")
    if list_from_user == "stop":
        break
    else:
        list_1.append(list_from_user)
print(list_1)


# Tuple (Кортеж):
# Завдання №1
colors = ("red", "green", "blue")
print(colors)

# Завдання №2
colors = ("red", "green", "blue", "red")
print(f"Було: {colors}")

replace_color_on = ("yellow", )
colors = colors[:3] + replace_color_on + colors[4:]
print(f"Стало: {colors}")


# Завдання №3
fruits = ("pear", "orange", "kiwi", "raspberry", "strawberry",
          "banana", "pomegranate", "pineapple", "pear", "orange",
          "apricot", "banana", "raspberry", "apple", "cherry",
          "raspberry", "apple", "pineapple", "cherry", "raspberry",
          "lemon", "kiwi", "raspberry", "apple")
count_of_fruits = fruits.count("raspberry")
print(count_of_fruits)


# Dict (Словник):
# Завдання №1
fruits = {
    "pear": 165,
    "orange": 235,
    "kiwi": 40,
    "raspberry": 68,
    "strawberry": 176,
    "banana": 65,
    "pomegranate": 37,
    "pineapple": 92,
    "apricot": 67,
    "apple": 188,
    "cherry": 149,
    "lemon": 87,
}
print(fruits)


# Завдання №2
fruits = {
    "pear": 165,
    "orange": 235,
    "pineapple": 92,
    "apricot": 67,
    "apple": 188,
    "cherry": 149,
    "lemon": 87,
}
print(fruits)
fruits.update({
    "kiwi": 40,
    "raspberry": 68,
    "strawberry": 176,
    "banana": 65,
})
print(fruits)


# Завдання №3
fruits = {
    "pear": 165,
    "orange": 235,
    "pineapple": 92,
    "apricot": 67,
    "apple": 188,
    "cherry": 149,
    "lemon": 87,
}
print(fruits)
remove_key = ["apple", "lemon", "pineapple"]
for key in remove_key:
    fruits.pop(key, None)
print(fruits)


# Set (Множина):
# Завдання №1
first = set("456")
second = set("ad")

value = first.union(second)
print(value)


# Завдання №2
first = set("218sad")
second = set("sdh138")

value = first.intersection(second)
print(value)


# Завдання №3
first = set("218sad")
second = set("adh232")
value = first.union(second)
print(value)
