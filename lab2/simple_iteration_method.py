# TODO исправить значения
import sys

from prettytable import PrettyTable
from termcolor import cprint

from iohandler import equation


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

        return f"Выполнено решение уравнения {equation} методом простых итераций.\n" \
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
