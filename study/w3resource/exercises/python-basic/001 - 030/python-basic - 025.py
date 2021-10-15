# 025 - Write a Python program to check whether a specified value is contained in a group of values.

def containsValue(pValues, pNumber):
    return pNumber in pValues

print(containsValue([1, 5, 8, 3], 3))
print(containsValue([1, 5, 8, 3], -1))