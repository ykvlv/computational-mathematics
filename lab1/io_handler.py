from prettytable import PrettyTable


def read_from_cli():
    print("Введите матрицу в формате:")
    print("В первой строке целое число n (1 <= n <= 20) — размерность матрицы.")
    print("Далее следует n строк, в каждой n чисел — элемены матрицы.")
    print("Последняя строка — коэффициенты матрицы.")

    n = int(input())
    matrix = [[float(i) for i in input().split()] for _ in range(n)]
    coefficients = list(map(float, input().split()))

    return matrix, coefficients


def read_from_file(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline())
        matrix = [[float(i) for i in file.readline().split()] for _ in range(n)]
        coefficients = list(map(float, file.readline().split()))

        return matrix, coefficients


def print_matrix(matrix, coefficients):
    table = PrettyTable(["x" + str(i) for i in range(len(matrix))])
    table.add_rows(matrix)
    table.add_column("c", coefficients)

    table.border = False
    # table.float_format = ".3"
    print(table)


def print_array(answer):
    table = PrettyTable(["x" + str(i) for i in range(len(answer))])
    table.add_row(answer)

    table.border = False
    # table.float_format = ".3"
    print(table)
    print()


def print_answer(answer):
    print("Корни получились:")
    print_array(answer)


def print_residual(residual):
    print("Невязки получились:")
    print_array(residual)


def print_help():
    print("only one param: file")


def its_error():
    print("Ну короче решений нет. Нолик мешает")
    exit(1)


def print_hello(matrix, coefficients):
    print("Ваша матрица:")
    print_matrix(matrix, coefficients)
    print()


def print_triangle(matrix, coefficients):
    print("Треугольная матрица получилась такая:")
    print_matrix(matrix, coefficients)
    print()
