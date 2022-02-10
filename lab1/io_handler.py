def read_from_cli():
    n = int(input())
    matrix = [[float(i) for i in input().split()] for _ in range(n)]
    coefficients = list(map(float, input().split()))

    return matrix, coefficients


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            n = int(file.readline())
            matrix = [[float(i) for i in file.readline().split()] for _ in range(n)]
            coefficients = list(map(float, file.readline().split()))

            return matrix, coefficients
    except OSError:
        print("Файл не был прочитан, гудбай")
        exit(1)


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def check_matrix():
    pass

def print_help():
    print("only one param: --file")


def print_hello():
    pass


def print_triangle(matrix, coefficients):
    pass
