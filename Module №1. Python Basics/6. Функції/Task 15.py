
# Завдання №15. Напишіть функцію, яка отримує речення у вигляді рядка і повертає нове речення, в якому
# перша буква кожного слова пишеться з великої літери. Використовуйте метод split, щоб розбити речення
# на слова, і метод capitalize, щоб зробити першу літеру великою.

def function_15(string):
    """ Функція повертає речення збільшуючи першу букву у кожному слові """
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    new_string = " ".join(capitalized_words)
    return new_string


input_string = input("Введіть речення: ")
print(function_15(input_string))
