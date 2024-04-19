import random
import os, time

game = [[" "," "," "], [" "," "," "], [" "," "," "]]


def draw(game):
	for x in game:
		print(x)

def update_board(game, row, col, symbol):
	game[row][col] = symbol

def get_input():
	row, col = map(int, input("ingrese x, y: ").split())
	return row, col

def winer(game, symbol):
	for i in range(3):
		# verifica las filas - horizontal
		if game[i][0] == symbol and game[i][1] == symbol and game[i][2] == symbol:
			return True
		# verifica columnas - vertical
		if game[0][i] == symbol and game[1][i] == symbol and game[2][i] == symbol:
			return True
	# verifica diagonales
	if (game[0][0] == symbol and game[1][1] == symbol and game[2][2] == symbol) or (game[0][2] == symbol and game[1][1] == symbol and game[0][0] == symbol):
		return True
	return False
	
def start(game):
    sw = 1
    draw(game)
    for i in range(9):
        if i % 2 == 0:
            while True:
                row, col = get_input()
                if row > 2 or col > 2:
                    print("Ingrese una posicion valida existente entre 0 - 2")
                else:
                    if game[row][col] == " ":
                        update_board(game, row, col, "x")
                        break
                    print(f"La posicion {row} {col} ya existe, ingrese otra posicion !!")
            if winer(game, "x"):
                print('\t Ganaste "x" !!!')
                sw = 0
        else:
            while True:
                row, col = random.randint(0,2), random.randint(0,2)
                if game[row][col] == " ":
                    update_board(game, row, col, "o")
                    print("La Computadora juega: ", row, col)
                    break
            if winer(game, "o"):
                print('\t Perdiste !, ganó "o"')
                sw = 0
        draw(game)
        if sw == 0:
            break
    if sw == 1:
        print("EMPATE !!")

    			
  
  
while True:
	print("\t Nuevo Juego")
	start(game)
	if input("Desea iniciar nuevo juego? (s/n)") == "s":
		os.system("cls") #clear
	else:
		break