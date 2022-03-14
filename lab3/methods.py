from enum import Enum
from numpy import arange
from sympy import Symbol
from sympy.abc import x

from io_helper import fatal_error


class RectangleType(Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


def rectangle_method(t: RectangleType, f: Symbol, a: float, b: float, n: int) -> float:
    h = (b - a) / n  # длина отрезка
    a = arange(a, b, h)  # массив отрезков

    if t == RectangleType.LEFT:
        ans = h * sum(f.subs(x, xi) for xi in a)
    elif t == RectangleType.MIDDLE:
        ans = h * sum(f.subs(x, xi + h / 2) for xi in a)
    elif t == RectangleType.RIGHT:
        ans = h * sum(f.subs(x, xi + h) for xi in a)
    else:
        raise OSError("Дурка ебать")

    return ans


def simpsons_method(f: Symbol, a: float, b: float, n: int) -> float:
    if n % 2 != 0:
        fatal_error("Для метода Симпсона необходимо четное число разбиений.")
    odds, evens = 0, 0

    # инициализация
    h = (b - a) / n
    left = a
    right = left + h
    y0 = f.subs(x, left)
    # print(f"x0 {left:.3f}\t\ty0 {y0:.3f}")

    for i in range(1, n):
        curr = f.subs(x, right)
        if i % 2 == 0:
            evens += curr
        else:
            odds += curr
        left = right
        right = left + h
        # print(f"x{i} {left:.3f}\t\ty{i} {curr:.3f}")

    yn = f.subs(x, right)
    # print(f"xn {right:.3f}\t\tyn {yn:.3f}")
    return (h / 3) * (y0 + 4 * odds + 2 * evens + yn)
