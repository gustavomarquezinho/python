# 012 - Write a Python program to print the calendar of a given month and year.

from calendar import month
print(month(int(input('Year: ')), int(input('Month: '))))