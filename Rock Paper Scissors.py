import random
i = True
x = ""
trueComputerChoice = ""
random.randint(1,2)
while (i == True):
    print("Rock Paper Scissors!    ")
    playerChoice = input("Type R, P or S    ").lower()
    ComputerChoiceIndex = random.randint(1,3)

    if (ComputerChoiceIndex == 1):
        trueComputerChoice = "r"
    elif (ComputerChoiceIndex == 2):
        trueComputerChoice = "p"
    else:
        trueComputerChoice = "s"
    
    print(trueComputerChoice)

    if (playerChoice == trueComputerChoice):
        print("Tie!")
        x = input("Play again? Y/N   ").lower()
    elif (playerChoice == "r"):
        if (trueComputerChoice == "p"):
            print("You lose!")
            x = input("Play again? Y/N   ").lower()
        else: 
            print("You win!")
            x = input("Play agian? Y/N    ").lower()
    elif (playerChoice == "p"):
        if (trueComputerChoice == "s"):
            print("You lose!")
            x = input("Play again? Y/N   ").lower()
        else: 
            print("You win!")
            x = input("Play agian? Y/N    ").lower()
    elif (playerChoice == "s"):
        if (trueComputerChoice == "r"):
            print("You lose!")
            x = input("Play again? Y/N   ").lower()
        else: 
            print("You win!")
            x = input("Play agian? Y/N    ").lower()
    if (x == "y"):
        i = True
    else: 
        i = False