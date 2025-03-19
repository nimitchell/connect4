from typing import Optional

from connect4.classes.player import Player


class Piece:
    def __init__(
        self,
        player: Optional[Player] = None,
        turn: int = 0,
        row: int = 0,
        col: int = 0,
    ):
        self.player = player
        self.turn = turn
        self.row = row
        self.col = col

    def __str__(self):
        return f"{self.player.number}({self.player.name}, turn:{self.turn}, ({self.row},{self.col}))"

    def __eq__(self, other):
        return (
            self.player == other.player
            and self.turn == other.turn
            and self.row == other.row
            and self.col == other.col
        )

    def get_player_num(self) -> Optional[int]:
        return self.player.number if self.player else None
