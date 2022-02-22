import sys
from typing import TextIO

from prettytable import PrettyTable
from termcolor import cprint, colored

from math_helper import equation


def read_parameter(input_stream: TextIO, invite: str, with_invite: bool) -> float:
    while True:
        if with_invite:
            print(invite, end=": ", flush=True)
        try:
            inp = input_stream.readline().strip().replace(",", ".")
            return float(inp)
        except ValueError as e:
            if with_invite:
                cprint("Требуется десятичное число. " + str(e), "yellow")
            else:
                cprint("Неверный формат теста. " + str(e), "red")
                sys.exit(e)


def read_accuracy(input_stream: TextIO, with_invite: bool) -> float:
    while True:
        accuracy = read_parameter(input_stream, "Введите погрешность вычисления", with_invite)
        if accuracy <= 0:
            if with_invite:
                cprint("Значение погрешности вычисления должна быть больше 0", "yellow")
            else:
                cprint("Неверный формат теста. Значение погрешности вычисления не может быть меньше 0.", "red")
                sys.exit(1)
        else:
            return accuracy


def read_data(input_stream: TextIO, is_approximation: bool, with_invite: bool):
    if is_approximation:
        initial_approximation = read_parameter(input_stream, "Введите начальное приближение", with_invite)

        accuracy = read_accuracy(input_stream, with_invite)
        return initial_approximation, accuracy
    else:
        left_border = read_parameter(input_stream, "Введите левую границу интервала", with_invite)
        right_border = read_parameter(input_stream, "Введите правую границу интервала", with_invite)
        if right_border < left_border:
            left_border, right_border = right_border, left_border
            cprint("Правая граница меньше левой. ъъъ ок я поправлю...", "yellow")

        accuracy = read_accuracy(input_stream, with_invite)
        return left_border, right_border, accuracy


def make_table(fields: [str], rows: [[str]]) -> PrettyTable:
    table = PrettyTable(fields)
    table.add_rows(rows)

    table.border = False
    table.float_format = ".5"
    return table


def print_help():
    print("Лабораторная 2. Численное решение нелинейных уравнений и систем.")
    print("\t--help — помощь")
    print("\t--out [file_path] — запись в файл")
    print("\t--in [file_path] — чтение из файла")
    print("Пример входного файла:")
    print("\t1")
    print("\t-0.2136")
    print("\t2.2839")
    print("\t0.001")


def print_hello():
    print(f"Решение уравнения {colored(equation, 'magenta', attrs=['underline'])}. Доступные методы:\n" +
          colored(f"2\tМетод хорд\n"
                  f"5\tМетод простой итерации\n"
                  f"7\tПоебота какая-то", "magenta"))
