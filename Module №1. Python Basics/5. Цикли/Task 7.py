
# Завдання №7. Напишіть програму, яка підраховує частоту кожного символу у рядку.

while True:
    input_string = input("Введіть текст: ")
    unique_letters = {}
    for letter in input_string:
        if letter in unique_letters:
            unique_letters[letter] += 1
        else:
            unique_letters[letter] = 1

    for letter, count in unique_letters.items():
        print(f"\"{letter}\" зустрічається {count} раз")
