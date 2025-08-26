print("Welcome to the Quiz Game")

print(" what is your name ?")

Name= input()

print("Hello "+ Name+ " nice to meet you!!")
print("you wanna Play?")

play= input("Yes or No").lower()

score= 0

if play != 'yes':
    quit()
print("Okay! lets play")

answer = input("What is CPU Means?").lower()

if answer == "controll processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

print("you got "+ str(score)+ " questions correct!")
    
print("you got "+ str(score/1 *100)+ " questions correct!")
