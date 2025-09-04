import random # Python’s random tool.

secret_number = random.randint(1, 12) # Randomly select a number between 1 and 12.

guess = 0 # starts with no guess yet and at 0. We define it before using it.

while guess != secret_number: # the loop starts
    guess = int(input("Enter your guess: ")) # the guess happens, maintaining the same hidden selected value.

    if guess < secret_number:
        print("too low champ! try again.")
    elif guess > secret_number:
        print("Too high buddy! try again.")
    else:
        print(f"You got it! congrats Cangrejero! The Number was {secret_number}!")
