# ===== NUMBER GUESSING GAME =====

import random

target = random.randint(1,100)
count = 0

while True:
    userChoice = input("GUESS THE TARGET OR QUIT (Q): ")
    if(userChoice=="Q"):
        break

    count += 1
    userChoice = int(userChoice)
    if(userChoice==target):
        print("SUCCESS : CORRECT GUESS!!")
        print("YOU GUESSED THE TARGET IN",count,"ATTEMPTS")
        break
    elif(userChoice < target):
        print("YOUR GUESSED NUMBER WAS TOO SMALL. MAKE A BIGGER GUESS..")
    else:
        print("YOUR GUESSED NUMBER WAS TOO BIG. MAKE A SMALLER GUESS..")

print("------------GAME OVER------------")
