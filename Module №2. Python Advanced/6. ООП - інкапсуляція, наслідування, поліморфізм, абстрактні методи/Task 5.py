"""
Завдання №5. Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод display_color().
В методі display_color() виведіть повідомлення про колір прямокутника і додайте також виведення повідомлення
про його розміри (ширину і висоту)."""


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

    def display_color(self):
        return f"{Shape.display_color(self)}\n{self.get_width()}\n{self.get_height()}"


rectangle = Rectangle("Blue", 10, 5)
print(rectangle.display_color())
