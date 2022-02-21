import sys
from typing import TextIO

from termcolor import cprint

from chord_method import chord_method
from iohandler import read_data
from secant_method import secant_method
from simple_iteration_method import simple_iteration_method


class Method:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def solve(self):
        report, table = self.method(*self.args)
        return report, table


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
