
# Завдання №16. Напишіть функцію, яка отримує кілька слів як аргументи та повертає словник, що містить
# кількість кожної голосної літери у ВСІХ словах. Використовуйте метод count для підрахунку входжень
# кожної голосної. Наприклад результат роботи функциії {”a”: 13, “e”: 4, “o”: 23, “i”: 2}

vowels = {
    "UA": ["А", "а", "Е", "е", "Є", "є", "И", "и", "І", "і", "Ї", "ї", "О", "о", "У", "у", "Ю", "ю", "Я", "я"],
    "EN": ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
}


def function_16(*args):
    """ Функція підраховує кількість голосних букв у словах """
    unique_letters = {}
    for words in args:
        for letter in words:
            if letter in vowels["UA"] or letter in vowels["EN"]:
                unique_letters[letter] = unique_letters.get(letter, 0) + 1

    return unique_letters


input_string = input("Введіть слова через пробіл: ").lower().split()
print(function_16(*input_string))
