# 052 - Write a Python program to print to stderr.

from __future__ import print_function
from sys import stderr

def printe(*pArgs, **pKwargs):
    print(*pArgs, file=stderr, **pKwargs)

printe('abc', 'efg', 'xyzm', sep = '--')