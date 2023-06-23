
# Завдання №4. Створіть метаклас, який викидає помилку при спробі створити клас з атрибутами, що
# починаються з '__' (два нижніх підкреслення)


class NoDunderAttributes(type):
    def __init__(cls, name, bases, attrs):
        import re
        for key in attrs:
            if re.compile(r"^_\w+__\w+$").search(key):
                raise TypeError('It is impossible to have attribute names beginning with "__"')

        attrs["secret_attribute"] = "secret_attribute"
        super().__init__(name, bases, attrs)


class MyPrivateClass(metaclass=NoDunderAttributes):
    __secret_attribute = 15
