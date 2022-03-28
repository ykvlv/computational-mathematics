from enum import Enum
from numpy import arange
from sympy import Symbol
from sympy.abc import x
from termcolor import cprint

from io_helper import fatal_error


class RectangleType(Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


def rectangle_method(t: RectangleType, f: Symbol, a: float, b: float, n: int,
                     accuracy: float, check_runge: bool) -> float:
    h = (b - a) / n  # длина отрезка
    if a == b:
        return 0
    arr = arange(a, b, h)  # массив отрезков

    if t == RectangleType.LEFT:
        ans = h * sum(f.subs(x, xi) for xi in arr)
    elif t == RectangleType.MIDDLE:
        ans = h * sum(f.subs(x, xi + h / 2) for xi in arr)
    elif t == RectangleType.RIGHT:
        ans = h * sum(f.subs(x, xi + h) for xi in arr)
    else:
        raise RuntimeError("Поведение не определено")

    if check_runge:
        runge_ans = rectangle_method(t, f, a, b, n * 2, accuracy, False)
        cprint(f"eps={abs(runge_ans - ans):.4f}\tn={n}: {ans:.4f}\tn={2*n}: {runge_ans:.4f}", "blue")
        if abs(runge_ans - ans) < accuracy:
            return runge_ans
        else:
            return rectangle_method(t, f, a, b, n * 2, accuracy, True)
    return ans


def simpsons_method(f: Symbol, a: float, b: float, n: int, accuracy: float, check_runge: bool) -> float:
    if n % 2 != 0:
        fatal_error("Для метода Симпсона необходимо четное число разбиений.")
    h = (b - a) / n  # длина каждого отрезка
    arr = arange(a, b, h)  # массив отрезков

    y0 = f.subs(x, a)  # y нулевое
    yn = f.subs(x, b)  # y последнее

    odds = sum(f.subs(x, xi) for xi in arr[1:n:2])  # результат функции на нечетных отрезках
    evens = sum(f.subs(x, xi) for xi in arr[2:n:2])  # результат функции на четных отрезках

    ans = (h / 3) * (y0 + 4 * odds + 2 * evens + yn)  # формула Симпсона

    if check_runge:
        runge_ans = simpsons_method(f, a, b, n * 2, accuracy, False)
        cprint(f"eps={abs(runge_ans - ans):.4f}\tn={n}: {ans:.4f}\tn={2*n}: {runge_ans:.4f}", "blue")
        if abs(runge_ans - ans) < accuracy:
            return runge_ans
        else:
            return simpsons_method(f, a, b, n * 2, accuracy, True)
    return ans
