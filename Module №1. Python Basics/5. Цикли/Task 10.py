
# Завдання №10. Напишіть програму, яка отримує на вхід рядок і видаляє з нього усі розділові знаки.

import re
while True:
    input_string = input("Введіть речення з розділовими знаками: ")
    delimiters = "[,.;!?]"
    string_split = re.split(delimiters, input_string)
    string = "".join(string_split)
    print(string, "\n")
