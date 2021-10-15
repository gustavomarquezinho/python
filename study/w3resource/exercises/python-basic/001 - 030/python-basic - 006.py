# 006 - Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numberInfo = input('Input some comma separated numbers: ').split(",")
print(f'\nList: {list(numberInfo)}\nTuple: {tuple(numberInfo)}\n')