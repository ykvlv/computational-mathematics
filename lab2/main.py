import sys

from termcolor import cprint, colored

from io_helper import print_help
from method import get_method

if __name__ == '__main__':
    input_stream = sys.stdin
    with_invite = True
    output_stream = sys.stdout
    is_file_output = False

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
            output_stream = open(sys.argv[sys.argv.index("--out") + 1], "w")
            is_file_output = True
        except OSError as e:
            cprint("Записать в файл не получится. " + e.strerror, "red")
            sys.exit(e.errno)

    method = get_method(input_stream, with_invite)
    report, table = method.solve()

    # Для цветного вывода
    if is_file_output:
        output_stream.write(report + "\n\n")
        output_stream.write("Таблица итераций:\n" + table)
        cprint("Программа успешно завершила работу!", "green")
    else:
        output_stream.write(colored(report + "\n\n", "cyan"))
        output_stream.write(colored("Таблица итераций:\n" + table + "\n", "blue"))

    # input_stream.close()
    # output_stream.close()
