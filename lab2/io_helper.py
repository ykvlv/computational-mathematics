import sys
from typing import TextIO, Callable
from math import sin, exp

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from termcolor import cprint

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


def choose_from_list(input_stream: TextIO, lst: list, invite: str, with_invite: bool) -> int:
    if with_invite:
        cprint("\n".join(list(f"{i + 1}\t{f[0]}" for i, f in enumerate(lst))), "magenta")
    while True:
        if with_invite:
            print(invite, end=": ", flush=True)
        try:
            number = int(input_stream.readline().strip())
            if number < 1 or number > len(lst):
                if with_invite:
                    error(f"Введите число на промежутке [{1}, {len(lst)}].")
                else:
                    fatal_error("Неверный формат теста. Нельзя выбрать число из промежутка.")
            else:
                return number - 1
        except ValueError as e:
            if with_invite:
                error("Требуется целое число. " + str(e))
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


def read_data(input_stream: TextIO, is_approximation: bool, with_invite: bool) -> tuple:
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


def make_report(f: Callable[[float], float], iterations: int, root: float, iter_end: float) -> str:
    return f"Выполнено решение уравнения {equation}.\n" \
           f"Х = {root}\n" \
           f"Количество итераций i = {iterations}\n" \
           f"Критерий окончания итерационного процесса = {iter_end}\n" \
           f"f({root}) = {f(root)}"


def make_table(fields: [str], rows: [[str]]) -> PrettyTable:
    table = PrettyTable(fields)
    table.add_rows(rows)

    table.border = False
    table.float_format = ".5"
    return table


def show_graph(f: Callable[[float], float], root: float) -> None:
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


def show_graph_2(func1, func2):
    f = [func1, func2]
    bx = 2.5
    x1 = np.linspace(-bx, bx, 100)
    x2 = np.linspace(-bx, bx, 100)
    f1 = np.zeros((x1.size, x2.size))
    f2 = np.zeros((x1.size, x2.size))

    for kf, g in enumerate((f1, f2)):
        for i, deta in enumerate(x2):
            for j, beta in enumerate(x1):
                g[j, i] = f[kf](beta, deta)

    X, Y = np.meshgrid(x1, x2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, f1)
    ax.plot_surface(X, Y, f2)
    plt.show()


def print_help() -> None:
    print("Лабораторная 2. Численное решение нелинейных уравнений и систем.")
    print("\t--help — помощь")
    print("\t--out [file_path] — запись в файл")
    print("\t--in [file_path] — чтение из файла")
    print("Пример входного файла:")
    print("\t2")
    print("\t-0.2136")
    print("\t2.2839")
    print("\t0.001")


functions = [
    [
        'f(x, y) = x + 0.1 * x^2 + x + 0.2 * y^2 - 0.3',
        lambda x, y: 0.3 - 0.1 * x ** 2 - 0.2 * y ** 2,
        lambda x, y: 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3
    ],
    [
        'f(x, y) = x - sin(2 * y^2 + 3)',
        lambda x, y: sin(2 * y ** 2 + 3),
        lambda x, y: x - sin(2 * y ** 2 + 3),
    ],
    [
        'f(x, y) = 0.2 * x^2 + y + 0.1 * x * x2 - 0.7',
        lambda x, y: 0.7 - 0.2 * x ** 2 - 0.1 * x * y,
        lambda x, y: 0.2 * x ** 2 + y + 0.1 * x * y - 0.7
    ],
    [
        'f(x, y) = exp(x^3 - 8 * x^2) + 4 * y',
        lambda x, y: -exp(x ** 3 - 8 * x ** 2) / 4,
        lambda x, y: exp(x ** 3 - 8 * x ** 2) + 4 * y
    ]
]


def read_system(input_stream: TextIO, with_invite: bool) -> tuple:
    func1 = functions[choose_from_list(input_stream, functions, "Выберите 1ю функцию", with_invite)]
    func2 = functions[choose_from_list(input_stream, functions, "Выберите 2ую функцию", with_invite)]
    if func1 == func2:
        error("Функции должны быть различными")
        return read_system(input_stream, with_invite)
    a1 = read_parameter(input_stream, "Начальное приближение x", with_invite)
    a2 = read_parameter(input_stream, "Начальное приближение y", with_invite)

    accuracy = read_accuracy(input_stream, with_invite)

    return func1, a1, func2, a2, accuracy
