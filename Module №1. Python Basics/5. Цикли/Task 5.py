
# Завдання №5. Напишіть програму, яка запитує у користувача число і виводить усі числа від 1 до цього числа.
# Однак, якщо число ділиться на 3, виведіть "Fizz" замість числа. Якщо число ділиться на 5, виведіть "Buzz"
# замість числа. Якщо число ділиться і на 3, і на 5, виведіть "FizzBuzz" замість числа.
# Розв'язання цієї задачі має бути за допомогою циклу while!

while True:
    input_value = int(input("Введіть число: "))
    i = 1
    while i <= input_value:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i += 1
