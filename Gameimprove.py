from random import randint


def guess_num_start():
    print('Привет добро пожаловать в игру "Угадай число"! \n Выбери уровень сложности: \n 1 - Легко (0, 10) \n 2 - Средний (-10, 10) \n 3 - Хардкор (-15, 15)')
    b = [1, 2, 3]
    users_answer = input("Ваш выбор: ")
    if not users_answer.isdigit() or int(users_answer) not in b:
        print('Неккроектный ввод!!')
        print('Попробуйте еще раз!')
        return
    users_answer = int(users_answer)
    turns = 5

    if users_answer == 1:
        comp_choice = randint(0, 10)
        print("Вы выбрали уровень Легко!")
    elif users_answer == 2:
        comp_choice = randint(-10, 10)
        print("Вы выбрали уровень Средний!")
    elif users_answer == 3:
        comp_choice = randint(-15, 15)
        print("Вы выбрали уровень Хардкор!")

    while turns != 0:
        user_choice = input('Ваше предположение? ')
        if not user_choice.lstrip("-").isdigit():
            print("Пожалуйста, введите корректное целое число.")
            continue
        user_choice = int(user_choice)

        if user_choice == comp_choice:
            print(f'Поздравляю вы угадали {comp_choice} за {5 - turns + 1} попыток!')
            break
        else:
            turns -= 1
            if turns > 0:
                print("Упс! Попробуйте еще раз")
                print(f'У вас осталось {turns} попыток!')
            else:
                print('Вы проиграли!')
                print(f"Загаданное число было {comp_choice}")


if __name__ == "__main__":
    guess_num_start()