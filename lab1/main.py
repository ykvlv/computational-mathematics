import sys

from io_handler import *


def get_triangle(matrix, coefficients):
    n = len(coefficients)
    for diagonal_or_row_hz in range(0, n - 1):
        for chosen_column_ili_row_hz in range(diagonal_or_row_hz + 1, n):
            cef_k = -matrix[chosen_column_ili_row_hz][diagonal_or_row_hz] / matrix[diagonal_or_row_hz][diagonal_or_row_hz]
            print(cef_k)
            for replaced_I_DONT_KNOW in range(0, n):
                # tut error
                matrix[chosen_column_ili_row_hz][diagonal_or_row_hz] += matrix[diagonal_or_row_hz][diagonal_or_row_hz] * cef_k
        print_matrix(matrix)


def solve_gaussian(matrix, coefficients):
    print_hello()

    check_matrix()

    triangle = get_triangle(matrix, coefficients)

    print_triangle(triangle, coefficients)




if __name__ == '__main__':

    if len(sys.argv) < 2:
        matrix, coefficients = read_from_cli()
        solve_gaussian(matrix, coefficients)
    elif sys.argv[1] == "file":
        matrix, coefficients = read_from_file(sys.argv[2])
        solve_gaussian(matrix, coefficients)
    else:
        print_help()