import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerChoice = input("enter a value: 1 for rock,\n2 for paper, or\n3 for scissors:\n\n")
player = int(playerChoice)

if player<1 or player>3:
    sys.exit("you must enter 1, 2 or 3.")

computerChoice = random.choice("123")
computer = int(computerChoice)

print("")
print("you chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("computer chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

if player == 1 and computer == 3:
    print("🥳 you win!")
elif player == 2 and computer == 1:
    print("🥳 you win!")
elif player == 3 and computer == 2:
    print("🥳 you win!")
elif player == computer:
    print("😲 tie game!")
else:
    print("🐍 computer wins!")