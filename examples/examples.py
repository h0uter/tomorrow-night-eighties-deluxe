import math
from enum import Enum
from typing import Final
from warnings import deprecated

import numpy as np


class Colors(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class Cool:
    a = Colors.RED

    def __init__(self):
        self.b = np.array([1, 2, 3])
        self.B: Final = 3
        self.c: Final = 3  # not working for members
        self.C = math.pi
        self.ok: list[list[str]] = []
        self.ok2 = min(1, 2, 3)

    @deprecated("Dont use me")
    def test(self) -> int:
        return 5


cool = Cool()
cool.test()


def wow() -> str:
    return "wow"
