
# Завдання №1. Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду. Контекстний менеджер
# повинен виводити час, що минув, при виході з контексту. Використовуйте контекстний менеджер для вимірювання часу
# виконання певного фрагмента коду. Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора
# contextmanager та за допомогою класу.

from contextlib import contextmanager
from time import time, sleep


@contextmanager
def timer(filename, mode):
    start = time()
    sleep(0.1)
    f = open(filename, mode)
    end = time()
    print(f'Час виконання функції за допомогою декоратора "contextmanager": {end - start} сек.')
    yield f
    f.close()


with timer("file.txt", "a") as file:
    file.write("\nSome text")


# ------------------------------------------------------------------------------------------------------------------


class Timer:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        start = time()
        sleep(0.1)
        self.file = open(self.filename, self.mode)
        end = time()
        print(f'Час виконання функції за допомогою класу: {end - start} сек.')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Timer("file.txt", "a") as file:
    file.write("\nSome text")
