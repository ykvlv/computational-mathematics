from io_helper import request_file, parse_input

if __name__ == '__main__':
    inp = request_file("Путь до входного файла (в консоль — Enter): ", "r")
    dots = parse_input(inp)

    out = request_file("Путь до выходного файла (в консоль — Enter): ", "w")
