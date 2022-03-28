import sys
from typing import TextIO

from termcolor import cprint


def error(msg: str) -> None:
    cprint(msg, "yellow")


def fatal_error(msg: str) -> None:
    cprint(msg, "red")
    exit(msg)


def request_file(invite: str, mode: str) -> TextIO:
    while True:
        try:
            inp = input(invite)
            if inp == "" or inp == "Enter":
                if mode == "w":
                    return sys.stdout
                if mode == "r":
                    return sys.stdin
            return open(inp, mode)
        except FileNotFoundError:
            error("Файл не найден")
        except PermissionError:
            error("Отказано в доступе")
        except OSError:
            error("Ошибка открытия файла")


def parse_input(inp: TextIO) -> list:
    try:
        xs = list(map(float, inp.readline().strip().split()))
        ys = list(map(float, inp.readline().strip().split()))
        return list(zip(xs, ys))
    except ValueError:
        error("На вход ожидаются только числа. Повторите попытку")
        return parse_input(inp)
