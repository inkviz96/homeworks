from random import randint


def guess_num_start():
    print('Привет добро пожаловать в игру "Угадай число"!')
    print('Выбери уровень сложности:')
    print('1 - Легко (0, 10)')
    print('2 - Средний (-10, 10)')
    print('3 - Хардкор (-15, 15)')
    a = input("Ваш выбор: ")
    if not a.isdigit() or int(a) not in [1,2,3]:
        print('Неккроектный ввывод!!')
        print('Попробуйте еще раз!')
        return
    a = int(a)
    turns = 5
    
    if a == 1:
        comp_choice = randint(0, 10)
        print("Вы выбрали уровень Легко!")
    elif a == 2:
        comp_choice = randint(-10, 10)
        print("Вы выбрали уровень Средний!")
    elif a == 3:
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
            
guess_num_start()
