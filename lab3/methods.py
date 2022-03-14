from enum import Enum
from typing import Callable
from numpy import arange


class RectangleType(Enum):
    LEFT = 1
    RIGHT = 2
    MIDDLE = 3


def rectangle_method(t: RectangleType, f: Callable, a: float, b: float, n: int) -> None:
    h = (b - a) / n  # длина отрезка
    a = arange(a, b, h)  # массив отрезков

    if t == RectangleType.LEFT:
        ans = h * sum(f(x) for x in a)
    elif t == RectangleType.RIGHT:
        ans = h * sum(f(x + h) for x in a)
    elif t == RectangleType.MIDDLE:
        ans = h * sum(f(x + h / 2) for x in a)
    else:
        raise OSError("Дурка ебать")

    return ans


def simpsons_method(f: Callable, a: float, b: float, n: int) -> None:
    pass
