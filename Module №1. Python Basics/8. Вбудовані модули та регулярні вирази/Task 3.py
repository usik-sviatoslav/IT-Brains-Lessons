
# Завдання №3. Напишіть регулярний вираз, який перевіряє, чи відповідає рядок формату електронної пошти.
# Наприклад: “vlad@gmail.com” - валідний. “vlad!ushakov@gmail.com” - не валідний

import re

email = input("Введіть електронну адресу: ")
pattern = r"^([a-zA-Z0-9]+[._-]?)+([a-zA-Z0-9])@([a-zA-Z]+[.-]?)+[.]+([a-zA-Z]+)$"
if re.match(pattern, email):
    print("Електронна адреса валідна")
else:
    print("Електронна адреса не валідна")
