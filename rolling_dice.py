import random

def roll():
    min_value= 1
    max_value= 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("who many players are playing this game:(enter between 1-4)")
    if players.isdigit():
        players= int(players)
        if 2<= players <=4:
            break
        else:
            print("Must be between 2-4 players")

    else:
        print("Invaild, try again")

max_Score= 50

player_scores= [0 for _ in range(players)]

while max(player_scores) < max_Score:

    for player_Num in range(players):
        
        current_Score=0
        print("\n PLayeer number ", player_Num+1, " turn has just started ")
        print("your current score is ", player_scores[player_Num], "\n")
    
        while True:
            should_roll = input("would you like to Roll ?? (Y/N):  ")
            
            if should_roll.lower() != "y":
                break

            value= roll()
            if value ==1:
                print("you have rolled the value ", value, "  : your turn is done!")
                current_Score = 0
                break
            else:
                current_Score += value
                print("you have rolled :  ", value)

            print("your current score: ", current_Score)
        player_scores[player_Num] += current_Score
        print("your total score is : ", player_scores[player_Num])

max_Score = max(player_scores)
winning_Num = player_scores.index(max_Score)

print("Player number  ", winning_Num+1, "  is the winner with the score of : ", max_Score)
    
