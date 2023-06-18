"""
Завдання №6. Ви розробляєте програму для інформації про тварин в зоопарку. У вас є базовий клас Animal (тварина),
який містить загальну інформацію про тварину, таку як назва та вид. У додаткових класах, які успадковують
від Animal, ви розширюєте функціональність для конкретних видів тварин.

1. Клас Mammal (ссавець) успадковує від Animal. Він має додатковий атрибут - тип харчування
(наприклад, травоїдний, всеїдний, хижий).
2. Клас Carnivore (хижак) успадковує від Mammal. Він має додатковий атрибут - кількість зубів.
3. Клас Lion (лев) успадковує від Carnivore. Він має додатковий атрибут - розмір гриви.

Створіть об'єкти різних класів (лев, хижак, ссавець) і використовуйте їх функціонал. Виведіть інформацію про
кожну тварину, включаючи загальну інформацію з Animal та специфічну інформацію для кожного класу."""


class Animal:
    def __init__(self, animal, species):
        self.animal = animal
        self.species = species

    def animal(self):
        return f"Звір: {self.animal}"

    def species(self):
        return f"Вид: {self.species}"


class Mammal(Animal):
    def __init__(self, animal, species, nutrition_type):
        super().__init__(animal, species)
        self.nutrition_type = nutrition_type

    def nutrition_type(self):
        return f"Тип харчування: {self.nutrition_type}"

    def display_info(self):
        return f"{Animal.animal(self)}\n{Animal.species(self)}\n{Mammal.nutrition_type(self)}"


class Carnivore(Mammal):
    def __init__(self, animal, species, nutrition_type, teeth_count):
        super().__init__(animal, species, nutrition_type)
        self.teeth_count = teeth_count

    def teeth_count(self):
        return f"Кількість зубів: {self.teeth_count}"

    def display_info(self):
        return f"{Mammal.display_info(self)}\n{Carnivore.teeth_count(self)}"


class Lion(Carnivore):
    def __init__(self, animal, species, nutrition_type, teeth_count, mane_size):
        super().__init__(animal, species, nutrition_type, teeth_count)
        self.mane_size = mane_size

    def mane_size(self):
        return f"Розмір гриви: {self.mane_size}"

    def display_info(self):
        return f"{Carnivore.display_info(self)}\n{Lion.mane_size(self)}"


lion = Lion("Сімба", "Лев", "Хижак", 30, "Велика")
carnivore = Carnivore("Тигр", "Хижак", "Хижак", 40)
mammal = Mammal("Слон", "Ссавець", "Травоїдний")

print(lion.display_info())
print("---------------------------")
print(carnivore.display_info())
print("---------------------------")
print(mammal.display_info())
