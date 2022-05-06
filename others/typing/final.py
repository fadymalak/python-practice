from typing import final
from abc import ABC, abstractmethod

"""
typing.final prevent from overriden speed method again

"""


class ABSCar:
    @abstractmethod
    def speed(self, max: int) -> None:
        pass


class Ford(ABSCar):
    @final
    def speed(self, max: int) -> None:

        self._max_speed = max + 10


@final
class BMW(ABSCar):
    pass


class SubBMW(BMW):  # Error reported to type checker
    pass


class SubFord(Ford):
    def speed(self, max: int) -> None:  # Error reported by type checker
        self._max_speed = max + 1
