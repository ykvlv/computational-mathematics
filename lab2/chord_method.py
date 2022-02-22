from io_helper import make_table
from math_helper import f, dd, equation


def chord_method(a: float, b: float, accuracy: float, max_iteration: int = 100) -> (str, [[]]):
    """ Метод хорд """
    fields = ['n', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|x - x0|']
    rows = []

    # Выбор начального приближения
    # TODO тут меньше нуля...
    if f(a) * dd(f, a) < 0:
        x = a
        fix_x = b
    elif f(b) * dd(f, b) < 0:
        x = b
        fix_x = a
    else:
        x = a - (b - a) / (f(b) - f(a)) * f(a)
        fix_x = None

    n = 0
    x0 = x + 2 * accuracy
    rows.append([n, a, b, x, f(a), f(b), f(x), abs(x - x0)])

    # TODO а правильно ли работает
    while abs(x - x0) > accuracy and n < max_iteration:
        n += 1
        if fix_x is None:
            if f(a) * f(x) < 0:
                b = x
            else:
                a = x
            x0, x = x, a - (b - a) / (f(b) - f(a)) * f(a)

            rows.append([n, a, b, x, f(a), f(b), f(x), abs(x - x0)])
        else:
            x0, x = x, x - (fix_x - x) / (f(fix_x) - f(x)) * f(x)
            if fix_x == a:
                rows.append([n, fix_x, x, x, f(fix_x), f(x), f(x), abs(x - x0)])
            else:
                rows.append([n, x, fix_x, x, f(x), f(fix_x), f(x), abs(x - x0)])

    return f"Выполнено решение уравнения {equation} методом хорд.\n" \
           f"Х = {x}\n" \
           f"Количество итераций n = {n}\n" \
           f"Критерий окончания итерационного процесса |a-b| = {abs(x - x0)}\n" \
           f"f({x}) = {f(x)}", make_table(fields, rows)
