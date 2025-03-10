from typing import Optional, Self

from Board import Board
from Player import Player


class State:
    def __init__(
        self,
        players: list[Player],
        board: Board,
        turn: int,
        current_player: Player,
        previous: Optional[Self],
    ):
        self.board = board
        self.players = players
        self.current_player = current_player
        self.turn = turn
        self.previous = previous

    def __str__(self):
        return (
            f"Players:\n"
            f"{[f'{p.player_num}: {p.name}\n' for p in self.players]}"
            f"Turn: {self.turn} ({self.current_player.name})\n"
            f"{self.board}\n"
            f"Previous turn:{f'{self.previous.turn} ({self.previous.current_player.name if self.previous else ''})'}"
        )
