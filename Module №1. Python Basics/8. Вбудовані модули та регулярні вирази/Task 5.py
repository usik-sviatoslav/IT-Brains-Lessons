
# Завдання №5. Напишіть регулярний вираз, який перевіряє, чи відповідає рядок формату IP-адреси
# Наприклад: "192.168.0.1" - валідний “192.168.270.1” - не валідний

def is_valid_ip(ip_address):
    """ Функція перевіряє валідність IP адреси """
    import re
    pattern = r"^(\d{1,3}.){3}\d{1,3}$"
    if not re.match(pattern, ip):
        return "Не валідний IP адрес"

    ip_parts = ip_address.split(".")
    for part in ip_parts:
        if int(part) > 255 or int(part) < 0:
            return "Не валідний IP адрес"

    return "Валідний IP адрес"


ip = input("Введіть IP адресу: ")
print(is_valid_ip(ip))
