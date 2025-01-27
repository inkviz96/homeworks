from random import choice

def rock_paper_sicossors_start():
    
    start = True
    while start:
        options = ['камень', 'ножницы', 'бумага']
        comp = choice(options)
        user_choice = input('Камень или Бумага или Ножницы: ').lower()
        print(f'Комп выбрал {comp}')
        if comp == user_choice:
            print('Ничья')
        elif (user_choice == "камень" and comp == "ножницы") or \
            (user_choice == "ножницы" and comp == "бумага") or \
            (user_choice == "бумага" and comp == "камень"):
            print("Вы победили!")
        else:
            print('Вы проиграли!')
        gp = input('Are you want continue? Y/N: ')
        if gp == 'N':
            start = False
        
rock_paper_sicossors_start()
