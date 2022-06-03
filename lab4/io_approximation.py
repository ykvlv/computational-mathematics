import sys
from typing import TextIO

import numpy as np
from matplotlib import pyplot as plt
from termcolor import cprint


def error(msg: str) -> None:
    cprint(msg, "yellow")


def fatal_error(msg: str) -> None:
    cprint(msg, "red")
    exit(1)


def request_file(invite: str, mode: str) -> TextIO:
    while True:
        try:
            inp = input(invite)
            if inp == "" or inp == "Enter":
                if mode == "w":
                    return sys.stdout
                elif mode == "r":
                    return sys.stdin
                else:
                    fatal_error("Использование в режиме \"" + mode + "\" не предусмотрено")
            return open(inp, mode)
        except FileNotFoundError:
            error("Файл не найден")
        except PermissionError:
            error("Отказано в доступе")
        except OSError:
            error("Ошибка открытия файла")


def parse_input(inp: TextIO) -> (list, list, int):
    try:
        xs = list(map(float, inp.readline().strip().split()))
        ys = list(map(float, inp.readline().strip().split()))
        return xs, ys, len(xs)
    except ValueError:
        error("На вход ожидаются только числа. Повторите попытку")
        return parse_input(inp)


OFFSET = 5


def show_graph(xs: list, ys: list, approximations: list) -> None:
    x1, x2, y1, y2 = min(xs), max(xs), min(ys), max(ys)
    bx, by = max(abs(x1), abs(x2)) + OFFSET, max(abs(y1), abs(y2)) + OFFSET
    x = np.linspace(min(xs) - OFFSET, max(xs) + OFFSET, 100)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    plt.grid(True)
    plt.xlim((-bx, bx))
    plt.ylim((-by, by))

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    for approximation in approximations:
        xt = x
        y = np.vectorize(approximation[3])
        try:
            y(x)
        except ValueError:
            xt = x[x > 0]
        finally:
            ax.plot(xt, y(xt), label=approximation[4])

    ax.plot(xs, ys, 'ro')
    plt.legend()

    plt.show()
