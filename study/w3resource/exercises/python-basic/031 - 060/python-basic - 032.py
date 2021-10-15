# 032 - Write a Python program to get the least common multiple (LCM) of two positive integers.

def returnLCM(pNumber1, pNumber2):
    pNumber3 = (pNumber1 if pNumber1 > pNumber2 else pNumber2)

    while True:
        if (pNumber3 % pNumber1 == 0) and (pNumber3 % pNumber2 == 0):
            return pNumber3

        pNumber3 += 1

print(returnLCM(4, 6), returnLCM(15, 17))