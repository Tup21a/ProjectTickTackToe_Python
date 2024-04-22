import random
import os, time


def draw(game):
	for x in game:
		print(x)

def update_board(game, row, col, symbol):
	game[row][col] = symbol


def parse_to_ints(user_input):
    return map(int, user_input.split())


def get_input():
    user_input = input("ingrese x, y: ")
    return parse_to_ints(user_input)


def winer(game, symbol):
	for i in range(3):
		# verifica las filas - horizontal
		if game[i][0] == symbol and game[i][1] == symbol and game[i][2] == symbol:
			return True
		# verifica columnas - vertical
		if game[0][i] == symbol and game[1][i] == symbol and game[2][i] == symbol:
			return True
	# verifica diagonales
	if (game[0][0] == symbol and game[1][1] == symbol and game[2][2] == symbol) or (game[0][2] == symbol and game[1][1] == symbol and game[2][0] == symbol): #tuve error
		return True
	return False


def start():
    game = [[" "," "," "], [" "," "," "], [" "," "," "]]
    #game = [[" " for _ in range(3)] for _ in range(3)]
    sw = 1
    sw_turn = random.randint(0,1)
    draw(game)
    for i in range(9):
        if sw_turn == 1:
            while True:
                row, col = get_input()
                if 0 <= row < 3 and 0 <= col < 3: #antes solo verficaba si fuese menor a 3
                    if game[row][col] == " ":
                        update_board(game, row, col, "x")
                        sw_turn = 0
                        break
                    print(f"La posicion {row} {col} ya esta ocupada, ingrese otra posicion !!")
                else:
                    print("Ingrese una posicion valida existente entre 0 - 2")
            if winer(game, "x"):
                for j in range(5):
                    print('\t\t Ganaste "x" !!!')
                    draw(game)
                    time.sleep(1)
                    os.system("cls")
                sw = 0
                print('\t\t Ganaste "x" !!!')
        else:
            while True:
                row, col = random.randint(0,2), random.randint(0,2)
                if game[row][col] == " ":
                    update_board(game, row, col, "o")
                    print("La Computadora juega: ", row, col)
                    sw_turn = 1
                    break
            if winer(game, "o"):
                print('\t\t Perdiste !!, ganó "o"')
                sw = 0
        draw(game)
        if sw == 0:
            break
    if sw == 1:
        print("EMPATE !!")



if __name__ == "__main__":
    while True:
        print("\t Nuevo Juego")
        start()
        if input("Desea iniciar nuevo juego? (s/n)") == "s":
            os.system("cls") #clear
        else:
            break