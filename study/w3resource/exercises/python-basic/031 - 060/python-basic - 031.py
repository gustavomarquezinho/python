# 031 - Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def returnGCD(pNumber1, pNumber2):
    if pNumber1 % pNumber2 == 0:
        return pNumber2

    for i in range((pNumber1 if pNumber1 > pNumber2 else pNumber1), 0, -1):
        if pNumber1 % i == 0 and pNumber2 % i == 0:
            return i

print(returnGCD(12, 17), returnGCD(4, 6), returnGCD(32, 64))