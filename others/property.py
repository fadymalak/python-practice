"""
use @property to support validation/processing/calculation/hide attr
     when set property instead set property directly
"""


class Car:
    def __init__(self, speed: int) -> None:
        self.speed = speed

    @property
    def speed(self) -> int:
        print("getter ")
        return self._max_speed

    @speed.setter
    def speed(self, value) -> None:
        print("setting value")
        self._max_speed = value

    @speed.deleter
    def speed(self) -> None:
        print("deleteing speed")
        del self._max_speed


car = Car(speed=120)
car.speed
del car.speed
