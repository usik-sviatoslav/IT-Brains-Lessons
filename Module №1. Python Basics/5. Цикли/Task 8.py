
# Завдання №8. Напишіть програму, яка отримує на вхід рядок і виводить слова у зворотному порядку.

while True:
    input_string = input("Введіть речення: ")
    reversed_words = reversed(input_string.split())
    new_string = " ".join(reversed_words)
    print(new_string, "\n")
