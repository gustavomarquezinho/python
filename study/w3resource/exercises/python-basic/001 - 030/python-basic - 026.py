# 026 - Write a Python program to create a histogram from a given list of integers.

def createHistogram(pValues):
    for i in pValues:
        print('*' * i)

createHistogram([2, 3, 6, 5])