# -------- Global Variable ----------
# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True

# Won or Tie
winner = None

# who's turn
import random
x = random.randrange(0, 2)
if x == 0:
    current_player = "O"
else:
    current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")

def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_palyer()

    # game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("! Tie.")

def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9 : ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9 : ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    # check rows
    row_winner = check_rows()
    # check colums
    colum_winner = check_colums()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_rows():
    global game_still_going
    # check if any row is match then call winner
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False
    # return the winner X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_colums():
    global game_still_going
    # check if any colum is match then call winner
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        game_still_going = False
    # return the winner X or O
    if col1:
        return board[1]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    # check if any diagonal is match then call winner
    diago1 = board[0] == board[4] == board[8] != "-"
    diago2 = board[6] == board[4] == board[2] != "-"
    if diago1 or diago2:
        game_still_going = False
    # return the winner X or O
    if diago1:
        return board[0]
    elif diago2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_palyer():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()

a = input("")