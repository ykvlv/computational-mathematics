import sys
from typing import TextIO

from termcolor import cprint

from iohandler import read_data


class Method:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def solve(self):
        self.method(*self.args)


def chord_method(left_border: float, right_border: float, accuracy: float):
    pass


def secant_method(left_border: float, right_border: float, accuracy: float):
    pass


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
