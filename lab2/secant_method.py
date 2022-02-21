import sys

from prettytable import PrettyTable
from termcolor import cprint

from iohandler import equation


def secant_method(left_border: float, right_border: float, accuracy: float):
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
    if f(left_border) * (6 * left_border - 6.25) > 0:
        prev_x = left_border
    else:
        prev_x = right_border

    xi = prev_x * accuracy * 2  # x1 выбирается рядом с x0 самостоятельно
    table.add_row([n, prev_x, f(prev_x), xi, f(xi), cal(prev_x, xi), f(cal(prev_x, xi)), abs(xi - cal(prev_x, xi))])
    while abs(xi - prev_x) > accuracy:
        k = xi
        xi = cal(prev_x, xi)
        prev_x = k
        n += 1
        table.add_row([n, prev_x, f(prev_x), xi, f(xi), cal(prev_x, xi), f(cal(prev_x, xi)), abs(xi - cal(prev_x, xi))])

    return f"Выполнено решение уравнения {equation} методом секущих.\n" \
           f"Х = {xi}\n" \
           f"Количество итераций n = {n}\n" \
           f"Критерий окончания итерационного процесса |a-b| = {abs(xi - prev_x)}\n" \
           f"f({xi}) = {f(xi)}", table
