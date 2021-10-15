# 017 - Write a Python program to test whether a number is within 100 of 1000 or 2000.

def nearThousand(pNumber):
    return ((abs(1000 - pNumber) <= 100) or (abs(2000 - pNumber) <= 100))

print(nearThousand(1000))
print(nearThousand(700))