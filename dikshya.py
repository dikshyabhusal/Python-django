import random

print("WELCOME!!!!!!!!!!!!!!!!!!!")
print("You have 5 chances to guess the correct number.")
print("----------------------------------------")


guess_number = random.randrange(1, 100)
attempts = 1



while attempts <= 5:
    user_guess = int(input(f"Attempt {attempts}: ENTER YOUR GUESS: "))
    
    attempts += 1
    
    if user_guess < guess_number:
        print("Too low! Try again.")
    elif user_guess > guess_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number correct in {attempts} attempts....Hurrayyy!")
        break

if user_guess != guess_number:
    print(f"Sorry, you've used all  attempts. The correct number was {guess_number}. Better luck next time!")