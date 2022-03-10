import sys
from typing import TextIO, Callable

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from termcolor import cprint, colored

equation = "x³ - 2.92x² + 1.435x + 0.791"


def error(msg: str):
    cprint(msg, "yellow")


def fatal_error(msg: str):
    cprint(msg, "red")
    sys.exit(1)


def read_parameter(input_stream: TextIO, invite: str, with_invite: bool) -> float:
    while True:
        if with_invite:
            print(invite, end=": ", flush=True)
        try:
            inp = input_stream.readline().strip().replace(",", ".")
            return float(inp)
        except ValueError as e:
            if with_invite:
                error("Требуется десятичное число. " + str(e))
            else:
                fatal_error("Неверный формат теста. " + str(e))


def read_accuracy(input_stream: TextIO, with_invite: bool) -> float:
    while True:
        accuracy = read_parameter(input_stream, "Введите погрешность вычисления", with_invite)
        if accuracy <= 0:
            if with_invite:
                error("Значение погрешности вычисления должна быть больше 0")
            else:
                fatal_error("Неверный формат теста. Значение погрешности вычисления не может быть меньше 0.")
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
            error("Правая граница меньше левой. ъъъ ок я поправлю...")

        accuracy = read_accuracy(input_stream, with_invite)
        return left_border, right_border, accuracy


def make_report(f: Callable[[float], float], iterations: int, root: float, iter_end: float):
    return f"Выполнено решение уравнения {equation}.\n" \
           f"Х = {root}\n" \
           f"Количество итераций i = {iterations}\n" \
           f"Критерий окончания итерационного процесса = {iter_end}\n" \
           f"f({root}) = {f(root)}"


def make_table(fields: [str], rows: [[str]]) -> PrettyTable:
    table = PrettyTable(fields)
    table.add_rows(rows)

    table.border = False
    table.float_format = ".3"
    return table


def show_graph(f, root):
    # Интервал изменения переменной по оси X
    x_min = -0.6
    x_max = 2.5

    # Количество отсчетов на заданном интервале
    count = 200

    # Создадим список координат по оси X на отрезке [x_min; x_max]
    x_list = np.linspace(x_min, x_max, count)

    # Вычислим значение функции в заданных точках
    y_list = [f(x) for x in x_list]

    # Нарисуем одномерный график
    plt.plot(x_list, y_list)

    # Нарисуем оси
    ax = plt.gca()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    # Добавим корень
    ax.plot(root, 0, 'o')

    # Покажем окно с нарисованным графиком
    plt.show()


def print_help():
    print("Лабораторная 2. Численное решение нелинейных уравнений и систем.")
    print("\t--help — помощь")
    print("\t--out [file_path] — запись в файл")
    print("\t--in [file_path] — чтение из файла")
    print("Пример входного файла:")
    print("\t2")
    print("\t-0.2136")
    print("\t2.2839")
    print("\t0.001")


def print_hello():
    print(f"Решение уравнения {colored(equation, 'magenta', attrs=['underline'])}. Доступные методы:\n" +
          colored(f"2\tМетод хорд\n"
                  f"4\tМетод секущих\n"
                  f"5\tМетод простой итерации", "magenta"))
