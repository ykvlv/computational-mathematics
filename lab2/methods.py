from typing import Callable, Tuple

from io_helper import make_table, make_report, fatal_error, show_graph, show_graph_2
from math_helper import dd, d


def chord_method(f: Callable[[float], float], a: float, b: float, accuracy: float,
                 max_iterations: int = 100) -> Tuple:
    """ Метод хорд """
    fields, rows = ['i', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|a - b|'], []

    # Проверка на наличие корня
    if f(a) * f(b) >= 0:
        fatal_error(f"На концах отрезка [{a}, {b}] функция имеет одинаковые знаки.\n"
                    f"На отрезке либо нет корней, либо их четное количество. Пожалуйста, уточните интервал.")

    # Выбор начального приближения
    if f(a) * dd(f, a) > 0:
        x0 = a
    else:
        x0 = b

    i = 0
    while True:
        xi = (a * f(b) - b * f(a)) / (f(b) - f(a))
        rows.append([i, a, b, xi, f(a), f(b), f(xi), abs(a - b)])

        if (abs(xi - x0) < accuracy and abs(f(xi)) < accuracy) or i > max_iterations:
            return make_report(f, i, xi, abs(xi - x0)), make_table(fields, rows), (show_graph, f, xi)

        if f(xi) * f(a) < 0:
            b = xi
        else:
            a = xi

        i += 1
        x0 = xi


def simple_iteration_method(f: Callable[[float], float], a: float, b: float, accuracy: float,
                            max_iterations: int = 100) -> Tuple:
    """ Метод простой итерации """
    fields, rows = ['i', 'xi', 'f(xi)', 'xi+1', 'φ(xi)', '|xi - xi+1|'], []
    o = max(d(f, a), d(f, b))

    def phi(x: float) -> float:
        _lambda = -1 / o
        return x + _lambda * f(x)

    def calculate_answer(func: Callable[[float], float], x0) -> Tuple:
        i = 0
        while True:
            xi = func(x0)
            rows.append([i, x0, f(x0), xi, func(xi), abs(xi - x0)])

            if abs(xi - x0) < accuracy or i > max_iterations:
                return make_report(f, i, xi, abs(f(xi))), make_table(fields, rows), (show_graph, f, xi)

            i += 1
            x0 = xi

    print(d(phi, a), d(phi, b))
    if abs(d(phi, a)) < 1 and abs(d(phi, b)) < 1:
        # Выбор начального приближения
        if f(a) * dd(f, a) > 0:
            return calculate_answer(phi, a)
        else:
            return calculate_answer(phi, b)
    # elif (еще одно допустимое условие):
    #     return calculate_answer(phi2)
    # elif (еще условие):
    #     return calculate_answer(phi3)
    else:
        fatal_error("Интервал неверный, не выполняется достаточное условие сходимости метода.")


def secant_method(f: Callable[[float], float], a: float, b: float, accuracy: float,
                  max_iterations: int = 100) -> Tuple:
    """ Метод секущих """
    fields, rows = ["i", "xi-1", "f(xi-1)", "xi", "f(xi)", "xi+1", "f(xi+1)", "|xi - xi+1|"], []

    def calc(prev_x, curr_x):
        return curr_x - (curr_x - prev_x) * f(curr_x) / (f(curr_x) - f(prev_x))

    # условие применимости метода Ньютона
    if f(a) * f(b) >= 0:
        fatal_error(f"На концах отрезка [{a}, {b}] функция имеет одинаковые знаки.\n"
                    f"На отрезке либо нет корней, либо их четное количество. Пожалуйста, уточните интервал.")

    # Выбор начального приближения
    if f(a) * dd(f, a) > 0:
        x0 = a
    else:
        x0 = b

    i = 0
    xi = x0 * accuracy * 2
    while True:
        rows.append([i, x0, f(x0), xi, f(xi), calc(x0, xi), f(calc(x0, xi)), abs(xi - calc(x0, xi))])

        if abs(xi - x0) < accuracy or i > max_iterations:
            return make_report(f, i, xi, abs(xi - x0)), make_table(fields, rows), (show_graph, f, xi)

        i += 1
        x0, xi = xi, calc(x0, xi)


def system_simple_iteration_method(_f, func1, a1: float, func2, a2: float, accuracy: float,
                                   max_iterations: int = 100) -> Tuple:
    """ Система методом простых итераций """
    fields, rows = ["i", "x0", "y0", "xi", "yi", "f1(x0, y0)", "f2(x0, y0)", "|x0 - xi|", "|y0 - yi|"], []

    f1, f2 = func1[1], func2[1]
    x0, y0 = a1, a2

    i = 0
    while True:
        xi = f1(x0, y0)
        yi = f2(x0, y0)
        print(xi, yi)
        rows.append([i, x0, y0, xi, yi, f1(x0, y0), f2(x0, y0), abs(xi - x0), abs(yi - y0)])
        if abs(xi - x0) < accuracy or abs(yi - y0) < accuracy or i > max_iterations:
            return f"Корни системы уравнений:\nx1 — {xi}, x2 — {yi}", make_table(fields, rows), \
                   (show_graph_2, func1[2], func2[2])

        i += 1
        x0, y0 = xi, yi
