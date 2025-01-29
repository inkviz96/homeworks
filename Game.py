import random

def guess_number_start():
    print("Добро пожаловать в игру 'Угадай число'!")
    lower_bound = int(input("Введите нижнюю границу диапазона: "))
    upper_bound = int(input("Введите верхнюю границу диапазона: "))

    if lower_bound >= upper_bound:
        print("Нижняя граница должна быть меньше верхней.")
        return

    secret_number = random.randint(lower_bound, upper_bound)
    print(f"Я загадал число от {lower_bound} до {upper_bound}. Попробуйте угадать его!")

    attempts = 0
while True:
        try:
            guess = int(input("Введите ваше предположение: "))
    attempts += 1

         if guess < secret_number:
                print("Загаданное число больше.")
            elif guess > secret_number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")


if __name__ == "__main__":
    guess_number_start()