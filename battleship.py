"""
battleship.py
"""
from random import randint
def main():
    """
    main function`
    """
    board = []
    for num in range(5):
        board.append(["O"] * 5)
    def print_board(board_a):
        """
        prints the battleship board
        """
        for row in board_a:
            print " ".join(row)
    print "Let's play Battleship!"
    print_board(board)
    def random_row(board_a):
        """
        returns random number for row
        """
        return randint(0, len(board_a) - 1)
    def random_col(board_a):
        """
        return random number for col
        """
        return randint(0, len(board_a[0]) - 1)
    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row
    print ship_col

    for turn in range(4):
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        while (guess_row > 4 or guess_row < 0) or (guess_col > 4 or guess_col < 0):
            print "Those are invalid coordinates. Guess again."
            guess_row = int(input("Guess Row:"))
            guess_col = int(input("Guess Col:"))
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if board[guess_row][guess_col] == "X":
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                print "Turn", turn + 1
        if turn == 3:
            print "Game Over"
            print_board(board)

main()
