# 021 - Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

print(f'\nThis is an {"EVEN" if int(input("Enter a number: ")) % 2 == 0 else "ODD"} number.\n')