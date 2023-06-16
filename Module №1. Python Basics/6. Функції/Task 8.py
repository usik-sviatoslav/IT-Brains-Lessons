
# Завдання №8. Напишіть функцію, яка приймає рядок і повертає кількість голосних літер у цьому рядку.

vowels = {
    "UA": ["А", "а", "Е", "е", "Є", "є", "И", "и", "І", "і", "Ї", "ї", "О", "о", "У", "у", "Ю", "ю", "Я", "я"],
    "EN": ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
}


def function_8(letters):
    """ Функція рахує кількість голосних літер у тексті """
    count_vowels = 0
    if input_string.isdigit():
        return "Ви ввели замість тексту числа!"
    elif input_string == "":
        return "Нічого рахувати"
    for letter in letters:
        if letter in vowels["UA"] or letter in vowels["EN"]:
            count_vowels += 1
    return "Кількість голосних: " + str(count_vowels)


while True:
    input_string = input("Введіть текст, а я підрахую кількість голосних у цьому тексті:\n")
    if input_string == ".":
        print("Ви вишли з програми")
        break
    print(function_8(input_string))
