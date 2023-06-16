
# Завдання №3. Напишіть програму, яка відкриває файл для читання та обробляє помилку FileNotFoundError,
# якщо файл не знайдено.

file_name = "file.txt"
try:
    file = open(file_name)
    print(file.readline())
    file.close()
except FileNotFoundError:
    print("Не зміг знайти файл у даній директорії")
