
# Завдання №1. Створіть клас Rectangle для представлення прямокутника.
# Додайте методи для обчислення площі та периметра прямокутника. Створіть об'єкт Rectangle і викличте ці методи.

class Rectangle:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

    @staticmethod
    def area(first_side, second_side):
        if first_side != second_side:
            print(f"Площа прямокутника = {first_side * second_side}")
        else:
            print(f"Площа квадрату = {first_side * second_side}")

    @staticmethod
    def perimeter(first_side, second_side):
        if first_side != second_side:
            print(f"Периметр прямокутника = {2 * (first_side + second_side)}")
        else:
            print(f"Периметр квадрату = {2 * (first_side + second_side)}")


while True:
    try:
        side_1 = int(input("Введи перше число: "))
        side_2 = int(input("Введи друге число: "))

        sides = Rectangle(side_1, side_2)
        sides.area(sides.first_side, sides.second_side)
        sides.perimeter(sides.first_side, sides.second_side)
    except ValueError:
        print("Введено не число!")
    finally:
        print()
