from sys import exit

from termcolor import cprint


def error(msg: str) -> None:
    cprint(msg, "yellow")


def fatal_error(msg: str) -> None:
    cprint(msg, "red")
    exit(1)


def read_int(invite: str) -> int:
    while True:
        print(invite, end=": ")
        try:
            return int(input().strip())
        except ValueError:
            error("Требуется целое число.")


def read_float(invite: str) -> float:
    while True:
        print(invite, end=": ")
        try:
            return float(input().strip().replace(",", "."))
        except ValueError:
            error("Требуется десятичное число.")


def read_accuracy(invite: str) -> float:
    while True:
        accuracy = read_float(invite)
        if accuracy <= 0 or accuracy >= 1:
            fatal_error("Значение погрешности вычисления должно находиться в промежутке (0, 1)")
        else:
            return accuracy


def choose_from_dict(d: dict, invite: str) -> str:
    keys = list(d)
    cprint("\n".join(list(f"{i + 1}\t{k}" for i, k in enumerate(keys))), "magenta")
    while True:
        i = read_int(invite) - 1
        if i < 0 or i >= len(keys):
            error(f"Введите число на промежутке [{1}, {len(keys)}].")
        else:
            return keys[i]


def read_parameters() -> (float, float, float, int):
    left_limit = read_float("Введите левый предел")
    right_limit = read_float("Введите правый предел")
    if right_limit < left_limit:
        left_limit, right_limit = right_limit, left_limit
        error("Правый предел меньше левого. Ок я поправлю...")
    n = read_int("Введите число разбиений")
    accuracy = read_accuracy("Введите погрешность вычисления")
    return left_limit, right_limit, n, accuracy
