# 018 - Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

def sumThrice(pX, pY, pZ):
    return ((pX + pY + pZ) * (3 if pX == pY == pZ else 1))

print(sumThrice(3, 5, 7))
print(sumThrice(8, 8, 8))