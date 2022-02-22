import sys
from typing import TextIO

from termcolor import cprint

from chord_method import chord_method
from io_helper import print_hello, read_data
from secant_method import secant_method
from simple_iteration_method import simple_iteration_method


class Method:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def solve(self):
        report, table = self.method(*self.args)
        return report, str(table)


def get_method(input_stream: TextIO, with_invite: bool):
    if with_invite:
        print_hello()
    while True:
        if with_invite:
            print("Введите номер метода", end=": ", flush=True)
        try:
            method_number = int(input_stream.readline().strip())
            if method_number == 2:
                return Method(chord_method, read_data(input_stream, False, with_invite))
            elif method_number == 5:
                return Method(simple_iteration_method, read_data(input_stream, True, with_invite))
            elif method_number == 7:
                return Method(secant_method, read_data(input_stream, False, with_invite))
            else:
                if with_invite:
                    cprint("Такого метода еще не придумали, братишка. Целое число от 1 до 3...", "yellow")
                else:
                    cprint("Неверный формат теста. Номер метода — Целое число от 1 до 3.", "red")
                    sys.exit(1)
        except ValueError as e:
            if with_invite:
                cprint("Целое число от 1 до 3... " + str(e), "yellow")
            else:
                cprint("Неверный формат теста. Требуется номер метода. " + str(e), "red")
                sys.exit(1)
