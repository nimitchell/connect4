from typing import Optional

from player import Player


class Piece:
    def __init__(
        self,
        player_num: Optional[int] = None,
        player: Optional[Player] = None,
        turn: int = 0,
        row: int = 0,
        col: int = 0,
    ):
        self.player_num = player_num
        self.player = player
        self.turn = turn
        self.row = row
        self.col = col

    def __str__(self):
        return f"{self.player_num}({self.player}, turn:{self.turn}, ({self.row},{self.col}))"

    def get_player_num(self) -> Optional[int]:
        return self.player_num
