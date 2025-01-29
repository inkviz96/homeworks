from quiz import game_start
from guess_the_number import guess_number_start

games = {
    "quiz": game_start, "guess_the_number": guess_number_start
}
if __name__ == "__main__":
    start = True
    while start:
        try:
            game_name = input("Choise game: ")
            games[game_name]()
            start = input("Choise next game?(Y/N)")
            if start == "N":
                start = False

        except KeyError:
            print("Неверное название игры. Пожалуйста, попробуйте еще раз.")