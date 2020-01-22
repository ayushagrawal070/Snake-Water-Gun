import random

choices = ["s","w","g"]

n = 10
computer_points = 0
player_points = 0
tiepoints = 0
print("Enter s for SNAKE")
print("Enter w for WATER")
print("Enter g for GUN\n")
while(n>0) :
    n -= 1
    comp = random.choice(choices)
    human = input("Enter your choice : ")
    if (human == comp) :
        tiepoints += 1
        print("Computer choice - ", comp)
        print("Its a tie !!")
        print("Chances Left = ", n )
        print("Computer - " , computer_points , "You - ", player_points, "Tie - " , tiepoints)
        continue
    elif (human == "s" and comp == "w") :
        player_points+=1
        print("Computer choice - ", comp)
        print("Congrats.. You win !!")
        print("Chances Left = ", n)
        print("Computer - ", computer_points, "You - ", player_points, "Tie - ", tiepoints)
        continue
    elif (human == "s" and comp == "g"):
        computer_points += 1
        print("Computer choice - ", comp)
        print("Oops.. You lose !!")
        print("Chances Left = ", n)
        print("Computer - ", computer_points, "You - ", player_points, "Tie - ", tiepoints)
        continue
    elif (human == "w" and comp == "s") :
        computer_points += 1
        print("Computer choice - ", comp)
        print("Oops.. You lose !!")
        print("Chances Left = ", n)
        print("Computer - ", computer_points, "You - ", player_points, "Tie - ", tiepoints)
        continue
    elif (human == "w" and comp == "g") :
        player_points+=1
        print("Computer choice - ", comp)
        print("Congrats.. You win !!")
        print("Chances Left = ", n)
        print("Computer - ", computer_points, "You - ", player_points, "Tie - ", tiepoints)
        continue
    elif (human == "g" and comp == "s"):
        player_points += 1
        print("Computer choice - ", comp)
        print("Congrats.. You win !!")
        print("Chances Left = ", n)
        print("Computer - ", computer_points, "You - ", player_points, "Tie - ", tiepoints)
        continue
    elif (human == "g" and comp == "w"):
        computer_points += 1
        print("Computer choice - ", comp)
        print("Oops.. You lose !!")
        print("Chances Left = ", n)
        print("Computer - ", computer_points, "You - ", player_points, "Tie - ", tiepoints)
        continue
print("\n!!!!! GAME OVER !!!!!!")
if(computer_points > player_points) :
    print("You lose by " , computer_points-player_points, "points")
elif(computer_points == player_points):
    print("Game Tied !!")
else:
    print("You win by" , player_points-computer_points , " points")

