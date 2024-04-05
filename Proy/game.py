row1 = [" "," ", " "]
row2 = [" "," ", " "]
row3 = [" "," ", " "]
game = [row1,row2,row3]

def draw(game):
    for row in game:
        print(row)
        
def get_input(game):
    while True:
        row, col = map(int, input("Ingrese fila y columna (0 1): ").split())
        if row and col <= 2:
            if game[row][col] == " ":
                return row, col
            print("La posicion:", row, col,"ya esta ocupada !!")
        else:
            print("Ingrese una posicion valida (entre 0 - 2 para filas y col)")

def update_board(game, row, col, symbol):
    game[row][col] = symbol
    
def start(game):
    draw(game)
    while True:
        row, col = get_input(game)
        update_board(game, row , col , "X")
        draw(game)
 

start(game)