
# Завдання №6. Напишіть генератор, який фільтрує непарні числа з заданої послідовності.

def generator(n):
    for i in range(1, n + 1, 2):
        yield i


number = generator(int(input("Послідовність непарних чисел від 1 до ")))
for num in number:
    print(num)

