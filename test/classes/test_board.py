from connect4.classes.board import Board
from connect4.classes.player import Player

# class TestBoard():
#     def setup(self):
#         self.board = Board()


def test_board():
    b = Board()
    assert b.size == 7
    assert len(b.array) == 7
    assert len(b.array[0]) == 7
    assert b == b
    assert str(b) == "| | | | | | | |\n" * 7


def test_transposed_array():
    b = Board()
    b.array[0][6] = 1
    assert b.transposed_array()[6][0] == 1


def test_add_piece():
    p0 = Player(0)
    p1 = Player(1)
    b = Board()
    assert b.add_piece(p0, 0, 5)
    assert b.stack[0].player == p0
    assert b.stack[0].row == 6
    assert b.stack[0].col == 5

    for c in range(b.size):
        for r in range(b.size):
            if r == 6 and c == 5:
                assert b.array[r][c].player == p0
            else:
                assert b.array[r][c] is None

    assert b.add_piece(p1, 1, 5)
    assert b.stack[1].player == p1
    assert b.stack[1].row == 5
    assert b.stack[1].col == 5

    # test full column
    for i in range(7):
        assert b.add_piece(p0, i, 1)
    assert not b.add_piece(p0, 7, 1)
