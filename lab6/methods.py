def euler_method(func, h, a, b, y0):
    x, y = [a], [y0]
    x0 = a + h
    while abs(x0 - b) > 1e-9:
        x.append(x0)
        y.append(y[-1] + h * func(x0, y[-1]))
        x0 += h

    return x, y


def adams_method(func, h, a, b, y0):
    n = int((b - a) / h)
    x, y = [a], [y0]
    for i in range(n):
        x.append(x[i] + h)
        y.append(y[i] + h * func(x[i], y[i]))

    for i in range(3, len(x)):
        k = [func(x[i - q], y[i - q]) for q in range(4)]
        df = k[0] - k[1]
        d2f = k[0] - 2 * k[1] + k[2]
        d3f = k[0] - 3 * k[1] + 3 * k[2] - k[3]
        y[i] = (
            y[i - 1] +
            1 * h ** 1 * k[1] +
            1 * h ** 2 * df / 2 +
            5 * h ** 3 * d2f / 12 +
            3 * h ** 4 * d3f / 8
        )

    return x, y


def runge_rule(yh, y2h, p):
    return abs((yh - y2h) / (2 ** p - 1))
