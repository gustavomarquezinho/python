# 042 - Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

from struct import calcsize
print(calcsize('P') * 8)