import sys
from typing import Callable

from prettytable import PrettyTable
from termcolor import cprint

from io_helper import make_table, make_report, make_graph
from math_helper import dd, d


def chord_method(f: Callable[[float], float], a: float, b: float, accuracy: float,
                 max_iterations: int = 100) -> tuple[str, PrettyTable]:
    """ Метод хорд """
    fields = ['i', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|a - b|']
    rows = []

    # Выбор начального приближения
    if f(a) * dd(f, a) > 0:
        x0 = a
    elif f(b) * dd(f, b) > 0:
        x0 = b
    else:
        # можно продумать условие
        x0 = a

    # инициализация
    i = 0
    x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    rows.append([i, a, b, x, f(a), f(b), f(x), abs(a - b)])

    while abs(x - x0) > accuracy and i < max_iterations:
        i += 1

        if f(x) * f(a) < 0:
            b = x
        else:
            a = x

        x0, x = x, (a * f(b) - b * f(a)) / (f(b) - f(a))
        rows.append([i, a, b, x, f(a), f(b), f(x), abs(a - b)])

    make_graph(abs(x), abs(f(x)), f)

    return make_report(f, i, x, abs(x - x0)), make_table(fields, rows)


def secant_method(f: Callable[[float], float], a: float, b: float, accuracy: float,
                  max_iterations: int = 100) -> tuple[str, PrettyTable]:
    """ Метод секущих """
    fields = ["i", "xi-1", "f(xi-1)", "xi", "f(xi)", "xi+1", "f(xi+1)", "|xi - xi+1|"]
    rows = []

    def cal(prev_x, now_x):
        return now_x - (now_x - prev_x) * f(now_x) / (f(now_x) - f(prev_x))

    # условие применимости метода Ньютона
    if f(a) * f(b) > 0:
        cprint(f"На концах отрезка [{a}, {b}] функция имеет одинаковые знаки.\n"
               f"На отрезке либо нет корней, либо их четное количество. Пожалуйста, уточните интервал.", "red")
        sys.exit(1)

    # выбор x0
    if f(a) * 2 * (3 * a - 5.84) > 0:
        x0 = a
    else:
        x0 = b

    # инициализация
    i = 0
    xi = x0 * accuracy * 2  # x1 выбирается рядом с x0 самостоятельно
    rows.append([i, x0, f(x0), xi, f(xi), cal(x0, xi), f(cal(x0, xi)), abs(xi - cal(x0, xi))])

    while abs(xi - x0) > accuracy and i < max_iterations:
        i += 1

        x0, xi = xi, cal(x0, xi)
        rows.append([i, x0, f(x0), xi, f(xi), cal(x0, xi), f(cal(x0, xi)), abs(xi - cal(x0, xi))])

    return make_report(f, i, xi, abs(xi - x0)), make_table(fields, rows)


def simple_iteration_method(f: Callable[[float], float], approximation: float, accuracy: float,
                            max_iterations: int = 100) -> tuple[str, PrettyTable]:
    """ Метод простых итераций """

    def calculate_answer(func: Callable[[float], float]) -> tuple[str, PrettyTable]:
        fields = ['i', 'xi', 'f(x)', 'xi+1', 'φ(xi)', '|xi - xi+1|']
        rows = []

        # инициализация
        i = 0
        x0 = approximation
        x = func(x0)
        rows.append([i, x0, f(x0), x, func(x), abs(x - x0)])

        while abs(f(x)) > accuracy and i < max_iterations:
            i += 1

            x0, x = x, func(x0)
            rows.append([i, x0, f(x0), x, func(x), abs(x - x0)])

        return make_report(func, i, x, abs(f(x))), make_table(fields, rows)

    # подставим в производную функцию значение начального приближения
    f_approximation = d(f, approximation)
    lmb = -1 / f_approximation
    q = 1

    # сходится ли метод простой итерации
    if abs(3 * lmb * approximation ** 2 - 5.84 * lmb * approximation + q + 1.435 * lmb) < q and (
            approximation > 0 or approximation < -1):
        # достаточное условие сходимости выполнено и начальное приближение не лежит в интервале от -1 до 0
        return calculate_answer(lambda x: x + lmb * f(x))
    else:
        fi1 = (- 5.84 * approximation + 1.435) / 3 / (
                    (- 2.92 * approximation ** 2 + 1.435 * approximation + 0.791) ** 2) ** (1 / 3)
        if abs(fi1) < 1:
            return calculate_answer(lambda x: - 2.92 * x ** 2 + 1.435 * x + 0.791)
        else:
            cprint("Начальное приближение неверно, не выполняется достаточное условие сходимости метода.", "red")
            sys.exit(1)
