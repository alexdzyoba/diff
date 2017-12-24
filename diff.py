#!/usr/bin/env python3

"""Simple diff based on LCS solution"""

import sys
from functools import partial

from lcs import lcslen

# Print without newline because input files already have it
_print = partial(print, end='')

def print_diff(c, x, y, i, j):
    """Print the diff using LCS length matrix by backtracking it"""

    if i < 0 and j < 0:
        return ""
    elif i < 0:
        print_diff(c, x, y, i, j-1)
        _print("+ " + y[j])
    elif j < 0:
        print_diff(c, x, y, i-1, j)
        _print("- " + x[i])
    elif x[i] == y[j]:
        print_diff(c, x, y, i-1, j-1)
        _print("  " + x[i])
    elif c[i][j-1] >= c[i-1][j]:
        print_diff(c, x, y, i, j-1)
        _print("+ " + y[j])
    elif c[i][j-1] < c[i-1][j]:
        print_diff(c, x, y, i-1, j)
        _print("- " + x[i])

def diff(x, y):
    c = lcslen(x, y)
    return print_diff(c, x, y, len(x)-1, len(y)-1)

def usage():
    print("Usage: {} <file1> <file2>".format(sys.argv[0]))

def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2:
        diff(f1.readlines(), f2.readlines())

if __name__ == '__main__':
    main()
