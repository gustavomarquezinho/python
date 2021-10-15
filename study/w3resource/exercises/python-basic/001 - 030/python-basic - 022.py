# 022 - Write a Python program to count the number 4 in a given list.

def fourCount(pNumbers):
    return pNumbers.count(4)

print(fourCount([1, 2, 9, 4, 3, 4]), fourCount([4, 2, 3, 4, 4, 0]))