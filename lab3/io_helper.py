from termcolor import cprint


def error(msg: str) -> None:
    cprint(msg, "yellow")


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


def choose_from_dict(d: dict, invite: str) -> str:
    keys = list(d)
    cprint("\n".join(list(f"{i + 1}\t{k}" for i, k in enumerate(keys))), "magenta")
    while True:
        i = read_int(invite) - 1
        if i < 0 or i >= len(keys):
            error(f"Введите число на промежутке [{1}, {len(keys)}].")
        else:
            return keys[i]


def read_parameters() -> (float, float, int):
    left_limit = read_float("Введите левый предел")
    right_limit = read_float("Введите правый предел")
    if right_limit < left_limit:
        left_limit, right_limit = right_limit, left_limit
        error("Правый предел меньше левого. Ок я поправлю...")
    n = read_int("Введите число разбиений")
    return left_limit, right_limit, n
