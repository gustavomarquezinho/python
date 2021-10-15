from random import choice, sample
from time import sleep
from os import system


hangmanDifficulty = [
    "Easy", "Medium", "Hard"
]

hangmanInfo = {
    "PERSON": ": GERAL :", "WATERMELON": ": FRUITS :", "COMPUTER": ": OBJECTS :", "FOX": ": ANIMALS :"
}

hangmanStatus = [
    0, 0, 0
] 


def cleanHangman(pTime):
    sleep(pTime)
    system("cls")


def closeHangman():
    cleanHangman(1)

    print(f"You played this game {hangmanStatus[0] + hangmanStatus[1]} times")
    print(f"Won: {hangmanStatus[0]} / Loss: {hangmanStatus[1]} / Points: {hangmanStatus[2]}")

    print("\n› I hope to see you again!\n")


def showHangman(pAttempts, pWord):
    cleanHangman(2)

    hangmanBody = {
        0: "|========|\n|         \n|         \n|         \n|         \n|\n|",
        1: "|========|\n|        0\n|         \n|         \n|         \n|\n|",
        2: "|========|\n|        0\n|        |\n|         \n|         \n|\n|",
        3: "|========|\n|        0\n|       /|\n|         \n|         \n|\n|",
        4: "|========|\n|        0\n|       /|\\\n|         \n|         \n|\n|",
        5: "|========|\n|        0\n|       /|\\\n|        |\n|         \n|\n|",
        6: "|========|\n|        0\n|       /|\\\n|        |\n|       /\n|\n|",
        7: "|========|\n|        0\n|       /|\\\n|        |\n|       / \\\n|\n|",
    }

    print(hangmanBody.get(pAttempts, "Nothing"))
    print(hangmanInfo[hangmanChoice].center(30))
    print(pWord.center(30))


while True:
    hangmanLevel = -1

    while hangmanLevel < 0 or hangmanLevel > 3:
        cleanHangman(0)
        hangmanLevel = int(input(": 0 : Close\n: 1 : Easy\n: 2 : Medium\n: 3 : Hard\n\nDifficulty: "))

    if hangmanLevel == 0:
        closeHangman()
        break

    print(f"\n› You selected {hangmanDifficulty[hangmanLevel - 1]} difficulty.")
    hangmanChoice = hangmanDisplay = choice(list(hangmanInfo.keys()))

    hangmanLetter = dict(zip(sample(hangmanChoice, int(len(hangmanChoice) * hangmanLevel * 0.25)), [i * 0 for i in range(len(hangmanChoice))]))

    for i in hangmanLetter.keys():
        hangmanDisplay = hangmanDisplay.replace(i, "_")

    hangmanAttempts = 0

    while hangmanAttempts <= 7:
        showHangman(hangmanAttempts, hangmanDisplay if hangmanAttempts < 7 else hangmanChoice)

        if hangmanAttempts == 7:
            print("\nx You miss!")
            cleanHangman(2)

            hangmanStatus[2] -= hangmanLevel
            hangmanStatus[1] += 1
            break

        hangmanUser = ""

        while hangmanUser == "":
            hangmanUser = input("\n::: Choose a letter : ").strip().upper()

            if hangmanUser == "0":
                break

            if len(hangmanUser) != 1 or hangmanUser not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("\nx You can only use letters and only 1 character!")
                hangmanUser = ""

        if hangmanUser in hangmanLetter:
            if hangmanLetter[hangmanUser] == 1:
                print("\nx You already used this letter!")
            else:
                hangmanLetter[hangmanUser] = 1

                if 0 not in hangmanLetter.values():
                    print(f"\n› Correct word ({hangmanChoice})!")
                    hangmanAttempts = 8

                    hangmanStatus[2] += hangmanLevel
                    hangmanStatus[0] += 1

                    cleanHangman(2)
                else:
                    print(f"\n› Correct letter!")

                    for i in range(len(hangmanChoice)):
                        if hangmanChoice[i] == hangmanUser:
                            hangmanDisplay = hangmanDisplay[:i] + hangmanUser + hangmanDisplay[i+1:]
        else:
            print("\nx Wrong letter!")
            hangmanAttempts += 1
