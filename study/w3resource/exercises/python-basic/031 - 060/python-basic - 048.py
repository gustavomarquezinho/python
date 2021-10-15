# 048 - Write a Python program to parse a string to Float or Integer.

def convertString(pString):
    return int(float(pString)), float(pString)

print(convertString('01.23'))