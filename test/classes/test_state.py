from connect4.classes.board import Board
from connect4.classes.player import Player
from connect4.classes.state import State


def test_state():
    p0 = Player(0)
    p1 = Player(1)
    b = Board()
    s = State(b, None, [p0, p1], 0, 0)
    assert s.turn == 0
    assert s.board == b
    assert s.players[0] == p0
    assert s.players[1] == p1
    assert s.current_player_ind == 0
    assert s.turn == 0
    assert s.previous is None
    assert s == s

    b2 = Board(8)
    s2 = State(b2, s)
    assert s2.turn == 1
    assert s2.board == b2
    assert s2.players[0] == p0
    assert s2.players[1] == p1
    assert s2.current_player_ind == 1
    assert s2.previous == s
