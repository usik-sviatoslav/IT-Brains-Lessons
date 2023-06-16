
def game():
    from random import choice
    from re import match

    list_of_fruits = [
        "Яблуко", "Банан", "Апельсин", "Груша", "Ківі", "Мандарин", "Лимон", "Ананас", "Манго", "Абрикос", "Персик",
        "Вишня", "Виноград", "Черешня", "Айва", "Полуниця", "Малина", "Чорна смородина", "Арбуз", "Грейпфрут"
    ]
    chosen_word = choice(list_of_fruits).lower()
    masked_word = "*" * len(chosen_word)
    guessed_letters = []

    print('Гра - "Поле Чудес"')

    try:
        attempts = int(input("Введи кількість спроб: "))
    except ValueError:
        attempts = 10

    print(f"У тебе {attempts} спроб вгадати слово. Погнали!")
    print(f"Ти можеш вгадати одразу слово {masked_word} або вводь по буквах: ")

    while attempts > 0:
        guess = input("")

        if len(guess) == 1:
            if guess in chosen_word:
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
                    masked_word = "".join([guess if guess in guessed_letters else "*" for guess in chosen_word])
                    print(masked_word)
                    if "*" not in masked_word:
                        print("Вітаю! Ти вгадав слово!\n")
                        return
                else:
                    print("Ти вже вводив цю літеру")
            elif match(r"[A-Za-z]", guess):
                print("Зміни мову!")
            else:
                print("Такої літери немає")
                attempts -= 1
        elif len(guess) == 2:
            if match(r"[A-Za-z]", guess):
                print("Зміни мову, та вводь по одній літері!")
            else:
                print("Вводь по одній літері!")
        else:
            if guess == chosen_word:
                print("Вітаю! Ти вгадав слово!\n")
                return
            if match(r"[A-Za-z]", guess):
                print("Слово введено не правильно! Зміни мову")
            else:
                print("Слово не правильне!")
                attempts -= 1

    print(f'Кількість спроб закінчилась, ти не відгадав слово "{chosen_word}"', "\n")


while True:
    start_game = input('Щоб почати натисніть "Enter", щоб вийти введи щось\n')
    if start_game == "":
        game()
    else:
        break
