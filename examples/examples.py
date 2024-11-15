import math
from enum import Enum
from typing import Final
from warnings import deprecated

x = 1
y: Final = 2


class Cool:
    a = 1

    def __init__(self):
        self.b = 2
        self.B: Final = 3
        self.c: Final = 3  # not working for members
        self.C = 4
        self.ok: list[list[str]] = []

    def okidoke(self) -> int:
        return 5

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

cool.okidoke()
cool.test()


class Colors(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


Colors.RED

min(1, 2, 3)

math.pi
math.e
