
# Завдання №8. Напишіть генератор, який видає послідовність простих чисел.

def prime_generator():
    yield 2
    primes = []
    number = 3

    while True:
        is_prime = True
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break

        if is_prime:
            yield number

        number += 2


my_range = int(input("Введи кількість простих чисел: "))
generator = prime_generator()
for num in range(my_range):
    print(next(generator))
