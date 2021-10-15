# 051 - Write a Python program to determine profiling of Python programs.

from cProfile import run

def Sum():
    print(1 + 2)

run('Sum()')