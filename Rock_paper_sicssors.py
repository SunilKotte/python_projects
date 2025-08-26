import random

user_win=0
computer_win=0

options = ["rock","paper","scissors"]
while True:
    user_input= input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)


    computer_guess= options[random_number]

    print ("Computer picked", computer_guess + ".")


    if user_input == "rock" and computer_guess =="scissors":
        print("You WON!")
        user_win += 1
        
    elif user_input == "paper" and computer_guess =="rock":
        print("You WON!")
        user_win += 1

    elif user_input == "scissors" and computer_guess =="paper":
        print("You WON!")
        user_win += 1
        
    else:
        print("Computer Wins !!")
        computer_win += 1

print("you win ", user_win," & Computer wins", computer_win)

print("Good Bye")
