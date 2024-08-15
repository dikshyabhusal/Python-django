import random

print("WELCOME TO NUMBER GUESSING")
print("ENTER A NUMBER BETWEEN 1 TO 100")

number = random.randrange(1,100)
attempts = 1

while attempts <= 5:
    guess =int(input(f"Attempt{attempts}:Enter guess: "))
    attempts = attempts +1
    if guess == number:
        print("Congrats!!!!! You won...Hurray!!!!!")
        break
    elif(guess < number):
        print("Too  Low! Guess Higher...")
    else:
        print("Too High!!Guess Lower...")
if guess != number :
    print(f"Sorry, you've used all  attempts. The correct number was {number}. Better luck next time!")
        



