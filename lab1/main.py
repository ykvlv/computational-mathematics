import sys

from io_handler import *


def permute_equation(target, a, b):
    for line in range(target + 1, len(a)):
        if a[line][target] != 0:
            a[line], a[target] = a[target], a[line]
            b[line], b[target] = b[target], b[line]
            return
    print("Ну короче матрица не решается нолик мешает")
    exit(1)


def make_triangle(a, b):
    n = len(a)
    for i in range(0, n - 1):

        if a[i][i] == 0:
            permute_equation(i, a, b)

        for k in range(i + 1, n):
            c = a[k][i] / a[i][i]
            # a[k][i] = 0

            for j in range(i, n):
                a[k][j] -= c * a[i][j]

            b[k] -= c * b[i]


def get_answer_by_reverse(a, b):
    n = len(a)
    x = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        s = 0
        if a[i][i] == 0:
            print("Ну короче матрица не решается нолик мешает")
            exit(1)

        for j in range(i + 1, n):
            s += a[i][j] * x[j]

        x[i] = (b[i] - s) / a[i][i]

    return x


def solve_gaussian(a, b):
    print_hello(matrix, coefficients)

    make_triangle(a, b)

    print_triangle(a, b)

    answer = get_answer_by_reverse(a, b)

    print_answer(answer)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        matrix, coefficients = read_from_cli()
        solve_gaussian(matrix, coefficients)
    elif sys.argv[1] == "file":
        matrix, coefficients = read_from_file(sys.argv[2])
        solve_gaussian(matrix, coefficients)
    else:
        print_help()
