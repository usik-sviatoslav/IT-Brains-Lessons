
# Завдання №2. Напишіть функцію, яка приймає рядок і повертає його у зворотному порядку

def function_2(string: str):
    """ Функція приймає рядок і повертає його у зворотному порядку """
    return string[::-1]


input_string = input("Введіть рядок: ")
print(function_2(input_string))
