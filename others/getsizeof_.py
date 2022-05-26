from sys import getsizeof
from dataclasses import dataclass


@dataclass(slots=True)
class XY:
    y: str = "asdasdaaasf"


class X:
    def __init__(self):
        self.x = 124235
        self.y = "asdasd"


y = XY()
print(getsizeof(y))
x = "asdasd"
print(getsizeof(x))
