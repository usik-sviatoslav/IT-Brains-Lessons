
# Завдання №6. Створіть клас Circle, який представляє коло. Реалізуйте методи для обчислення площі та довжини кола.
# Використовуйте атрибут класу для зберігання значення π (pi).

class Circle:
    pi = 3.14159265359

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"{self.radius}"

    def area(self):
        area = round(self.pi * self.radius ** 2, 2)
        return f'Площа круга = {area}'

    def length(self):
        length = round(2 * self.pi * self.radius, 2)
        return f'Довжина кола = {length}'


radius_circle = int(input("Введи радіус кола: "))
circle_1 = Circle(radius_circle)
print(f'{circle_1.area()}\n{circle_1.length()}')
