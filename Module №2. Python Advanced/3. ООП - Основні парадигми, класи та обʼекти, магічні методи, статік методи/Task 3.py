
# Завдання №3. Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути, такі як назва,
# швидкість і вартість. Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
# Створіть список транспортних засобів і відсортуйте його за швидкістю.

class Vehicle:
    def __init__(self, brand, speed, price):
        self.brand = brand
        self.speed = speed
        self.price = price

    def __gt__(self, other):
        if self.speed > other.speed:
            return f"{self.brand} швидше за {other.brand} на {self.speed - other.speed} км/год"
        elif self.speed < other.speed:
            return f"{other.brand} швидше за {self.brand} на {other.speed - self.speed} км/год"
        else:
            return f"Автомобіль {self.brand} та {other.brand} можуть розвити однакову швидкість"

    def __repr__(self):
        return f"{self.brand}. Швидкість: {self.speed} км/год; Ціна: ${self.price:_}".replace("_", ".")

    @staticmethod
    def sorted(*cars):
        cars_list = list(cars)
        cars_list.sort(key=lambda car: car.speed, reverse=True)
        result = "\n".join([repr(car) for car in cars_list])

        return result


car_1 = Vehicle("Mercedes", 270, 59000)
car_2 = Vehicle("BMW", 250, 68000)
car_3 = Vehicle("Audi", 260, 72000)
car_4 = Vehicle("Lexus", 240, 62000)
car_5 = Vehicle("Toyota", 220, 48000)
car_6 = Vehicle("Ford", 200, 40000)
car_7 = Vehicle("Chevrolet", 180, 36000)
car_8 = Vehicle("Honda", 190, 42000)
car_9 = Vehicle("Volkswagen", 210, 52000)
car_10 = Vehicle("Hyundai", 180, 32000)

print(car_1 > car_2)
print(Vehicle.sorted(car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8, car_9, car_10))
