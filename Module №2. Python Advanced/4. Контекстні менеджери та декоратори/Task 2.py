
# Завдання №2. Створіть контекстний менеджер DividerContext, який буде прінтити символ, який ми до нього передамо
# як розділитель для основного блоку коду до та після його виконання. Реалізувати контекстний менеджер потрібно
# 2 способами, за допомогою декоратора contextmanager та за допомогою класу. (приклад можна знайти у презентації)

from contextlib import contextmanager


@contextmanager
def divider_context(symbol):
    print(f'\n{51 * symbol}')
    yield
    print(51 * symbol)


with divider_context("-"):
    print('-----> Divided content with "contextmanager" <-----')


# ------------------------------------------------------------------------------------------------------------------


class DividerContext:
    def __init__(self, symbol):
        self.symbol = symbol

    def __enter__(self):
        print(f'\n{51 * self.symbol}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(51 * self.symbol)


with DividerContext("-"):
    print('----------> Divided content with class <-----------')
