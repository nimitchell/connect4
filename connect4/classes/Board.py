from connect4.classes.piece import Piece
from connect4.classes.player import Player


class Board:
    def __init__(self, size=7):
        self.size = size
        self.array = [[None for col in range(self.size)] for row in range(self.size)]
        self.stack = []

    def __str__(self):
        board_string = ""
        for row in self.array:
            for p in row:
                board_string += f"|{p.player.number if p else " "}"
            board_string += "|\n"
        return board_string

    def __eq__(self, other):
        return (
            self.size == other.size
            and self.array == other.array
            and self.stack == other.stack
        )

    def transposed_array(self):
        return [[row[col] for row in self.array] for col in range(self.size)]

    def add_piece(self, player: Player, turn: int, col: int) -> bool:
        for row, p in reversed(list(enumerate(self.transposed_array()[col]))):
            if p is None:
                new_piece = Piece(player, turn, row, col)
                self.stack.append(new_piece)
                self.array[row][col] = new_piece
                return True
        return False
