
# Завдання №2. Напишіть програму, яка отримує на вхід рядок і перевіряє, чи є він паліндромом.
# Паліндром - це рядок який читається однаково з початку до кінця і з кінця у початок

while True:
    input_string = input("Введіть рядок: ")
    string = ""
    if input_string == "":
        break
    for letter in input_string:
        if not letter.isalpha():
            continue
        string += letter

    string_1 = string.lower()
    string_2 = string_1[::-1]
    if string_1 == string_2:
        print("Введений рядок є паліндромом", "\n")
    else:
        print("Введений рядок не є паліндромом", "\n")
