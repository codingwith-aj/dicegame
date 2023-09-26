import random
import time

#CREATES TWO DICE WITH SIX SIDES
dice1 = ["1", "2", "3", "4", "5", "6"]
dice2 = ["1", "2", "3", "4", "5", "6"]

P1score = 0
P2score = 0
Player1 = 5
Player2 = 5

Pin = "8544"

#MENU
def menu():
    global name_Player1
    global name_Player2
    print ("WELCOME TO THE GAME")
    print ("")
    choice()
    
def choice():
    choice = input("""
            A: Start Game
            B: High Scores
            C: Exit

            Please enter your choice: """)
    if choice == "A" or choice =="a":
        game()
    elif choice == "B" or choice =="b":
        gameOver()
    elif choice == "C" or choice =="c":
        exit()
    else:
        print("You must only select either A,B or C.")
        print("Please try again")
        menu()

        
authentication = input("Input PIN: ")
if authentication == Pin:
    print ("")
    name_Player1 = input("Enter name Player 1: ")
    print ("")
    name_Player2 = input("Enter name Player 2: ")
    print ("")
    print("The game will start in....")
    time.sleep(0.5)
    print("5")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    menu()
else:
    game()

def firstPlayer():
    global P1score
    global Player1   
    start = input ("Player 1, please press enter to roll the dice: ")
    firstRoll = random.choice(dice1)
    print (firstRoll)
    secondRoll = random.choice(dice2)
    print (secondRoll)
    if firstRoll == secondRoll:
        Player1 = Player1 + 1
    firstScore = int(firstRoll) + int(secondRoll)
    print (firstScore)
    P1score = P1score + firstScore
    Player1 = Player1 - 1
    if P1score % 2 == 0:
                P1score = P1score + 10
    elif P1score % 2 != 0:
                P1score = P1score - 5
    if Player2 > 0:
        secondPlayer()
    elif Player1 > 0:
        firstPlayer()
    print ("")
    print ("")


def secondPlayer():
    global P2score
    global Player2
    start = input ("Player 2, please press enter to roll the dice: ")
    firstRoll = random.choice(dice1)
    print (firstRoll)
    secondRoll = random.choice(dice2)
    print (secondRoll)
    if firstRoll == secondRoll:
        Player2 = Player2 + 1
    firstScore = int(firstRoll) + int(secondRoll)
    print (firstScore)
    P2score = P2score + firstScore
    Player2 = Player2 - 1
    print ("")
    if P2score % 2 == 0:
                P2score = P2score + 10
    elif P2score % 2 != 0:
                P2score = P2score - 5
    print ("")
    game()


def gameOver():
    name = name_Player1
    string = name_Player1.upper() + " - "  + str(P1score) + "\n"
    myFile = open("scores.txt" , "a")
    myFile.write(string)
    myFile.close()
menu()


#GAME
def game():
    if Player1 > 0:
        firstPlayer()
    if Player2 > 0: 
        secondPlayer()
    if P1score == P2score:
        Player1 = Player1 + 1
        Player2 = Player2 + 1
    else:
        gameOver()

    

#HIGH SCORE
def score():
    scores = []
    myFile = open("scores.txt" , "r")
    for line in myFile.readlines():
        line = line.strip()
        scores.append(line)
        scores.sort(reverse=True)
        for i in range(0,5):
            try:
                print (scores[i])
            except:
                continue
            menu()

print (name_Player1 + " score is " + str(P1Score))
print (name_Palyer2 + " score is " + str(P2score))



