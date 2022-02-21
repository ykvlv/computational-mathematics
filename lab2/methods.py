import sys
from typing import TextIO

from termcolor import cprint

from iohandler import read_data, equation


def calculate_function(x):
    return x ** 3 - 2.92 * x ** 2 + 1.435 * x + 0.791


class Method:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def solve(self):
        return self.method(*self.args)


def chord_method(left_border: float, right_border: float, accuracy: float):
    pass


def secant_method(left_border: float, right_border: float, accuracy: float):
    n = 0
    # условие применимости метода Ньютона
    if calculate_function(left_border) * calculate_function(right_border) > 0:
        cprint(f"На концах отрезка [{left_border}, {right_border}] функция имеет одинаковые знаки.\n"
               f"На отрезке либо нет корней, либо их четное количество. Пожалуйста, уточните интервал")
        sys.exit(1)

    # выбор x0
    if calculate_function(left_border) * 6 * left_border - 6.25 > 0:
        x0 = left_border
    else:
        x0 = right_border

    # x1 выбирается рядом с x0 самостоятельно
    x = x0 * accuracy * 2
    while abs(x - x0) > accuracy:
        k = x
        x -= (x - x0) * calculate_function(x) / (calculate_function(x) - calculate_function(x0))
        x0 = k
        n += 1

    return f"Выполнено решение уравнения {equation} методом секущих.\n" \
           f"Х = {x}\n" \
           f"Количество итераций n = {n}\n" \
           f"Критерий окончания итерационного процесса |a-b|={abs(x-x0)}\n" \
           f"f({x}) = {calculate_function(x)}"


def simple_iteration_method(initial_approximation: float, accuracy: float):
    pass


def get_method(source: TextIO, is_cli: bool):
    method_number = source.readline().strip()

    if method_number == "1":
        return Method(chord_method, read_data(source, False, is_cli))
    elif method_number == "2":
        return Method(secant_method, read_data(source, False, is_cli))
    elif method_number == "3":
        return Method(simple_iteration_method, read_data(source, True, is_cli))
    else:
        cprint("Вы не выбрали метод...", "red")
        sys.exit(1)
