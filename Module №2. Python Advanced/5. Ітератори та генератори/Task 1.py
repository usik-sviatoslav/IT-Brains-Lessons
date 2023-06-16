
# Завдання №1. Змініть функцію even_odd_generator так, щоб вона генерувала послідовність чисел від 1 до n з
# рядками "Fizz" для чисел, які діляться на 3, "Buzz" для чисел, які діляться на 5, і "FizzBuzz" для чисел,
# які діляться як на 3, так і на 5.

def even_odd_generator(n):
    for num in range(1, n):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            yield num


func = even_odd_generator(100)
for i in func:
    print(i)
