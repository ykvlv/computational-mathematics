import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from math import cos, sin, e

from methods import euler_method, adams_method, runge_rule
from util import Equation, format_float as ff

EQUATIONS = [
    Equation(
        dif=[
            'y + (1 + x) * y ** 2',
            lambda x, y: y + (1 + x) * y ** 2
        ],
        ex=[
            '-1 / x',
            lambda x: -1 / x
        ],
        a=1,
        b=1.5,
        y0=-1
    ),
    Equation(
        dif=[
            'cos(x) - y',
            lambda x, y: cos(x) - y
        ],
        ex=[
            '(cos(x) + sin(x)) / 2',
            lambda x: (cos(x) + sin(x)) / 2
        ],
        a=0,
        b=5,
        y0=0.5
    )
]

METHODS = [
    ('Метод Эйлера', euler_method, 2),
    ('Метод Адамса', adams_method, 4)
]


def main():
    for i, eq in enumerate(EQUATIONS, 1):
        print(f"{i}.\ty' = {eq.dif[0]!s}\n"
              f"\tx[{eq.a}; {eq.b}], y({eq.a}) = {eq.y0}")
    eq = EQUATIONS[int(input('Выберите дифференциальное уравнение: ')) - 1]

    for i, method in enumerate(METHODS):
        print(f"{i+1}. {method[0]}")
    method = METHODS[int(input('Выберите метод решения: ')) - 1]
    fun, p = method[1], method[2]

    h = float(input('Выберите шаг (h): '))

    x, y = fun(eq.dif[1], h, eq.a, eq.b, eq.y0)
    f_dif = [eq.dif[1](xi, yi) for xi, yi in zip(x, y)]
    f_ex = [eq.ex[1](xi) for xi in x]
    eps = [abs(yi - ex) for yi, ex in zip(y, f_ex)]

    table = PrettyTable(['i', 'x', 'y', 'f(x, y)', 'Точное решение', 'eps'])
    table.border = False
    for i in range(len(x)):
        table.add_row((i, ff(x[i]), ff(y[i]), ff(f_dif[i]), ff(f_ex[i]), ff(eps[i])))
    print(table)
    runge = runge_rule(y[-1], fun(eq.dif[1], 2 * h, eq.a, eq.b, eq.y0)[1][-1], p)

    print('Погрешность:', max(eps))
    print('По Рунге:', runge)

    x_ex = np.linspace(eq.a, eq.b)
    y_ex = np.vectorize(eq.ex[1])(x_ex)

    plt.title(f"y' = {eq.dif[0]}")
    plt.plot(x_ex, y_ex, 'blue', label=f"y = {eq.ex[0]}")
    plt.plot(x, y, 'ro', label=method[0])
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
