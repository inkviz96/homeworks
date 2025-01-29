from quiz import play_game
from guess_the_number import guess_number

games = {
    "quiz": play_game, "guess_the_number": guess_number
}
if __name__ == "__main__":
    start = True
    while start:
        game_name = input("Choise game: ")
        games[game_name]()
        start = input("Choise next game?(Y/N)")
        if start == "N":
            start = False