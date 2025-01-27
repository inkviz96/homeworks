import random

def hang_start():
    words = ['барс', 'АндП', 'АндБ']
    
    ran_choice = random.choice(words)
    print(ran_choice)
    guessed_word = ["_"] * len(ran_choice)
    print("Секретное слово:", "_" * len(ran_choice))
    turns = 5
    while turns != 0:
        print("\nТекущее слово:", " ".join(guessed_word))
        a = input('Угадайте букву: ')

        if a in ran_choice:
            print('Угадали!')

            for index, char in enumerate(ran_choice):
                if char == a:
                    guessed_word[index] = a

        else:
            print("Не угадали!")
            turns -= 1    

        if "_" not in guessed_word:
            print("\nПоздравляем, вы отгадали слово:", ran_choice)
            break
    else:
        print("\nВы проиграли! Загаданное слово было:", ran_choice)
hang_start()

# Hello
#  1

# _ _ _ _ _
# e
# _ e _ _ _

# x
# Wrong 4 tries

# l 2 3

# ran_choice "hello"
# word = ["".join("_") for _ in len(ran_choise)]
# word[1] = "e" # _e___