# 036 - Write a Python program to add two objects if both objects are an integer type.

def sumInteger(pNum1, pNum2):
    if (int(pNum1) != pNum1) or (int(pNum2) != pNum2):
        return "Inputs must be integers"
    return pNum1 + pNum2

print(sumInteger(10, 20))
print(sumInteger(10.5, 20))
print(sumInteger(10, 20.5))