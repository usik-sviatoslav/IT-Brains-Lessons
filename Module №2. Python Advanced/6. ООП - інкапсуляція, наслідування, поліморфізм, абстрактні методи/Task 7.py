"""
Завдання №7. Розробіть клас "Square", який успадковує властивості й методи з класу "Rectangle". Додайте
властивість side_length (довжина сторони) і перевизначите методи, які використовують властивості width і height
класу "Rectangle", щоб вони використовували властивість side_length класу "Square". Виведіть значення ширини,
висоти й довжини сторони для об'єкта класу "Square"."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return f"Ширина: {self.width}"

    def get_height(self):
        return f"Висота: {self.height}"


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def get_side_length(self):
        return f"Довжина: {self.side_length}"

    def get_width(self):
        return f"Ширина: {self.width}"

    def get_height(self):
        return f"Висота: {self.height}"


rectangle = Square(5)
print(rectangle.get_width())
print(rectangle.get_height())
print(rectangle.get_side_length())
