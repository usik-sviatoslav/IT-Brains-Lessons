"""
Завдання №2. Багатопотоковість: Паралельний пошук файлів

Потрібно створити Python скрипт, який використовує багатопотоковість для пошуку файлів з конкретним розширенням
(наприклад, .txt або .jpg) в різних директоріях на вашому комп'ютері.

Вимоги:
1. Скрипт повинен приймати розширення файлу та список директорій для пошуку як вхідні параметри.
2. Скрипт повинен використовувати багатопотоковість для одночасного пошуку в різних директоріях.
3. Знайдені файли повинні виводитися на екран з інформацією про те, в якій директорії вони були знайдені.

"""

from pathlib import Path
import time
from threading import Thread


def find_file(path, file_type, result):
    folder_path = Path(path)
    found_files = list(folder_path.glob(f'**/*.{file_type}'))

    for file in found_files:
        if file.parent not in result:
            result[file.parent] = [file.name]
        else:
            result[file.parent].append(file.name)


def task():
    dirs = [
        ("C:/Users/Public", "jpg"),
        ("C:/Apps", "exe"),
        ("C:/Drivers", "exe"),
    ]

    result = {}
    threads = [Thread(target=find_file, args=(path, file_type, result)) for path, file_type in dirs]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for root, files in result.items():
        print('\033[0;32m' + f"{root}")
        print('\033[0;37m' + f"Знайдено {len(files)} файлів:")
        print('\033[0;33m' + '\n'.join(files), '\n')


if __name__ == '__main__':
    start_time = time.time()
    task()
    print("Загальний час: ", time.time() - start_time, "сек")
