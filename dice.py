import random

firstUserDice = 0
secondUserDice = 0

firstUserScore = 0
secondUserScore = 0

print("Welcome to dice game!")

def dice():
    diceNumber = random.randint(1,6)
    diceNumber2 = random.randint(1,6)
    diceTotal = diceNumber + diceNumber2
    print(f"First dice: {diceNumber}")
    print(f"Second dice: {diceNumber2}")
    print(f"Dice total: {diceTotal}")
    return diceTotal

while True:
    userChoice = input("Player one enter to play, for quit (q) ")

    if userChoice == "q":
        break

    firstUserDice = dice()

    userChoice = input("Player two enter to play, for quit (q) ")

    if userChoice == "q":
        break

    secondUserDice = dice()

    if firstUserDice > secondUserDice:
        firstUserScore += 1
        print(f"Player one wins! Score {firstUserScore} : {secondUserScore}")
        firstUserDice = 0
        secondUserDice = 0
    elif firstUserDice < secondUserDice:
        secondUserScore += 1
        print(f"Player two wins! Score {firstUserScore} : {secondUserScore}")
        firstUserDice = 0
        secondUserDice = 0
    elif firstUserDice == secondUserDice:
        print(f"Draw! Score {firstUserScore} : {secondUserScore}")
        firstUserDice = 0
        secondUserDice = 0

    if firstUserScore == 3:
        print("Player one wins the game!")
        break
    elif secondUserScore == 3:
        print("Player two wins the game!")
        break
