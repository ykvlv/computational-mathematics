from iohandler import *


import sys

class Method:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def solve(self):
        self.method(*self.args)


def chord_method(left_border, right_border, accuracy):
    pass


def secant_method(left_border, right_border, accuracy):
    pass


def simple_iteration_method(initial_approximation, accuracy):
    pass


def get_method(inp: ):
    method_number = inp.readline().strip()


    if method_number == "1":
        return Method(chord_method, read_from_cli(False))
    elif method_number == "2":
        return Method(secant_method, read_from_cli(False))
    elif method_number == "3":
        return Method(simple_iteration_method, read_from_cli(True))
    else:
        print("Вы не выбрали метод...")
        exit(1)
