
# Завдання №5. Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.

file_name = "file.txt"

file = open(file_name)
words_in_file = len(file.read().split())
file.close()

print(words_in_file)
