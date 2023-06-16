
# Завдання №8. Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст, виводячи рядки,
# які є у першому файлі, але відсутні у другому.

while True:
    try:
        print("Введіть директорію файлів, вміст котрих треба порівняти")
        path_1 = input("Директорія першого файлу: ")
        file_1 = open(path_1, "r")

        path_2 = input("Директорія другого файлу: ")
        file_2 = open(path_2, "r")

        new_lines = []
        new_lines += file_1.read().strip().split("\n")

        for lines_2 in file_2.read().strip().split("\n"):
            if lines_2 not in new_lines:
                new_lines.append(lines_2)
            else:
                new_lines.remove(lines_2)

        result = "\n".join(new_lines)
        print()
        print(result, "\n")

        file_1.close()
        file_2.close()
    except FileNotFoundError:
        print("Файлу за даною директорією не знайдено!\n")
    except KeyboardInterrupt:
        exit_from = input("Ти хочеш вийти з програми?\n0 = Вихід\n1 = Продовжити\n: ")
        if exit_from == "0":
            break
        else:
            continue
