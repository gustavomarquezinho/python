# 019 - Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def newString(pString):
    if len(pString) >= 2 and pString[:2] == 'Is':
        return pString
    return 'Is' + pString

print(newString('IsArray'))
print(newString('Empty'))
