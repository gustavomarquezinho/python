# 027 - Write a Python program to concatenate all elements in a list into a string and return it.

def concatenateArray(pArray):
    pConcatenate = ''

    for i in pArray:
        pConcatenate += str(i)
    return pConcatenate

print(concatenateArray([3, 5, 7, 2, 10, 12]))