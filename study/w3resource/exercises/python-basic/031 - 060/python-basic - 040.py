# 040 - Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

from math import sqrt

def returnDistance(xPos1, yPos1, xPos2, yPos2):
    return round(sqrt(((xPos1 - xPos2) ** 2) + ((yPos1 - yPos2) ** 2)), 4)

print(returnDistance(4, 0, 6, 6))