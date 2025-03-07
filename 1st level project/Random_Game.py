import random
def guess_num():
    rand_num = random.randint(1, 100)
    attempts = 0

    print("Hello, this is a random number game!")
    print("I'm thinking about number between 0 and 100, guess it")
    
    while True:
        guess = int(input("Guess number"))
        attempts += 1
        
        if guess < rand_num:
            print("Too low, try again!")
        elif guess > rand_num:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
guess_num()