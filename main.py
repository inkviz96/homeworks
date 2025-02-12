

from quiz_game import quiz_game_start
games = {
    "guess_number": quiz_game_start
}
if __name__ == "__main__":
    start = True
    while start:
        game_name = input("Choise game: ")
        games[quiz_game_start()]()
        start = input("Choise next game?(Y/N)")
        if start == "N":
            start = False



