# 034 - Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sumTwice(pNum1, pNum2):
    return (20 if 15 <= (pNum1 + pNum2) <= 20 else (pNum1 + pNum2)) 

print(sumTwice(10, 6), sumTwice(10, 2), sumTwice(10, 12), sumTwice(10, 5), sumTwice(15, 5))