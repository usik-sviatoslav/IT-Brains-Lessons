
# Завдання №3. Створіть простий декоратор логування log_func, який буде прінтити будь-яке повідомлення перед
# викликом декорованої функції, та після.

def log_func(func):

    def decorator(name):
        print("# start loggin func")
        func(name)
        print("# end of loggin func")

    return decorator


@log_func
def say_hi(name):
    print(f'Wussup {name}')


say_hi("bro")
