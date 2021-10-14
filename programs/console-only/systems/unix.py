monthInfo = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]


def dateToUnix(pDay, pMonth, pYear, pHours, pMinutes, pSeconds):
    return ((pDay + (365 * (pYear - 1970)) + (int(((pYear - 1) - 1970) / 4)) + sum(monthInfo[0:(pMonth - 1)])) * 86400) + ((pHours + 3) * 3600) + (pMinutes * 60) + pSeconds


print(dateToUnix(23, 3, 2021, 12, 42, 10))