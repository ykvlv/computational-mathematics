equation = "x^3 - 2,92x^2 + 1,435x + 0,791"


def get_parameter(invite):
    print(invite, end=": ")
    while True:
        try:
            inp = input().strip().replace(",", ".")
            return float(inp)
        except ValueError:
            print("Требуется десятичное число", end=": ")


def read_from_cli(is_initial_approximation):
    if is_initial_approximation:
        initial_approximation = get_parameter("Введите начальное приближение")
        accuracy = get_parameter("Введите погрешность вычисления")
        if accuracy < 0:
            print("Значение погрешности вычисления не может быть меньше 0")
            exit(1)
        return initial_approximation, accuracy
    else:
        left_border = get_parameter("Введите левую границу интервала")
        right_border = get_parameter("Введите правую границу интервала")
        if right_border < left_border:
            left_border, right_border = right_border, left_border
            print("Правая граница меньше левой. ъъъ ок я поправлю...")
        accuracy = get_parameter("Введите погрешность вычисления")
        if accuracy < 0:
            print("Значение погрешности вычисления не может быть меньше 0")
            exit(1)
        return left_border, right_border, accuracy


def read_from_file(file_path):
    pass


def print_help():
    pass


def print_hello():
    print(f"Решение уравнения {equation}")
    print("Для выбора метода хорд введите 1")
    print("метода секущих — 2")
    print("метода простой итерации — 3")
