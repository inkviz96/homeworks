
# Викторина

import random


def choose_word():
    words = ["питон", "компьютер", "игра", "программа"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def game_start():
    print("Добро пожаловать в игру 'Угадай слово'!")
    word = choose_word()
    guessed_letters = set()
    attempts = 7

    while attempts > 0:
        current_word = display_word(word, guessed_letters)
        print("\nСлово: ", current_word)
        print(f"Осталось попыток: {attempts}")

        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже называли эту букву.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print(f"Отлично! Буква '{guess}' есть в слове.")


        else:
            print(f"Увы! Буквы '{guess}' нет в слове.")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nПоздравляем! Вы угадали слово:", word)
            break
    else:
        print("Вы проиграли! Загаданное слово было:", word)

game_start()
