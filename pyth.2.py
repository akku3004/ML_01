import random
num= random.randint(0,50)
print("Welcome to guess game \n I'm thinking of a number, \n let's see if you can guess it")
for i in range(5):
    guess = int(input(f"Chance {i+1}:"))
    if guess < num:
        print("You guessed lower. Try guessing higher")
    elif guess> num:
        print("You guessed higher: Try guessing lower")
    else:
        print(f"You guessed it!! Congrats, You used {i} guesses")
else:
    print("Game over, You used all attempts")