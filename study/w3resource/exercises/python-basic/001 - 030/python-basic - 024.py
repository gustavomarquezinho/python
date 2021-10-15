# 024 - Write a Python program to test whether a passed letter is a vowel or not.

def vowelLetter(pLetter):
    return pLetter.upper() in 'AEIOU'

print(vowelLetter('A'))
print(vowelLetter('B'))