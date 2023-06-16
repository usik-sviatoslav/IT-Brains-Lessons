
# Завдання №9. Створіть функцію, яка видаляє вказаний рядок з текстового файлу.

def remove_selected_string(file_directory):
    while True:
        lines = []
        try:
            # Для візуального відображення вмісту файлу
            file = open(file_directory, "r")
            file.seek(0)
            print("\n" f"{file.read()}" "\n")
            file.close()

            # Для розділення файлу по рядках
            file = open(file_directory, "r")
            lines += file.read().strip().split("\n")

            # Для видалення рядка
            string_number = int(input("Введи номер рядка який треба видалити: "))
            lines.remove(lines[string_number - 1])
            new_file = "\n".join(lines)
            print("\n" f"{new_file}" "\n")
            file.close()

            # Перезапис файлу
            file = open(file_directory, "w")
            file.write(new_file)
            file.close()
            print(f"Видалено {string_number}-й рядок!")
            break
        except FileNotFoundError:
            print("Файлу за даною директорією не знайдено!\n")
        except ValueError:
            print("Введено не коректне значення!\n")
        except IndexError:
            print(f"Такого рядка не існує! Введи від 1-{len(lines)} ")


file_path = input("Введи директорію файлу, в котрому треба видалити вказаний рядок: ")
remove_selected_string(file_path)
