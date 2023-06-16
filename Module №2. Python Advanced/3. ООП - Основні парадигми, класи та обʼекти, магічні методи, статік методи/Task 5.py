
# Завдання №5. Розробіть клас Library для представлення бібліотеки. А також клас Book для представлення книги. Клас
# Library повинен мати атрибут books зі списком книжок. Кожна книга в бібліотеці має атрибути, такі як назва, автор і
# рік видання. Додайте метод add_book, який додає нову книгу до бібліотеки. Реалізуйте метод __str__, який виводить
# список книг у бібліотеці. Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.

class Library:
    books = []

    def __int__(self, book):
        self.book = book

    @classmethod
    def add_book(cls, *new_books):
        for book in new_books:
            if book not in cls.books:
                cls.books.append(book)

    @classmethod
    def __str__(cls):
        book_list = "\n".join([book.__repr__() for book in cls.books])
        return f"Книги у бібліотеці:\n{book_list}"


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __repr__(self):
        return f'"{self.name}", {self.author}. {self.year} year.'


book1 = Book("The Enigma of Time", "Jennifer Collins", 2022)
book2 = Book("The Shadows Within", "Michael Anderson", 2023)
book3 = Book("Echoes of Destiny", "Emily Thompson", 2021)

Library.add_book(book1, book2, book3)
print(Library.__str__())
