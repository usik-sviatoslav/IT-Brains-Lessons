"""
Завдання №2. Розширте клас "Person" з попереднього завдання, додавши методи для зміни значень імені та віку.
Зробіть так, щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120. При спробі
встановити недійсне значення, виведіть повідомлення про помилку."""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __get_name(self):
        return f"Your name {self.__name}."

    def __get_age(self):
        return f"{self.__age} years."


class Update(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def is_name(self):
        if self._Person__name is None:
            return "Обов'язкове поле!"

        for letter in self._Person__name:
            if not letter.isalpha():
                return "У імені не може бути цифр!"
        return self._Person__get_name()

    def is_age(self):
        if self._Person__age is None:
            return "Вік не встановлений!"

        if isinstance(self._Person__age, int):
            if self._Person__age < 0:
                return "Вік не може бути менше 0!"
            elif self._Person__age > 120:
                return "Вік обмежений до 120 років!"
        else:
            return "Введено не коректно дані!"

        return self._Person__get_age()


update_user_1 = Update("Sviatoslav23", 121)
print(update_user_1.is_name())
print(update_user_1.is_age())
