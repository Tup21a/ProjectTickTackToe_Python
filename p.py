# row1 = ["X","X", "O"]
# row2 = ["O","X", "O"]
# row3 = ["O","X", "X"]
# game = [row1,row2,row3]

# def show(game):
#     for row in game:
#         print(row)
 

# show(game)


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-----------\n")

def check_win(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [
        [" " for _ in range(3)] for _ in range(3)
    ]

    current_player = "X"

    while True:
        print_board(board)

        print(f"Turno de {current_player}")

        try:
            row = int(input("Fila (1-3): "))
            col = int(input("Columna (1-3): "))
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")
            continue

        if board[row-1][col-1] != " ":
            print("Celda ocupada. Inténtalo de nuevo.")
            continue

        board[row-1][col-1] = current_player

        if check_win(board):
            print_board(board)
            print(f"¡{current_player} gana!")
            break

        if check_draw(board):
            print_board(board)
            print("Empate")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
