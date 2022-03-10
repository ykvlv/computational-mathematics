from typing import Callable

from prettytable import PrettyTable

from io_helper import make_table, make_report, fatal_error, show_graph
from math_helper import dd, d


def chord_method(f: Callable[[float], float], a: float, b: float, accuracy: float,
                 max_iterations: int = 100) -> tuple[str, PrettyTable]:
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
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        rows.append([i, a, b, x, f(a), f(b), f(x), abs(a - b)])

        if abs(x - x0) < accuracy or i > max_iterations:
            show_graph(f, x)
            return make_report(f, i, x, abs(x - x0)), make_table(fields, rows)

        if f(x) * f(a) < 0:
            b = x
        else:
            a = x

        i += 1
        x0 = x


def simple_iteration_method(f: Callable[[float], float], approximation: float, accuracy: float,
                            max_iterations: int = 100) -> tuple[str, PrettyTable]:
    """ Метод простых итераций """
    fields, rows = ['i', 'xi', 'f(xi)', 'xi+1', 'φ(xi)', '|xi - xi+1|'], []

    def phi(x: float) -> float:
        _lambda = -1 / d(f, x)
        return x + _lambda * f(x)

    def calculate_answer(func: Callable[[float], float]) -> tuple[str, PrettyTable]:
        i = 0
        x0 = approximation

        while True:
            xi = func(x0)
            rows.append([i, x0, f(x0), xi, func(xi), abs(xi - x0)])

            if abs(xi - x0) < accuracy or i > max_iterations:
                show_graph(f, xi)
                return make_report(f, i, xi, abs(f(xi))), make_table(fields, rows)

            i += 1
            x0 = xi

    q = 0.5  # коэффициент сжатия
    if d(phi, approximation) <= q < 1:  # сходится ли метод простой итерации
        return calculate_answer(phi)
    # elif (еще одно допустимое условие):
    #     return calculate_answer(phi2)
    # elif (еще условие):
    #     return calculate_answer(phi3)
    else:
        fatal_error("Начальное приближение неверно, не выполняется достаточное условие сходимости метода.")


def secant_method(f: Callable[[float], float], a: float, b: float, accuracy: float,
                  max_iterations: int = 100) -> tuple[str, PrettyTable]:
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
            show_graph(f, xi)
            return make_report(f, i, xi, abs(xi - x0)), make_table(fields, rows)

        i += 1
        x0, xi = xi, calc(x0, xi)
