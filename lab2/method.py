from typing import TextIO, Callable

from prettytable import PrettyTable

from methods import chord_method, secant_method, simple_iteration_method
from io_helper import print_hello, read_data, error, fatal_error


def f(x: float) -> float:
    """ Используемая функция """
    return x**3 - 2.92 * x**2 + 1.435 * x + 0.791


class Method:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def solve(self) -> tuple[str, PrettyTable]:
        report, table = self.method(f, *self.args)
        return report, table


def get_method(input_stream: TextIO, with_invite: bool) -> Method:
    if with_invite:
        print_hello()
    while True:
        if with_invite:
            print("Введите номер метода", end=": ", flush=True)

        method_number = input_stream.readline().strip()
        if method_number == "2":
            return Method(chord_method, read_data(input_stream, False, with_invite))
        elif method_number == "4":
            return Method(secant_method, read_data(input_stream, False, with_invite))
        elif method_number == "5":
            return Method(simple_iteration_method, read_data(input_stream, True, with_invite))
        else:
            if with_invite:
                error("Такого метода еще не придумали, братишка. Только 2, 4, 5.")
            else:
                fatal_error("Неверный формат теста. Возможные номера методов — 2, 4, 5.")
