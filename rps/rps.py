import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS = 3

# print(RPS(1))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# # sys.exit()

print("")
winMessage = "You win!"
losMessage = "You lose!"
playerchoice = input("Enter ... \n1 for Rock , \n2 for Paper, \n3 for Scissors:\n\n")
player=int(playerchoice)

if player < 1 or player> 3:
    sys.exit("you must enter 1, 2, or 3")

computer = random.choice("123")
computer = int(computer)

print("")
print("Your chose " + str(RPS(player).name) +".")
print("computer choice " + str(RPS(computer).name) + ".")

if player == 1 and computer == 3:
    print("🥳 "+winMessage)
elif player == 2 and computer == 1:
    print("🥳 "+winMessage)
elif player == 3 and computer == 2:
    print("🥳 "+winMessage)
elif player == int(computer):
    print("😲 Tie game!")
else :
    print("😭 "+losMessage)