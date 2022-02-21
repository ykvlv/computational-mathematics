import sys
from typing import TextIO
from termcolor import cprint

equation = "x^3 - 2,92x^2 + 1,435x + 0,791"


def read_parameter(source: TextIO, invite: str, is_cli: bool):
    while True:
        if is_cli:
            print(invite, end=": ", flush=True)
        try:
            inp = source.readline().strip().replace(",", ".")
            return float(inp)
        except ValueError:
            if is_cli:
                cprint("Требуется десятичное число", "yellow")
            else:
                cprint("Неверный формат теста. Требуется десятичное число.", "red")
                sys.exit(1)


def read_accuracy(source: TextIO, is_cli: bool):
    while True:
        accuracy = read_parameter(source, "Введите погрешность вычисления", is_cli)
        if accuracy < 0:
            if is_cli:
                cprint("Значение погрешности вычисления не может быть меньше 0", "yellow")
            else:
                cprint("Неверный формат теста. Значение погрешности вычисления не может быть меньше 0.", "red")
                sys.exit(1)
        else:
            return accuracy


def read_data(source: TextIO, is_approximation: bool, is_cli: bool):
    if is_approximation:
        initial_approximation = read_parameter(source, "Введите начальное приближение", is_cli)

        accuracy = read_accuracy(source, is_cli)
        return initial_approximation, accuracy
    else:
        left_border = read_parameter(source, "Введите левую границу интервала", is_cli)
        right_border = read_parameter(source, "Введите правую границу интервала", is_cli)
        if right_border < left_border:
            left_border, right_border = right_border, left_border
            cprint("Правая граница меньше левой. ъъъ ок я поправлю...", "yellow")

        accuracy = read_accuracy(source, is_cli)
        return left_border, right_border, accuracy


def print_help():
    print("Только один параметр — file. Пример входного файла:")
    print("1")
    print("-0.2136")
    print("2.2839")
    print("0.001")


def print_hello():
    print(f"Решение уравнения {equation}")
    print("Для выбора метода хорд введите 1")
    print("метода секущих — 2")
    print("метода простой итерации — 3")
