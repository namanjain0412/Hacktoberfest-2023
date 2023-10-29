# Tic-Tac-Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board():
    print(" | ".join(board[:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:9]))

# Function to check if the game is over
def is_game_over():
    # Check rows, columns, and diagonals
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    # Check for a tie
    if " " not in board:
        return True
    return False

# Function to play the game
def play_game():
    player = "X"
    while not is_game_over():
        print_board()
        try:
            move = int(input(f"Player {player}, enter your move (0-8): "))
            if 0 <= move < 9 and board[move] == " ":
                board[move] = player
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")

    print_board()
    if is_game_over() and not any(" " in cell for cell in board):
        print("It's a tie!")
    else:
        print(f"Player {player} wins!")

# Start the game
play_game()
