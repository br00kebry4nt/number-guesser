import random

correct_number = random.randint(1, 100)

attempt_count = 0
allowed_attempts = 7
keepGoing = True

print("You have 7 tries to guess a number between 1-100.")

while keepGoing:
    
    user_guess = input("What is your guess? ")
    
    if user_guess.isdigit():
        guess = int(user_guess)
        
        if guess > correct_number:
            print("Too high")
        if guess < correct_number:
            print("Too low")
        if guess == correct_number:
            print(f"Congrats, you won in {attempt_count + 1} turns!")
            keepGoing = False
        else:
            attempt_count += 1
    else:
        print("That's not a valid number, you lose a turn!")
        attempt_count += 1
    
    if attempt_count >= allowed_attempts:
        if guess != correct_number:
            print("Looks like you are on the losing side this time!")
        keepGoing = False
        