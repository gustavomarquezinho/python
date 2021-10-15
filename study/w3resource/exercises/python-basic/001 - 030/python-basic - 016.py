# 016 - Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

numberInfo = int(input('Enter a number: '))
print((17 - numberInfo) if 17 >= numberInfo else (numberInfo - 17) * 2)