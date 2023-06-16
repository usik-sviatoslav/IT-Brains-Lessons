
# Завдання №6. Реалізувати декоратор кешування memoize, який кешує результати декорованої функції для покращення
# продуктивності при повторних викликах з тими самими аргументами. Тобто він повинен запамʼятовувати аргументи з
# якими функція викликалась і результат роботи функції з цими аргументами. І у випадку, якщо ми вже маємо результат
# для цих аргументів, просто повернути закешований результат, замість виклику функції.

def memoize(func):
    cache = {}

    def wrapper(a, b):
        result_str = f"{a} * {b}"
        if result_str not in cache:
            result = func(a, b)
            cache[result_str] = result
            return f"{a} * {b} = {result}"
        else:
            return f"{a} * {b} = {cache.get(result_str)}"
    return wrapper


@memoize
def multiply_func(a, b):
    print("Результат множення:")
    return a * b


while True:
    number1 = int(input("Множення першого числа: "))
    number2 = int(input("На друге: "))
    print(multiply_func(number1, number2))
