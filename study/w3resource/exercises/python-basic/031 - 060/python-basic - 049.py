# 049 - Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile, join

print(list(i for i in listdir('') if isfile(join('', f))))