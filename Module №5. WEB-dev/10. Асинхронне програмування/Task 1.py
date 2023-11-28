"""
Завдання №1. Багатопроцесорність: Підрахунок кількості парних чисел у великому списку

Дано великий список цілих чисел. Ваше завдання полягає в тому, щоб розподілити цей список на дві приблизно рівні
частини й використовувати два окремі процеси для підрахунку кількості парних чисел в кожній з цих частин.

Вимоги:
1. Використовувати модуль `multiprocessing` для створення процесів.
2. Результати обох процесів повинні бути підсумовані та виведені.

"""

import random
import time
from multiprocessing import Process, Manager


def even_num_counter(nums, result, idx):
    result[idx] = sum(num for num in nums if num % 2 == 0)


def task(num_list, process_count):

    chunk_size, remainder = divmod(len(num_list), process_count)
    new_list = [num_list[i * chunk_size:(i + 1) * chunk_size] for i in range(process_count)]

    if remainder:
        new_list[-1].extend(num_list[-remainder:])

    with Manager() as manager:
        result = manager.list([None] * process_count)
        processes = [
            Process(target=even_num_counter, args=(process, result, idx)) for idx, process in enumerate(new_list)
        ]

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        print(f"Сума парних чисел з рандомного списку = {sum(result):_}".replace('_', ','))


def main():
    print("Генерація 10 мільйонів рандомних чисел у список...")
    start_time = time.time()
    num_list = [random.randrange(0, 10000000) for _ in range(10000000)]
    print("Генерація списку чисел тривала:", time.time() - start_time, "сек\n")

    start_time = time.time()
    process_count = 2
    task(num_list, process_count)
    print(f"Час підрахунку {process_count} процесами: ", time.time() - start_time, "сек")


if __name__ == '__main__':
    main()
