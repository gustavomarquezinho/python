# 033 - Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sumThrice(pNumber1, pNumber2, pNumber3):
    return (0 if (pNumber1 == pNumber2 or pNumber1 == pNumber3 or pNumber2 == pNumber3) else (pNumber1 + pNumber2 + pNumber3))

print(sumThrice(5, 7, 9), sumThrice(6, 8, 8))