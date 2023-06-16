
# Завдання №5. Створіть декоратор retry який приймає першим аргументом число - кількість разів, яку потрібно буде
# повторити виконання функції у разі викидання нею помилки. (приклад можна знайти у презентації)


def retry(num=1):
    def decorator(func):
        def inner(*args, **kwargs):
            for i in range(num):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"{e}")
        return inner
    return decorator


@retry(3)
def function():
    number_input = int(input("Введи число: "))
    print(f"Ваше число {number_input}")
    return number_input


function()
