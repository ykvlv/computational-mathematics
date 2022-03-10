from typing import TextIO

from prettytable import PrettyTable

from methods import chord_method, secant_method, simple_iteration_method, system_simple_iteration_method
from io_helper import read_data, fatal_error, read_system, choose_from_list


def f(x: float) -> float:
    """ Используемая функция """
    return x ** 3 - 2.92 * x ** 2 + 1.435 * x + 0.791


class Method:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def solve(self) -> tuple[str, PrettyTable]:
        report, table = self.method(f, *self.args)
        return report, table


methods = [
    [
        "Метод хорд",
        chord_method
    ], [
        "Метод секущих",
        secant_method
    ], [
        "Метод простой итерации",
        simple_iteration_method
    ], [
        "Система методом простой итерации",
        system_simple_iteration_method
    ]
]


def get_method(input_stream: TextIO, with_invite: bool) -> Method:
    method_number = choose_from_list(input_stream, methods, "Выберите метод", with_invite)
    if method_number == 0:
        return Method(chord_method, read_data(input_stream, False, with_invite))
    elif method_number == 1:
        return Method(secant_method, read_data(input_stream, False, with_invite))
    elif method_number == 2:
        return Method(simple_iteration_method, read_data(input_stream, True, with_invite))
    elif method_number == 3:
        return Method(system_simple_iteration_method, read_system(input_stream, with_invite))
    else:
        fatal_error("Такого метода не существует.")
