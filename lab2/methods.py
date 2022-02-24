import sys
from typing import Callable

from prettytable import PrettyTable
from termcolor import cprint

from io_helper import make_table, make_report
from math_helper import dd


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

    while abs(a - b) > accuracy and i < max_iterations:
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x

        x0 = x
        i += 1
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        rows.append([i, a, b, x, f(a), f(b), f(x), abs(a - b)])

    return make_report(f, i, x, abs(a - b)), make_table(fields, rows)


def secant_method(left_border: float, right_border: float, accuracy: float) -> tuple[str, PrettyTable]:
    def f(x):
        return x ** 3 - 2.92 * x ** 2 + 1.435 * x + 0.791

    def cal(_prev_x, _xi):
        return xi - (xi - prev_x) * f(xi) / (f(xi) - f(prev_x))

    # условие применимости метода Ньютона
    if f(left_border) * f(right_border) > 0:
        cprint(f"На концах отрезка [{left_border}, {right_border}] функция имеет одинаковые знаки.\n"
               f"На отрезке либо нет корней, либо их четное количество. Пожалуйста, уточните интервал.", "red")
        sys.exit(1)

    table = PrettyTable(["N", "X(k-1)", "f(X(k-1))", "X(k)", "f(X(k))", "X(k+1)", "f(X(k+1))", "|X(k)-X(k+1)|"])
    table.float_format = ".5"
    table.border = False

    n = 0
    # TODO Выбор x0 ИСПРАВИТЬ
    prev_x = right_border

    xi = prev_x * accuracy * 2  # x1 выбирается рядом с x0 самостоятельно
    table.add_row([n, prev_x, f(prev_x), xi, f(xi), cal(prev_x, xi), f(cal(prev_x, xi)), abs(xi - cal(prev_x, xi))])
    while abs(xi - prev_x) > accuracy:
        k = xi
        xi = cal(prev_x, xi)
        prev_x = k
        n += 1
        table.add_row([n, prev_x, f(prev_x), xi, f(xi), cal(prev_x, xi), f(cal(prev_x, xi)), abs(xi - cal(prev_x, xi))])

    return f"Выполнено решение уравнения методом секущих.\n" \
           f"Х = {xi}\n" \
           f"Количество итераций n = {n}\n" \
           f"Критерий окончания итерационного процесса |a-b| = {abs(xi - prev_x)}\n" \
           f"f({xi}) = {f(xi)}", table


def simple_iteration_method(approximation: float, accuracy: float):
    # TODO бред lamb
    def f1(x):
        return x + lamb * (x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458)

    def f2(x):
        return (3.125 * x ** 2 + 3.5 * x - 2.458) ** (1 / 3)

    def calculate_answer(func):
        # TODO таблицу
        table = PrettyTable()

        x0 = approximation
        n = 0
        while True:
            x1 = func(x0)
            n += 1
            f = x1 ** 3 - 3.125 * x1 ** 2 - 3.5 * x1 + 2.458
            # Для более точного ответа
            if abs(f) <= accuracy:
                break
            x0 = x1

        return f"Выполнено решение уравнения  методом простых итераций.\n" \
               f"X = {x1}\n" \
               f"Количество итераций n = {n}\n" \
               f"f({x1})={f}", table

    # подставим в производную функцию значение начального приближения
    f_approximation = 3 * approximation ** 2 - 6.25 * approximation - 3.5
    lamb = -1 / f_approximation

    # сходится ли метод простой итерации
    if abs(3 * lamb * approximation ** 2 - 6.25 * lamb * approximation + 1 - 3.5 * lamb) < 1 and (
            approximation > 0 or approximation < -1):
        # достаточное условие сходимости выполнено и начальное приближение не лежит в интервале от -1 до 0
        return calculate_answer(f1)
    else:
        fi1 = 6.25 * approximation + 3.5 / 3 / ((3.125 * approximation ** 2 + 3.5 * approximation - 2.458) ** 2) ** (
                1 / 3)
        if abs(fi1) < 1:
            return calculate_answer(f2)
        else:
            cprint("Начальное приближение неверно, не выполняется достаточное условие сходимости метода.", "red")
            sys.exit(1)
