import random
def guess():
    options = ["Rock", "Paper", "Scissors"]
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Choose: Rock, Paper, Scissors ")

    userChoice = input("Your Choice: ").lower().capitalize()
    if userChoice not in options:
        print("Invalid Choice")
        return guess()
    
    computerChoice = random.choice(options)
    print(f"Computer chose : {computerChoice}")

    if userChoice == computerChoice:
        print("Tie!")
    elif (userChoice == "Rock" and computerChoice == "Scissors") or\
         (userChoice == "Scissors" and computerChoice == "Paper" ) or\
         (userChoice == "Paper" and computerChoice == "Rock"):
         print("You Win!")
    else:
        print("Computer Win!")

    tryAgain = input("Do you want to play again? (Y/N): ").lower().capitalize()
    if tryAgain == "Y":
        guess()
    else:
        print("Thanks for playing")

guess()