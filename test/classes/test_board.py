from connect4.classes.board import Board

# class TestBoard():
#     def setup(self):
#         self.board = Board()


def test_board():
    b = Board()
    assert b.size == 7
    assert len(b.array) == 7
    assert len(b.array[0]) == 7

    assert b == b
