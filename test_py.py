# Usage: py test_py.py 5

import sys


def fact(n):
    """
    Factorial function

    :arg n: Number
    :returns: factorial of n

    """
    if n == 0:
        return 1
    return n * fact(n - 1)


def main():
    res = fact(5)
    print(res)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
