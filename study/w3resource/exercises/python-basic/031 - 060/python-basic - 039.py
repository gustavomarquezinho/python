# 039 - Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

def futureValue(pValue, pRate, pYears):
    return round(pValue * ((1 + (0.01 * pRate)) ** pYears), 2)

print(futureValue(10000, 3.5, 7))