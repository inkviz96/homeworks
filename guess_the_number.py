 #Угадай число

import random


def guess_number_start():
    print("Угадай число от 1 до 100")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            user_guess = int(input("Введите число: "))
            if user_guess < 1 or user_guess > 100:
                print("Введите число в диапазоне от 1 до 100.")
                continue
            attempts += 1
            if user_guess < secret_number:
                print("Загаданное число больше. Попробуйте еще раз.")
            elif user_guess >  secret_number:
                print("Загаданное число меньше. Попробуйте еще раз.")
            else:
                print(f"Супер! Вы угадали число{secret_number} за {attempts} попыток.")
                break

        except ValueError:
            print("Пожалуйста, введите корректное число.")


guess_number_start()