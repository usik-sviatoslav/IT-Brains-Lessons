
# Завдання №4. Напишіть функцію, яка приймає список рядків і повертає новий список, в якому всі рядки
# переведені у верхній регістр.

def function_4(*args):
    """ Функція переводить рядки у верхній регістр """
    result = "\n".join(args).upper()
    return result


print("Введіть список рядків:")
input_string = ""
while True:
    next_string = input()
    if next_string == "":
        break
    input_string += next_string + "\n"

print(function_4(*input_string.split("\n")))
