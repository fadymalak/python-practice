from typing import Tuple


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.soft, self.hard = self._pionts()

    # private method
    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)
