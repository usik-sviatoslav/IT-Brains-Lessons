"""
Завдання №4. Створіть базовий клас "Shape" (фігура), який має властивість color (колір) і метод
display_color() для виведення кольору фігури. Створіть похідний клас "Rectangle" (прямокутник), який наслідує
властивість color і додає властивості width (ширина) і height (висота). Забезпечте можливість встановлення
значень ширини й висоти прямокутника та виведення їх значень."""


class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        return f"Color: {self.color}"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_width(self):
        return f"Width: {self.width}"

    def get_height(self):
        return f"Height: {self.height}"


rectangle = Rectangle("Blue", 10, 5)
print(rectangle.display_color())
print(rectangle.get_width())
print(rectangle.get_height())
