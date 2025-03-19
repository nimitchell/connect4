from connect4.classes.board import Board
from connect4.classes.player import Player


class Game:
    def __init__(
        self,
        board: Board,
        players: list[Player],
        turn: int = 0,
    ):
        self.board = board
        self.players = players
        self.turn = turn
        self.num_players = len(players)

    def __str__(self):
        return (
            f"Players:\n"
            f"{''.join([f'{p.number}: {p.name}\n' for p in self.players])}"
            f"Turn: {self.turn} ({self.get_current_player().name})\n"
            f"{self.board}"
        )

    def __eq__(self, other):
        return (
            self.board == other.board
            and self.players == other.players
            and self.turn == other.turn
            and self.num_players == other.num_players
        )

    def get_current_player(self) -> Player:
        return self.players[self.turn % self.num_players]
