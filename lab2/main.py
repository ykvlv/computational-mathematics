import sys


from methods import *

if __name__ == '__main__':
    sys.stdin.
    if len(sys.argv) < 2:
        print_hello()
        method = get_method()
    elif sys.argv[1] == "file":
        method = read_from_file(sys.argv[2])
    else:
        print_help()


    method.solve()
