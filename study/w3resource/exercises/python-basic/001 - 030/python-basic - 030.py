# 030 -  Write a Python program that will accept the base and height of a triangle and compute the area.

def triangleArea():
    return (float(input('Base: ')) * float(input('Height: '))) / 2

print(f'Area = {triangleArea()}')