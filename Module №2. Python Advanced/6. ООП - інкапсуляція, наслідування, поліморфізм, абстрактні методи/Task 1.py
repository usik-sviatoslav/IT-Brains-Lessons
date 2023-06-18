"""
Завдання №1.Напишіть клас "Person", який має властивості name (ім'я) і age (вік). Зробіть ці властивості
приватними, щоб вони не могли бути змінені напряму ззовні класу. Забезпечте методи для доступу до цих
властивостей та встановлення їх значень."""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __get_name(self):
        return f"Your name {self.__name}."

    def __get_age(self):
        return f"{self.__age} years"


user_1 = Person("Sviatoslav", 23)
print(user_1._Person__get_name(), user_1._Person__get_age())
