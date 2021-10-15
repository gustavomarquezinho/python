# 035 - Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def verifyValues(pNum1, pNum2):
    return (pNum1 == pNum2) or (pNum1 + pNum2) == 5 or abs(pNum1 - pNum2) == 5

print(verifyValues(7, 2), verifyValues(3, 2), verifyValues(2, 2))