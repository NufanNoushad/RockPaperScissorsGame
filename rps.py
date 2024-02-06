# Rock Paper Scissors Game

import sys
import random #the random module which allows you to generate random numbers.

from enum import Enum 

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
print("")
playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1,2 or 3.")
    
computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

# Who won system

if player == 1 and computerchoice == 3:
    print("🎉You win!")
elif player == 2 and computerchoice == 1:
    print("You win!")
elif player == 3 and computerchoice == 2:
    print("You win!")
elif player == computer:
    print("🤯It is a tie!")
else:
    print("🐍Python won!")
