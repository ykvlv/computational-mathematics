from typing import Callable


def d(function: Callable[[float], float], value: float, h: float = 0.000000001) -> float:
    """ Считает производную функции """
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    return slope


def dd(function: Callable[[float], float], value: float, h: float = 0.000000001) -> float:
    """ Считает производную второго порядка """
    return (d(function, value + h, h) - d(function, value, h)) / h
