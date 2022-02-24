import sys

from termcolor import cprint, colored

from io_helper import print_help
from method import get_method

if __name__ == '__main__':
    input_stream = sys.stdin
    with_invite = True
    output_stream = sys.stdout
    is_file_output = False
    with_graph = False

    if "--help" in sys.argv:
        print_help()
        sys.exit()
    if "--in" in sys.argv:
        try:
            input_stream = open(sys.argv[sys.argv.index("--in") + 1], "r")
            with_invite = False
        except OSError as e:
            cprint("Прочитать из файла не получится. " + e.strerror, "red")
            sys.exit(e.errno)
    if "--out" in sys.argv:
        try:
            file_name = sys.argv[sys.argv.index("--out") + 1]
            output_stream = open(file_name, "w")
            is_file_output = True
        except OSError as e:
            cprint("Записать в файл не получится. " + e.strerror, "red")
            sys.exit(e.errno)
    if "--graph" in sys.argv:
        with_graph = True

    method = get_method(input_stream, with_invite)
    report, table = method.solve()

    # Для цветного вывода
    if is_file_output:
        output_stream.write(report + "\n\n")
        output_stream.write("Таблица итераций:\n" + table)
        cprint(f"Файл {file_name} записан успешно!", "green")
    else:
        output_stream.write(colored(report + "\n\n", "cyan"))
        output_stream.write(colored("Таблица итераций:\n" + table + "\n", "blue"))

    # input_stream.close()
    # output_stream.close()
