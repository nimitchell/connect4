from connect4.classes.player import Player


def test_player():
    p = Player(0)
    assert p.number == 0
    assert p.name == "player_0"
    assert str(p) == "player_0 (Player:0)"
    assert p == p

    # test with name input
    p2 = Player(1, "Nicholas")
    assert p2.name == "Nicholas"
    assert p2.number == 1
    assert str(p2) == "Nicholas (Player:1)"
