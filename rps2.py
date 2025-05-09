import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playAgain = True

while playAgain:
    playerChoice = input("\nenter a value: 1 for rock,\n2 for paper, or\n3 for scissors:\n\n")
    player = int(playerChoice)

    if player<1 or player>3:
        sys.exit("you must enter 1, 2 or 3.")

    computerChoice = random.choice("123")
    computer = int(computerChoice)

    print("\nyou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("computer chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == 1 and computer == 3:
        print("🎉 you win!")
    elif player == 2 and computer == 1:
        print("🎉 you win!")
    elif player == 3 and computer == 2:
        print("🎉 you win!")
    elif player == computer:
        print("😲 tie game!")
    else:
        print("🐍 computer wins!")
    
    playAgain = input("\nplay again? \nY for yes or\nQ to quit\n\n")

    if playAgain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("thank you for playing!\n")
        playAgain = False

sys.exit("bye!, 👋")