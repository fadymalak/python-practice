import random
from typing import Type
from abc import ABC , abstractmethod 
from metaclasses import DiceMeta
import logging
import sys

class DieLog(metaclass=DiceMeta):
    # __metaclass__ = DiceMeta
    logger:logging.Logger
    def __init__(self) -> None:
        self.face : int
        self.roll()

    @abstractmethod
    def roll(self) -> None : 
        ...

class Diex(DieLog):
    def roll(self) -> None:
        self.face = random.randint(1,6)


class Dice:
    def __init__(self, n:int, die_class:Type[DieLog]) -> None:
        self.dice = [die_class() for q in range(n)]
        self.adjust: int = 0

    def roll(self) -> None:
        for d in self.dice:
            d.roll()

    @property
    def total(self)-> int:
        print(f"{[x.face for x in self.dice]}")
        return sum(d.face for d in self.dice)

class DDice:
    def __init__(self, *die_class:Type[DieLog]) -> None:
        self.dice = [d() for d in die_class]
        self.adjust: int = 0

    def roll(self) -> None:
        for d in self.dice:
            d.roll()

    def plus(self,value) -> "DDice":
        self.adjust = value
        return self
    @property
    def total(self)-> int:
        print(f"{[x.face for x in self.dice]}")
        return sum(d.face for d in self.dice) + self.adjust

    def _add(self,adjust:int = 0) -> "DDice":
        pass

    def __add__(self,die_class) -> "DDice":
        if isinstance(die_class,type) and issubclass(die_class,DieLog):
            new_classes = [type(d) for d in self.dice] + [die_class]
            new = DDice(*new_classes)
        elif isinstance(die_class,int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
        return new

#config logging 
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


game  = Dice(3,Diex)
game.roll()
print(game.total)
print("###################")
game_multi = DDice(*[Diex]*4)
print(game_multi.total)
game_multi.plus(3).roll()
print(game_multi.total)

