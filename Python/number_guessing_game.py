#number guessing game in python
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print ("Please type a number larger than 0 next time.")
        quit()
else:
    print ("Please type a number next time.")
    quit()
    
random_num = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Make a guess: ")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print ("Please type a number next time.")
        continue

    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num:
        print ("You were above the number!")
    else:
        print ("You were below the number!")
    
print ("You got it in", guesses, "guesses.") 
