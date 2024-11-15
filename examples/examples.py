from enum import Enum
from typing import Final
from warnings import deprecated


class Cool:
    a = 1

    def __init__(self):
        self.b = 2
        self.B: Final = 3
        self.C = 4

    @deprecated("Dont use me")
    def test(self):
        self.b = 5
        self.B = 6
        self.C = 7


cool = Cool()
cool.a
cool.b
cool.B
cool.C

cool.test()


class Colors(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


Colors.RED
