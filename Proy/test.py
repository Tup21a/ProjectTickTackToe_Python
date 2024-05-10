import pytest
from game import draw, update_board, get_valid_input, winner, play_user, play_computer, start


def test_update_board():
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    update_board(game, 0, 0, "x")
    assert game[0][0] == "x"


def test_winner():
    game = [["x", "o", "x"], ["o", "x", "o"], ["x", "o", "x"]]
    assert winner(game, "x") == True
    game = [["o", "x", "o"], ["x", "o", "x"], ["o", "x", "o"]]
    assert winner(game, "o") == True
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    assert winner(game, "x") == False
    assert winner(game, "o") == False


def test_play_computer():
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    assert play_computer(game) == False
    game = [["o", "o", "o"], [" ", " ", " "], [" ", " ", " "]]
    assert play_computer(game) == True


if __name__ == "__main__":
    pytest.main()

#cd ubicacion
#python -m pytest test.py
