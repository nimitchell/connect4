from connect4.classes.piece import Piece
from connect4.classes.player import Player


def test_piece():
    player = Player(0)
    piece = Piece(player)
    assert piece.row == 0
    assert piece.col == 0
    assert piece.player == player
    assert piece.turn == 0
    piece2 = Piece(player)
    assert piece == piece2


def test_get_player_num():
    player = Player(3)
    piece = Piece(player)
    player_num = piece.get_player_num()
    assert player_num == 3
