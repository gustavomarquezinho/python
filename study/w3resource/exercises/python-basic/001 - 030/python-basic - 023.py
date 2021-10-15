# 023 - Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def copyString(pString, pTimes):
    return (pString[:2 if len(pString) >= 2 else 1] * pTimes)

print(copyString('Copy', 2), copyString('C', 4))