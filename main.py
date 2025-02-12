from r_p_s import rock_paper_scissors_start
from hangman import hang_start
from cvest import cvest_start
from quizz import quizz_start
from guess_number import guess_num_start

games = {
    'rock-paper-scissors': rock_paper_scissors_start,
    'hangman': hang_start,
    'cvest': cvest_start,
    'guess_number': guess_num_start,
    'quizz': quizz_start
}

if __name__ == "__main__":
    print("Добро пожаловать в игровую платформу!")
    print("Доступные игры:")
    for game in games:
        print(f"- {game}")

    while True:
        game_name = input('\nВведите название игры (или "exit" для выхода): ').strip()

        if game_name.lower() == "exit":
            print("До свидания! Спасибо за игру.")
            break

        if game_name in games:
            print(f"Запуск игры: {game_name}")
            games[game_name]()
        else:
            print("Ошибка: такой игры нет. Пожалуйста, выберите из списка доступных игр.")



