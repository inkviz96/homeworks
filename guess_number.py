# import random
#
# def guess_number_start():
#     print("Добро пожаловать в игру 'Угадай число'!")
#
#     while True:
#         print("Выберите уровень сложности:")
#         print("1. Легкий (5 попыток)")
#         print("2. Средний (7 попыток)")
#         print("3. Сложный (10 попыток)")
#
#         difficulty = input("Введите номер уровня сложности (1/2/3): ").strip()
#
#         if difficulty == '1':
#             lower_bound, upper_bound, max_attempts = 1, 10, 5
#         elif difficulty == '2':
#             lower_bound, upper_bound, max_attempts = 1, 50, 7
#         elif difficulty == '3':
#             lower_bound, upper_bound, max_attempts = 1, 100, 10
#         else:
#             print("Некорректный выбор. Попробуйте снова.")
#             continue
#
#         secret_number = random.randint(lower_bound, upper_bound)
#         print(f"Я загадал число от {lower_bound} до {upper_bound}. У вас есть {max_attempts} попыток, чтобы угадать его!")
#
#         attempts = 0
#
#         while attempts < max_attempts:
#             try:
#                 guess = int(input("Введите ваше предположение: "))
#                 attempts += 1
#
#                 if guess < secret_number:
#                     print("Загаданное число больше.")
#                 elif guess > secret_number:
#                     print("Загаданное число меньше.")
#                 else:
#                     print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток.")
#                     break
#             except ValueError:
#                 print("Пожалуйста, введите корректное число.")
#
#             if attempts == max_attempts:
#                 print(f"К сожалению, вы не угадали число {secret_number}. Попробуйте снова!")
#
#         play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
#         if play_again != 'да':
#             print("Спасибо за игру! До встречи!")
#             break
#
# if __name__ == "__main__":
#     guess_number_start()

























