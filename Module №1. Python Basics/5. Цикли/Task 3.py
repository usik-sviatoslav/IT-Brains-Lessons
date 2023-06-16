
# Завдання №3. Напишіть програму яка приймає на вхід рядок і повертає рядок де кожен
# символ з першого рядка буде продубльовано. Наприклад “hello” → “hheelllloo”

while True:
    input_string = input("Введіть текст: ")
    if input_string == "":
        break
    for letter in input_string:
        print(letter * 2, end="")
    print("\n")
