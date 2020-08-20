import random


sticks = random.randint(15, 25)
player = 1

while True:
    nmbOfPlayers = int(input("Choose 1 or 2 players "))

    try:
        if int(nmbOfPlayers) < 1 or int(nmbOfPlayers) > 2:
            print("Please choose a number between 1 and 2")

        else:
            break

    except ValueError:
        print("Your input was not a number")

if nmbOfPlayers < 2:
    while True:

        aiIntellect = input("Choose AI Difficulty. Random(1), Normal(2) or Difficult(3): ")

        try:
            if int(aiIntellect) < 1 or int(aiIntellect) > 3:
                print("Please choose either 1, 2 or 3")
            else:
                break
        except ValueError:
            print("Your input was not a valid number")

    player1Name = input("Choose a name for player 1: ")
    player2Name = "AI"

else:
    player1Name = input("Choose a name for player 1: ")
    player2Name = input("Choose a name for player 2: ")

while True:
    print("\n")
    tempSticks = sticks
    while tempSticks > 0:
        if ((sticks-tempSticks) % 5) == 0:
            print(" ", end="")

        print("|", end="")
        tempSticks = tempSticks-1
    #print(str(sticks)+" sticks remain.")

    while True:

        if player == 1:
            removed = input(" "+player1Name + " choose either to remove one or two sticks: ")
        if player == 2 and nmbOfPlayers == 2:
            removed = input(" "+player2Name + " choose either to remove one or two sticks: ")

        if player == 2 and nmbOfPlayers == 1:
            if aiIntellect == 1:
                removed = random.randint(1, 2)

            if aiIntellect == 2:
                if 5 >= sticks >= 4:
                    removed = sticks-3
                if sticks <= 2:
                    removed = 2
                else:
                    removed = random.randint(1, 2)

            if aiIntellect == 3:
                if 5 >= sticks >= 4:
                    removed = sticks-3
                if sticks == 2:
                    removed = 2
                if (sticks % 2) == 0:
                    remove = 1
                else:
                    remove = 2

            print(" AI removes " + str(removed) + " sticks")


        try:
            checkRemoved = int(removed)
            if checkRemoved < 1 or checkRemoved > 2:
                print("Please choose a number between 1 and 2")
            else:
                break
        except ValueError:
            print("Your input was not a number")

    sticks = sticks-checkRemoved

    if sticks <= 0 and player == 1:
        print(player1Name+" has won the game!")
        break

    if sticks <= 0 and player == 2:
        print(player2Name + " has won the game!")
        break

    if player == 1:

        player = 2

    else:
        player = 1







