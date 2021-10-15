from random import sample
from time import sleep
from os import system


memoryInfo = [
]

memoryStatus = [
    0, 0, 0
]


def cleanMemory():
    system("cls")

def printEx(pMessage, pBefore, pLater, pClean):
    if pClean == 0:
        cleanMemory()

    sleep(pBefore)
    print(pMessage)
    sleep(pLater)

    if pClean == 1:
        cleanMemory()


memoryLevel, memoryType = -1, -1


while True:
    memoryWord = ""
    cleanMemory()

    while memoryLevel < 0 or memoryLevel > 3:
        memoryLevel = int(input(": 0 : Close\n: 1 : Easy\n: 2 : Medium\n: 3 : Hard\n\nDifficulty: "))
        
    if memoryLevel == 0:
        cleanMemory()
    
        printEx(f"You played this game {memoryStatus[0] + memoryStatus[1]} times", 0.5, 0.5, -1)
        printEx(f"Won: {memoryStatus[0]} / Loss: {memoryStatus[1]} / Points: {memoryStatus[2]}", 0.5, 2.0, -1)

        printEx("\n› I hope to see you again!\n", 0.5, 3.0, -1)
        break
    
    sleep(1)

    while memoryType < 0 or memoryType > 3:
        cleanMemory()
        memoryType = int(input(": 0 : Back\n: 1 : Letter\n: 2 : Number\n: 3 : Both\n\nType: "))

        if memoryType == 0:
            memoryLevel = -1
    
    sleep(1)

    if memoryType >= 1:
        memoryChoice = sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", int(26 * (memoryLevel * 20 / 100))) if memoryType == 1 else sample("01234567890123456789", int(20 * (memoryLevel * 20 / 100)))
    
        cleanMemory()

        for i in memoryChoice:
            memoryWord += i

        print(memoryWord)

        sleep(4 + (memoryLevel * 2))
        cleanMemory()

        memoryUser = input("Type 0 to go back to the menu\n::: What was the combination? ")

        if memoryUser == "0":
            memoryType = -1
        else:
            printEx(f"\nCombination: {memoryWord}", 1, 1, -1)

            if memoryWord == memoryUser:
                printEx("+ Win +", 1, 3, 1)

                memoryStatus[2] += memoryLevel 
                memoryStatus[0] += 1
            else:
                printEx("- Loss -", 1, 3, 1)

                memoryStatus[2] -= memoryLevel 
                memoryStatus[1] += 1
