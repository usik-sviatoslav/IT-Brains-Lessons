
# Завдання №2. Створіть метаклас, який записує в консоль повідомлення, коли створюється новий клас.


class LogginMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f'Class "{name}" has been created')
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=LogginMeta):
    pass


a = MyClass()
