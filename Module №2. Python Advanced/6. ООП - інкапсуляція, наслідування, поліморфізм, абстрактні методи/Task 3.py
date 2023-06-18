"""
Завдання №3. Розробіть клас "Car", який містить такі властивості: make (марка автомобіля),
model (модель автомобіля), year (рік випуску автомобіля) і mileage (пробіг автомобіля). Забезпечте
можливість доступу до цих властивостей через методи, а також зробіть властивості "make" і "model" приватними.

Додайте метод "drive" до класу "Car", який збільшує пробіг автомобіля на задане значення. Перевірте, чи не
перевищує пробіг заданий ліміт (наприклад, 300 000 км), і виведіть повідомлення про досягнення ліміту при
спробі здійснити поїздку."""


class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return f"{self.year} року"

    def get_mileage(self):
        return f"пробіг {self.mileage:_} км".replace("_", " ")

    def drive(self, new_distance):
        limit = 300000
        if self.mileage >= limit:
            return "Досягнення ліміту 300 000 км"
        self.mileage += new_distance
        return self.get_mileage()


car = Car("Toyota", "Camry", 2020, 50000)
print(car.get_make(), car.get_model(), car.get_year())
print(car.get_mileage())

car.drive(100)
print(f"Новий {car.get_mileage()}")
