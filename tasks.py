import random
question = input("Question: ")
random_number = random.randint(1, 9)
if random_number = 1:
  print("Yes - definitely.")
elif = 2 :
  print("It is decidedly so.")
elif = 2 :
  print("Without a doubt.")
elif = 2 :
  print("Reply hazy, try again.")
elif = 2 :
  print("Ask again later.")
elif = 2 :
  print("Better not tell you now.")
elif = 2 :
  print("My sources say no.")
elif = 2 :
  print("Outlook not so good.")
elif = 2 :
  print("Very doubtful.")
else:
  print("perhaps")


---------------------


height = int(input(" Your height in cm please: "))
credits = int(input(" how many credits do you have? "))
if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits")
else:
  print("Go home!")


--------------------

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# Q1
ans = int(input("Do you like Dawn or Dusk? 1) Dawn 2) Dusk "))
if ans == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif ans == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input")

# Q2
ans2 = int(input("When I’m dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold "))
if ans2 == 1:
    Hufflepuff += 2
elif ans2 == 2:
    Slytherin += 2
elif ans2 == 3:
    Ravenclaw += 2
elif ans2 == 4:
    Gryffindor += 2
else:
    print("Wrong input")

# Q3
ans3 = int(input("Which kind of instrument most pleases your ear? 1) Violin 2) Drums 3) Piano 4) Trumpet "))
if ans3 == 1:
    Slytherin += 4
elif ans3 == 2:
    Hufflepuff += 4
elif ans3 == 3:
    Ravenclaw += 4
elif ans3 == 4:
    Gryffindor += 4
else:
    print("Wrong input")

# scores
print("\nFinal Scores:")
print(f"Gryffindor: {Gryffindor}")
print(f"Ravenclaw: {Ravenclaw}")
print(f"Hufflepuff: {Hufflepuff}")
print(f"Slytherin: {Slytherin}")

houses = {
    "Gryffindor": Gryffindor,
    "Ravenclaw": Ravenclaw,
    "Hufflepuff": Hufflepuff,
    "Slytherin": Slytherin
}

sorted_houses = sorted(houses.items(), key=lambda x: x[1], reverse=True)
print(f"\nYour house is: {sorted_houses[0][0]}!")

-------------------------
print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')

------------------------

guess = 0
tries = 0

while guess != 6 and tries < 3:
    guess = int(input("Guess the num: "))
    tries += 1 

    if guess == 6:
        print("You got it!")
        break  
    elif tries == 1:
        print("You have only 2 tries left.")
    elif tries == 2:
        print("You have only 1 try left.")
    elif tries == 3:
        print("You used all your tries.")
    else:
      print("Lost")
-------------------------

for i in range(99, 0, -1):
  print(f'{i} Bottles of Beer')

------------------------
for num in range(1, 100):
  if num % 3 == 0 or num % 5 ==0:
    print("FizzBuzz")
  elif num % 5 ==0:
    print("Buzz")
  elif num % 3 ==0:
    print("Fizz")
  else:
    print("IDK")
    -------------------------

