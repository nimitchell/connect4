from typing import Optional, Self

from connect4.classes.board import Board
from connect4.classes.player import Player


class State:
    def __init__(
        self,
        board: Board,
        previous: Optional[Self] = None,
        players: Optional[list[Player]] = None,
        turn: int = 0,
        current_player_ind: int = 0,
    ):
        self.board = board
        self.previous = previous
        # build off previous state
        if previous:

            self.players: Optional[list[Player]] = previous.players
            len_players = len(players) if players else 0
            self.current_player_ind: int = (
                0
                if previous.current_player_ind + 1 == len_players
                else previous.current_player_ind + 1
            )
            self.turn = turn + 1

        else:
            self.players = players
            self.current_player_ind = current_player_ind
            self.turn = turn

    def __str__(self):
        return (
            f"Players:\n"
            f"{[f'{p.number}: {p.name}\n' for p in self.players]}"
            f"Turn: {self.turn} ({self.players[self.current_player_ind].name})\n"
            f"{self.board}\n"
            f"Previous turn:{f'{self.previous.turn} ({self.players[self.previous.current_player_ind].name if self.previous else ''})'}"
        )

    def __eq__(self, other):
        return (
            self.board == other.board
            and self.previous == other.previous
            and self.players == other.players
            and self.turn == other.turn
            and self.current_player_ind == other.current_player_ind
        )
