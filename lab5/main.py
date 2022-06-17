import numpy as np
import matplotlib.pyplot as plt
from math import sin, sqrt

from interpolation import lagrange, gauss


FUNCTIONS = [
    [
        '2 * x**2 - 8 * x + 1',
        lambda x: 2 * x**2 - 8 * x + 1
    ],
    [
        'sqrt(x) / 2',
        lambda x: sqrt(x) / 2
    ],
    [
        'sin(x)',
        lambda x: sin(x)
    ],
]


def read_table():
    dots = []

    print('Введите координаты через пробел. Enter — конец ввода.')
    while (line := input()) != '':
        dots.append(tuple(map(float, line.split())))

    return dots


def read_func():
    print('Выберите функцию.')
    for i, fun in enumerate(FUNCTIONS, 1):
        print(f'{i}. {fun[0]!s}')
    func_id = int(input('Номер функции: '))
    func = FUNCTIONS[int(func_id) - 1]

    a, b = map(float, input('Границы отрезка через пробел: ').split())
    a, b = min(a, b), max(a, b)

    n = int(input('Количество узлов интерполяции: '))

    return space(func, a, b, n)


def plot(x, y, plot_x, plot_y, x0, answer):
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker='>', ms=5, color='k', transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker='^', ms=5, color='k', transform=ax.get_xaxis_transform(), clip_on=False)

    plt.plot(x, y, 'o', plot_x, plot_y, 'b')
    plt.plot([x0], [answer], 'o', markeredgecolor='red', markerfacecolor='red')
    plt.show()


def space(f, a, b, n):
    dots = []
    h = (b - a) / (n - 1)
    for i in range(n):
        dots.append((a, f[1](a)))
        a += h
    return dots


def get_input():
    print('Выберите метод интерполяции.')
    print('1. Многочлен Лагранжа')
    print('2. Многочлен Гаусса')
    method = int(input('Метод решения: ').strip())

    print('Выберите способ ввода исходных данных.')
    print('1. Набор точек')
    print('2. Функция')
    input_method = int(input('Способ: '))

    dots = (read_table, read_func)[input_method - 1]()
    x = float(input('Значение аргумента для интерполирования: '))

    return method, dots, x


def main():
    method, dots, x0 = get_input()
    x = np.array([dot[0] for dot in dots])
    y = np.array([dot[1] for dot in dots])
    plot_x = np.linspace(np.min(x), np.max(x), 100)

    res = (
        (lambda: lagrange(dots, x0),
         lambda: [lagrange(dots, x_) for x_ in plot_x]),
        (lambda: gauss(dots, x0),
         lambda: [lagrange(dots, x_) for x_ in plot_x]),
    )[method - 1]
    answer, plot_y = map(lambda f: f(), res)

    plot(x, y, plot_x, plot_y, x0, answer)

    print(f'Приближенное значение функции: {answer}')


if __name__ == "__main__":
    main()
