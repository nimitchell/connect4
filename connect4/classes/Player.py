class Player:
    def __init__(self, number: int, name: str = f""):
        self.number = number
        self.name = name if len(name) > 0 else f"player_{number}"
        self.wins = 0

    def __str__(self):
        return f"{self.name}(player:{self.player_num}, wins: {self.wins})"
