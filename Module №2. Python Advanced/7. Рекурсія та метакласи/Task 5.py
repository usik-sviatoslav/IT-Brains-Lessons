
# Завдання №5. Створіть метаклас, який переконується, що назва класу задана у форматі CamelCase. Перевірки
# на те що перший символ з великої літери - вистачить.

class CamelCase(type):
    def __new__(cls, name, bases, attrs):
        import re
        if not re.findall(r"^[A-Z]", name):
            raise TypeError("Class name not in CamelCase")
        return super().__new__(cls, name, bases, attrs)


class notCamelCase(metaclass=CamelCase):
    pass
