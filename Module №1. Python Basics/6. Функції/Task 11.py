
# Завдання №11. Напишіть функцію, яка приймає на вхід два словники. Значення у словника обовʼязково число.
# Повернути новий словник, де будуть всі ключі з першого та другого словника, а у випадку якщо ключ
# є і там і там, потрібно додати значення за цим ключем з першого та другого словника до результату.

dict_1 = {"a": 40, "b": 32, "c": 24}
dict_2 = {"d": 51, "c": 12, "a": 18}


def function_11(first_dict, second_dict):
    """ Функція створює новий словник з двох інших, а значення для однакових ключів, обчислює та виводить суму """
    new_dict = {}
    new_dict.update(first_dict)

    for keys in second_dict.keys():
        if keys not in new_dict:
            new_dict[keys] = second_dict[keys]
        else:
            new_dict[keys] += second_dict[keys]

    return f"Новий словник: {new_dict}"


print(f"Перший словник: {dict_1}")
print(f"Другий словник: {dict_2}")
print(function_11(dict_1, dict_2))
