import sys

from termcolor import cprint, colored

from io_helper import print_help, fatal_error
from method import get_method

if __name__ == '__main__':
    input_stream = sys.stdin
    with_invite = True
    output_stream = sys.stdout
    file_name = None
    with_graph = False

    if "--help" in sys.argv:
        print_help()
        sys.exit()
    if "--in" in sys.argv:
        try:
            input_stream = open(sys.argv[sys.argv.index("--in") + 1], "r")
            with_invite = False
        except OSError as e:
            fatal_error("Прочитать из файла не получится. " + e.strerror)
    if "--out" in sys.argv:
        try:
            file_name = sys.argv[sys.argv.index("--out") + 1]
            output_stream = open(file_name, "w")
        except OSError as e:
            fatal_error("Записать в файл не получится. " + e.strerror)
            sys.exit(e.errno)

    method = get_method(input_stream, with_invite)
    report, table, graph = method.solve()

    if file_name:
        output_stream.write(report + "\n\n")
        output_stream.write("Таблица итераций:\n" + str(table))
        cprint(f"Файл {file_name} записан успешно!", "green")
    else:
        output_stream.write(colored(report + "\n\n", "cyan"))
        output_stream.write(colored("Таблица итераций:\n" + str(table) + "\n", "blue"))

    graph[0](graph[1], graph[2])
    input_stream.close()
    output_stream.close()
