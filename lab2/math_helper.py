equation = "x³ - 2.92x² + 1.435x + 0.791"


def f(x: float):
    """ Используемая функция """
    return x ** 3 - 2.92 * x ** 2 + 1.435 * x + 0.791


def d(function, value: float, h: float = 0.000000001):
    """ Считает производную функции """
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    return slope


def dd(function, value: float, h: float = 0.000000001):
    """ Считает производную второго порядка """
    return (d(function, value + h, h) - d(function, value, h)) / h
