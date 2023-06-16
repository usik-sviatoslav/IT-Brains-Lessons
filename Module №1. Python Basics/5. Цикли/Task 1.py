
# Завдання №1. Напишіть програму, яка отримує на вхід рядок і підраховує кількість голосних у ньому.

vowels = {
    "UA": ["А", "а", "Е", "е", "Є", "є", "И", "и", "І", "і", "Ї", "ї", "О", "о", "У", "у", "Ю", "ю", "Я", "я"],
    "EN": ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
}

while True:
    count = 0
    input_string = input("Введіть текст, а я підрахую кількість голосних у цьому тексті:\n")
    if input_string.isdigit():
        print("Ви ввели замість тексту число!")
        continue
    elif input_string == "":
        break
    for letter in input_string:
        if letter in vowels["UA"] or letter in vowels["EN"]:
            count += 1
    print(f"Кількість голосних: {count}", "\n")
