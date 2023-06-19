"""
Завдання №8. Ви розробляєте програму для автосалону, яка обробляє інформацію про різні автомобілі. У вас є
базовий абстрактний клас Car (автомобіль), який містить загальну інформацію про автомобіль, таку як марка та модель.
У додаткових класах, які успадковують від Car, ви розширюєте функціональність для конкретних типів автомобілів.

1. Клас Sedan (седан) успадковує від Car. Він має додатковий атрибут - кількість дверей.
2. Клас SUV успадковує від Car. Він має додатковий атрибут - кількість пасажирських місць.
3. Клас SportsCar (спортивний автомобіль) успадковує від Car. Він має додатковий атрибут - максимальна швидкість.

Створіть об'єкти різних класів (седан, позашляховик, спортивний автомобіль) і використовуйте їх функціонал.
Виведіть інформацію про кожен автомобіль, включаючи загальну інформацію з Car та специфічну інформацію для
кожного класу."""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return f"Бренд: {self.brand}"

    def get_model(self):
        return f"Модель: {self.model}"

    def display_info(self):
        return f"{Car.get_brand(self)}\n{Car.get_model(self)}"


class Sedan(Car):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def doors_count(self):
        return f"Кількість дверей: {self.doors}"

    def display_info(self):
        return f"{Car.display_info(self)}\n{Sedan.doors_count(self)}"


class SUV(Car):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def seats_number(self):
        return f"Кількість місць: {self.seats}"

    def display_info(self):
        return f"{Car.display_info(self)}\n{SUV.seats_number(self)}"


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def max_speed(self):
        return f"Максимальна швидкість: {self.speed} км/год"

    def display_info(self):
        return f"{Car.display_info(self)}\n{SportsCar.max_speed(self)}"


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

print(33 * "-")
print(sedan.display_info())
print(33 * "-")
print(suv.display_info())
print(33 * "-")
print(sports_car.display_info())
print(33 * "-")
