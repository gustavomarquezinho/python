# 043 - Write a Python program to get OS name, platform and release information.

from platform import release, system
from os import name

print(f'Name: {name}\nPlatform: {release()}\nRelease: {system()}')