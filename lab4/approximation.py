import math

import numpy as np


def msr(ps, ys, n):
    s = 0
    for i in range(n):
        s += (ps[i] - ys[i]) ** 2
    return (s / n) ** 0.5


def confidence(ps, ys, n):
    yp2 = sum((ys[i] - ps[i]) ** 2 for i in range(n))
    p2 = sum(ps[i] ** 2 for i in range(n))

    return 1 - yp2 / (p2 - sum(ps) ** 2 / n)


def correlation(xs: list, ys: list):
    x0, y0 = np.mean(xs), np.mean(ys)
    return np.sum((xs - x0) * (ys - y0)) / (np.sum((xs - x0) ** 2) * np.sum((ys - y0) ** 2)) ** 0.5


def linear(xs: list, ys: list, n: int):
    SX = sum(xs)
    SXX = sum(x ** 2 for x in xs)
    SY = sum(ys)
    SXY = sum(xs[i] * ys[i] for i in range(n))

    a, b = np.linalg.solve(
        np.array([[SXX, SX], [SX, n]]),
        np.array([SXY, SY])
    )

    ps = [a * xs[i] + b for i in range(n)]
    S = sum((ps[i] - ys[i]) ** 2 for i in range(n))

    print(f'Коэффициент корреляции: {correlation(xs, ys):.3f}')

    return msr(ps, ys, n), float(S), confidence(ps, ys, n), lambda x: a * x + b, f'{a:.3f}x + {b:.3f}'


def quadratic(xs: list, ys: list, n: int):
    pf = np.polyfit(xs, ys, 2)
    ps = np.poly1d(pf)(xs)

    S = sum((ps[i] - ys[i]) ** 2 for i in range(n))

    return msr(ps, ys, n), float(S), confidence(ps, ys, n), \
           lambda x: pf[0] * x ** 2 + pf[1] * x + pf[2], \
           f'{pf[0]:.3f}x^2 + {pf[1]:.3f}x + {pf[2]:.3f}'


def cubic(xs: list, ys: list, n: int):
    pf = np.polyfit(xs, ys, 3)
    ps = np.poly1d(pf)(xs)

    S = sum((ps[i] - ys[i]) ** 2 for i in range(n))

    return msr(ps, ys, n), float(S), confidence(ps, ys, n), \
           lambda x: pf[0] * x ** 3 + pf[1] * x ** 2 + pf[2] * x + pf[3], \
           f'{pf[0]:.3f}x^3 + {pf[1]:.3f}x^2 + {pf[2]:.3f}x + {pf[3]:.3f}'


def power(xs: list, ys: list, n: int):
    XS = [math.log(xs[i]) for i in range(n)]
    YS = [math.log(ys[i]) for i in range(n)]
    A, B = np.polyfit(XS, YS, 1)[:]
    a, b = math.exp(A), B
    ps = [a * xs[i] ** b for i in range(n)]

    S = sum((ps[i] - ys[i]) ** 2 for i in range(n))

    return msr(ps, ys, n), float(S), confidence(ps, ys, n), \
           lambda x: a * math.pow(x, b), \
           f'{a:.3f}x^{b:.3f}'


def exponential(xs: list, ys: list, n: int):
    YS = [math.log(ys[i]) for i in range(n)]
    A, B = np.polyfit(xs, YS, 1)[:]
    a, b = math.exp(A), B
    ps = [a * math.exp(b * xs[i]) for i in range(n)]

    S = sum((ps[i] - ys[i]) ** 2 for i in range(n))

    return msr(ps, ys, n), float(S), confidence(ps, ys, n), \
           lambda x: a * math.exp(b * x), \
           f'{a:.3f}e^{b:.3f}x'


def logarithmic(xs: list, ys: list, n: int):
    XS = [math.log(xs[i]) for i in range(n)]
    A, B = np.polyfit(XS, ys, 1)[:]
    a, b = A, B

    ps = [a * math.log(xs[i]) + b for i in range(n)]

    S = sum((ps[i] - ys[i]) ** 2 for i in range(n))

    return msr(ps, ys, n), float(S), confidence(ps, ys, n), \
           lambda x: a * math.log(x) + b, \
           f'{a:.3f}ln(x) + {b:.3f}'
