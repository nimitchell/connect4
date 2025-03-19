from connect4.classes.board import Board
from connect4.classes.game import Game
from connect4.classes.player import Player


def test_game():
    p0 = Player(0)
    p1 = Player(1)
    b = Board()
    g1 = Game(b, [p0, p1])
    assert g1.turn == 0
    assert g1.board == b
    assert g1.players[0] == p0
    assert g1.players[1] == p1
    assert g1.turn == 0
    assert g1.num_players == 2
    # test __eq__
    assert g1 == g1
    # test __str__
    assert str(g1) == (
        "Players:\n" "0: player_0\n" "1: player_1\n" "Turn: 0 (player_0)\n"
    ) + ("| | | | | | | |\n" * 7)

    b2 = Board(8)
    g2 = Game(b2, [p1, p0], 4)
    assert g2.turn == 4
    assert g2.board == b2
    assert g2.players[0] == p1
    assert g2.players[1] == p0


def test_whose_turn():
    p0 = Player(0)
    p1 = Player(1)
    b = Board()
    g1 = Game(b, [p0, p1])
    assert g1.get_current_player() == p0
    g1.turn = 5
    assert g1.get_current_player() == p1
