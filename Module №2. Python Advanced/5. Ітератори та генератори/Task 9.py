
# Завдання №9. Створіть ітератор, який перебирає всі паліндроми (слова, які читаються однаково зліва направо
# та справа наліво) з заданого списку слів.
<<<<<<< HEAD
=======

words = [
    "комок", "море", "довод", "вова", "ліс", "топот", "потоп", "мадам", "колесо", "тут",
    "соня", "радар", "вітер", "садок", "шабаш", "мир", "казак", "дім", "ротор", "книга"
]


class Iterator:
    def __init__(self, elements):
        self.elements = elements
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.elements):
                raise StopIteration
            word = self.elements[self.index]
            palindrome = word[::-1]
            if word == palindrome:
                self.index += 1
                return word
            else:
                self.index += 1


new_list = Iterator(words)
for i in new_list:
    print(i)
>>>>>>> 1ce66cc (Modified)
