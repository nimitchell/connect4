from Piece import Piece


class Board:
    def __init__(self, size=7):
        self.size = size
        self.array = [
            [Piece(row=row, col=col) for col in self.size] for row in self.size
        ]

    def __str__(self):
        board_string = ""
        for row in self.array:
            for col in row:
                num = col.get_player_num
                board_string += f"|{num if num else " "}"
            board_string += "|\n"
        return board_string[:-1]  # TODO:validate that this works as expected
