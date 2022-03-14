from io_helper import choose_from_dict, read_parameters
from sympy.abc import x

from methods import simpsons_method, rectangle_method, RectangleType

functions = {
    "x³ - 3x² + 6x - 19": x ** 3 - 3 * x ** 2 + 6 * x - 19,
    "-4x³ - 3x² + 5x - 20": -4 * x ** 3 - 3 * x ** 2 + 5 * x - 20
}

methods = {
    "Метод прямоугольников (левые)": lambda f, p: rectangle_method(RectangleType.LEFT, f, *p),
    "Метод прямоугольников (правые)": lambda f, p: rectangle_method(RectangleType.RIGHT, f, *p),
    "Метод прямоугольников (средние)": lambda f, p: rectangle_method(RectangleType.MIDDLE, f, *p),
    "Метод Симпсона": lambda f, p: simpsons_method(f, *p)
}

if __name__ == '__main__':
    method_name = choose_from_dict(methods, "Выберите метод")
    function_name = choose_from_dict(functions, "Выберите функцию")

    method = methods[method_name]
    function = functions[function_name]
    parameters = read_parameters()

    method(function, parameters)
