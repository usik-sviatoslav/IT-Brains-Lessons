
# Завдання №7. Створіть декоратор **`rate_limit`**, який обмежує кількість викликів декорованої функції протягом
# певного періоду часу. Декоратор повинен приймати два параметри `max_calls` та `period`.
# Перший параметр - максимальна кількість допустимих викликів функції. Другий параметр - кількість секунд у рамках
# яких ми можемо зробити `max_calls` викликів. Вам допоможе модуль `datetime` для розв'язання цієї задачі.

import time


def rate_limit(max_calls, period):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for function in range(max_calls):
                func(*args, **kwargs)
            time.sleep(period)
        return wrapper
    return decorator


@rate_limit(max_calls=1, period=10)
def my_func():
    input("Нове повідомлення: ")
    print("Відправлено!")


print("Відправлення повідомлень обмежено до 1 разу за 10 секунд.")
while True:
    my_func()
