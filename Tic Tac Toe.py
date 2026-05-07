# Tic Tac Toe Game in Python

board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check winner
def check_winner(player):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check draw
def check_draw():
    return " " not in board

# Main game function
def play_game():
    current_player = "X"

    while True:
        print_board()

        try:
            move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position! Choose between 1 and 9.")
                continue

            if board[move] != " ":
                print("Position already taken!")
                continue

            board[move] = current_player

            if check_winner(current_player):
                print_board()
                print(f"🎉 Player {current_player} wins!")
                break

            if check_draw():
                print_board()
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number.")

# Start the game
play_game()