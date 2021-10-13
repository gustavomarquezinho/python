from random import randint
from time import sleep
from os import system


jokenpoInfo = [
    "ROCK", "PAPER", "SCISSORS"
]

jokenpoWin = {
    0:2, 1:0, 2:1
}

jokenpoUser = [
    0, 0, 0
]


def printEx(pMessage, pBefore, pLater):
    sleep(pBefore)
    print(pMessage)
    sleep(pLater)    

def jokenpoMessage(pContinue):
    system("cls")

    print('| ============================= |')
    print('|          x Jokenpo x          |')
    print('| ============================= |')

    if pContinue == 0:
        printEx(f"\nYou played this minigame {sum(jokenpoUser)} times", 0.5, 0.5)
        printEx(f"   Won: {jokenpoUser[0]} / Loss: {jokenpoUser[1]} / Draw: {jokenpoUser[2]} ", 0.5, 0.5)

        printEx("\n› Goodbye!\n", 0.5, 3.0)


while True:
    userChoice = -1

    while userChoice == -1:
        jokenpoMessage(1)
        userChoice = int(input("\n: 0 : Close\n: 1 : Rock\n: 2 : Paper\n: 3 : Scissors\n\nChoose an option: "))

        if userChoice < 0 or userChoice > 3:
            printEx("\nx Invalid option!\n", 0.5, 3.0)
            userChoice = -1

    if userChoice == 0:
        jokenpoMessage(0)
        break

    enemyChoice = randint(0, 2)

    printEx(f"\nYou chose '{jokenpoInfo[userChoice - 1]}'.", 0.5, 0.5)
    printEx(f"Your opponent chose '{jokenpoInfo[enemyChoice]}'.", 0.5, 0.5)

    if jokenpoWin[userChoice - 1] == enemyChoice:
        printEx("\n+ Won +\n", 1.0, 3.0)
        jokenpoUser[0] += 1

    elif (userChoice - 1) == enemyChoice:
        printEx("\n= Draw =\n", 1.0, 3.0)
        jokenpoUser[2] += 1

    else:
        printEx("\n- Loss -\n", 1.0, 3.0)
        jokenpoUser[1] += 1
