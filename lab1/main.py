import sys

from io_handler import *


def get_minor(a, line_num, k):
    m = []

    for i in range(len(a)):
        if i != line_num:
            line = []
            for j in range(len(a)):
                if j != k:
                    line.append(a[i][j])
            m.append(line)
    return m


def get_determinant(a):
    if len(a) == 1:
        return a[0][0]

    det = 0
    sign = 1
    for i in range(len(a)):
        det += sign * a[0][i] * get_determinant(get_minor(a, 0, i))
        sign *= -1
    return det


def permute_equation(target, a, b):
    for line in range(target + 1, len(a)):
        if a[line][target] != 0:
            a[line], a[target] = a[target], a[line]
            b[line], b[target] = b[target], b[line]
            return
    its_error()


def make_triangle(a, b):
    n = len(a)
    for i in range(0, n - 1):

        if a[i][i] == 0:
            permute_equation(i, a, b)

        for k in range(i + 1, n):
            c = a[k][i] / a[i][i]

            for j in range(i, n):
                a[k][j] -= c * a[i][j]
            a[k][i] = 0

            b[k] -= c * b[i]


def calc_answer_by_reverse(a, b):
    n = len(a)
    x = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        s = 0
        if a[i][i] == 0:
            its_error()

        for j in range(i + 1, n):
            s += a[i][j] * x[j]

        x[i] = (b[i] - s) / a[i][i]

    return x


def calc_residual(original_matrix, original_coefficient, answer):
    mine_coefficient = [0 for _ in range(len(original_coefficient))]

    for i in range(len(original_matrix)):
        left_side = 0
        for j in range(len(original_matrix)):
            left_side += original_matrix[i][j] * answer[j]
        mine_coefficient[i] = left_side

    residual = [0 for _ in range(len(original_coefficient))]
    for i in range(len(original_matrix)):
        residual[i] = original_coefficient[i] - mine_coefficient[i]
    return residual


def solve_gaussian(a, b):
    print_hello(a, b)

    coefficients_copy = [i for i in b]
    matrix_copy = [[j for j in i] for i in a]

    print(coefficients_copy)
    make_triangle(a, b)

    print_triangle(a, b)

    answer = calc_answer_by_reverse(a, b)

    print_answer(answer)
    residual = calc_residual(matrix_copy, coefficients_copy, answer)

    print_residual(residual)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        matrix, coefficients = read_from_cli()
        solve_gaussian(matrix, coefficients)
    elif sys.argv[1] == "file":
        matrix, coefficients = read_from_file(sys.argv[2])
        solve_gaussian(matrix, coefficients)
    else:
        print_help()
