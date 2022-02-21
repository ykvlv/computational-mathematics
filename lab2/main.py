import sys

from termcolor import cprint

from iohandler import print_hello, print_help

from method import get_method

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_hello()
        method = get_method(sys.stdin, True)
    elif sys.argv[1] == "file":
        file = open(sys.argv[2], "r")
        method = get_method(file, False)
    else:
        print_help()
        sys.exit(1)

    report, table = method.solve()
    # TODO вывод в файл
    cprint(report, "cyan")
    print()
    cprint(table, "blue")
