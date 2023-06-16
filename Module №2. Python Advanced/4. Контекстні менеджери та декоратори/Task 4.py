
# Завдання №4. Реалізувати декоратор timeit, який вимірює час виконання декорованої функції й виводить його.
# Для отримання часу роботи скористуйтесь модулем time і функцією time.time()

from time import perf_counter as time


def timeit(func):

    def decorator(*args):
        start = time()
        func(*args)
        end = time()
        print(f'Час виконання: {end - start}')

    return decorator


@timeit
def multiply_numbers(a, b):
    print(f'a x b = {a * b}')


multiply_numbers(50, 26)
