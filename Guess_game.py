import random

print("Hello , What is your name?")
name = input()

print('Well,'+ name + ' , Iam thinking a number between 0 to 20 ')

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range= int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
secretNumber = random.randint(0,top_of_range)
guess =1

while True:
    
    user_guess=input("make a guess: ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == secretNumber:
        print("you Got it this time!!!")
        break
    elif user_guess> secretNumber:
        print("you were above the number")
    else:
        print("you were below the number")
    guess += 1

print("you got it in", guess, "guesses")
    
