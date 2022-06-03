from approximation import *
from io_approximation import request_file, parse_input, show_graph

approximations = [
    ['Линейная функция', linear],
    ['Квадратичная функция', quadratic],
    ['Кубическая функция', cubic],
    ['Экспоненциальная функция', exponential],
    ['Степенная функция', power],
    ['Логарифмическая функция', logarithmic],
]

if __name__ == '__main__':
    inp = request_file("Путь до входного файла (из консоли — Enter): ", "r")
    xs, ys, n = parse_input(inp)
    out = request_file("Путь до выходного файла (в консоль — Enter): ", "w")

    for i in xs:
        if i < 0:
            approximations.remove(approximations[5])
            approximations.remove(approximations[4])
            out.write("Логарифмическая Степенная ")
            break
    for i in ys:
        if i < 0:
            if len(approximations) > 4:
                approximations.remove(approximations[4])
                out.write("Степенная ")
            approximations.remove(approximations[3])
            out.write("Экспоненциальная ")
            break
    if len(approximations) < 6:
        out.write("функции не могут аппроксимировать на отрицательных значениях.\n")

    for i in range(len(approximations)):
        deviation, dispersion, confidence, function, string = approximations[i][1](xs, ys, n)
        approximations[i] += [deviation, function, string]
        out.writelines(f'{i + 1}. {approximations[i][0]}\n'
                       f'phi(x) = {string}\n'
                       f'S = {dispersion:.3f}\n'
                       f'δ = {deviation:.3f}\n'
                       f'R^2 = {confidence:.3f}\n')

    best_approximation = approximations[0]
    for approximation in approximations:
        if approximation[2] < best_approximation[2]:
            best_approximation = approximation
    out.writelines(f'\nЛучше всего аппроксимирует {best_approximation[0]}: '
                   f'δ = {best_approximation[2]:.3f}\n')

    show_graph(xs, ys, approximations)
