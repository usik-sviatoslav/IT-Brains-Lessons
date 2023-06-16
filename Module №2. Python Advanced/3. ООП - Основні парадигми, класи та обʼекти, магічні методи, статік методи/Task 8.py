
# Завдання №8. Створіть клас Book який має такі атрибути як рік видання, назву, автор та кількість сторінок.
# Створіть статік метод який буде приймати список книжок та рік, та повертати кількість книжок з цього списку які
# були опубліковані у цьому році.

class Book:
    def __init__(self, year, name, author, pages):
        self.year = year
        self.name = name
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f'{self.author}. "{self.name}", {self.pages} pages. {self.year} year.'

    @staticmethod
    def books(books_list, year):
        found_books = []
        for book in books_list:
            if book.year == year:
                found_books.append(book)

        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"Книги {year} року видання немає у списку.")


book1 = Book(2022, "The Enigma of Time", "Jennifer Collins", 350)
book2 = Book(2023, "The Shadows Within", "Michael Anderson", 420)
book3 = Book(2021, "Echoes of Destiny", "Emily Thompson", 280)
book4 = Book(2023, "The Lost Expedition", "Jonathan Roberts", 400)
book5 = Book(2022, "Whispers in the Dark", "Sophia Adams", 320)
book6 = Book(2021, "The Forgotten Land", "David Wilson", 280)
book7 = Book(2022, "The Crimson Rose", "Victoria Roberts", 400)
book8 = Book(2023, "Echoes of Silence", "Alexander Thompson", 320)

year_input = int(input("Введи рік видання: "))
Book.books([book1, book2, book3, book4, book5, book6, book7, book8], year_input)
