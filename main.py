from rock_paper_scissors import rock_paper_scissors_start

games = {
    "rock_paper_scissors": rock_paper_scissors_start
}
if __name__ == "__main__":
    start = True
    while start:
        game_name = input("Choise game: ")
        games[game_name]()
        start = input("Choise next game?(Y/N)")
        if start == "N":
            start = False