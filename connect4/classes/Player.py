class Player:
    def __init__(self, number: int, name: str = ""):
        self.number = number
        self.name = name if len(name) > 0 else f"player_{number}"

    def __str__(self):
        return f"{self.name} (Player:{self.number})"

    def __eq__(self, other):
        return self.number == other.number and self.name == other.name
