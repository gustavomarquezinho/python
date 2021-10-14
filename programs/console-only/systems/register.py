from time import sleep
from os import system


infoName = {
    1000: "Gustavo", 1001: "Henrique"
}

infoAge = {
    1000: 18, 1001: 17
}

userTotal = len(infoName) - 1


def showUserMenu():
    print(": 1 : Register user\n: 2 : Remove user\n: 3 : Search user\n: 4 : Show user\n: 5 : Close")


def printEx(pMessage, pBefore, pLater, pClean):
    if pClean == 0:
        system("cls")

    sleep(pBefore)
    
    if pMessage not in "":
        print(pMessage)

    sleep(pLater)

    if pClean == 1:
        system("cls")

    showUserMenu()


def menuRegister():
    global userOption

    if userOption != 1:
        return False

    userName, userAge = "", -1

    while userName == "":
        userName = input("\n- Enter the name: ")

    while userAge < 0 or userAge > 125:
        userAge = int(input("- Enter the age: "))

    global userTotal
    userTotal += 1

    userIndex, infoName[userIndex], infoAge[userIndex] = (userTotal + 1000), userName, userAge
    printEx("\n› Successfully registered user!", 0, 3, 1)
    return  True


def menuSearch(pRemove=0):
    global userOption

    if userOption != (2 if pRemove == 1 else 3):
        return False

    userIndex = -1

    if len(infoName) == 0:
        printEx("\nx There is no registered at the moment!", 0, 3, 1)
    else:
        userSearch = input("\n- Enter Name, Age or ID: " if pRemove == 0 else "\n - Enter ID: ").upper()

        if userSearch.isdigit():
            userSearch = int(userSearch)

            if userSearch >= 1000:
                if userSearch in infoName.keys():
                    userIndex = userSearch

                    if pRemove == 0:
                        printEx(f": {userIndex} : {infoName[userIndex]} - {infoAge[userIndex]}\n", 0, 3, 0)
                    else:
                        printEx(f"\n› User ': {userIndex} : {infoName[userIndex]} - {infoAge[userIndex]}' has been removed!\n", 0, 3, 0)

                        del infoName[userIndex]
                        del infoAge[userIndex]
            else:
                if pRemove == 1:
                    userIndex = 0
                else:
                    printEx("", 0, 3, 0)

                    for x in infoAge:
                        if infoAge[x] == userSearch:
                            print(f": {x} : {infoName[x]} - {infoAge[x]}")
                            userIndex = 1
                            
                    print()
        else:
            if pRemove == 1:
                userIndex = 0
            else:
                printEx("", 0, 3, 0)

                for x in infoName:
                    if infoName[x].upper() == userSearch:
                        print(f": {x} : {infoName[x]} - {infoAge[x]}")
                        userIndex = 1

                printEx("", 0, 3, -1)

        if userIndex == 0:
            printEx("\nx You can only remove a user by ID!", 0, 3, 1)
        elif userIndex == -1:
            printEx("\nx No results were found!", 0, 3, 1)



def menuUsers():
    global userOption

    if userOption != 4:
        return False

    if len(infoName) == 0:
        printEx("\nx There is no registered at the moment!", 0, 3, 1)
    else:
        system("cls")

        for x in infoName:
            print(f": {x} : {infoName[x]} - {infoAge[x]}")

        printEx(" ", 0, 3, -1)


def menuClose():
    global userOption

    if userOption != 5:
        return False

    printEx("\n› I hope to see you again!\n", 0, 0, 0)


while True:
    printEx("", 0, 0, 0)
    userOption = -1

    while userOption != 5:
        userOption = input("\n::: Choose an option : ")

        if not userOption.isdigit():
            printEx("\nx Enter only numbers!", 0, 3, 1)
        else:
            userOption = int(userOption)

            menuFunctions = {
                1: menuRegister(), 2: menuSearch(1), 3: menuSearch(0), 4: menuUsers(), 5: menuClose()
            }

            menuFunctions[userOption]

    if userOption == 5:
        break