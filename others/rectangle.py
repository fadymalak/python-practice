from typing import List
import math


class Point(object):
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self._x - other._x, self._y - other._y)


p1 = Point()

# _Class__attr  to Access Protected attributes
# print(p1._Point__x)
p2 = Point(4, 4)

dis = p1.calculate_distance(p2)
print(dis)
