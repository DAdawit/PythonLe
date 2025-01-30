
import random
import sys


def gs(name):
    playerWins = 0
    computerWins = 0
    gameCount = 0

    def playGs():
        nonlocal playerWins
        nonlocal computerWins
        nonlocal name
        computer = random.choice("123")
        print(computer)
        playerGuss =input(f"\n{name}  guss which number i'am thinking ... of ? 1, 2, or 3 \n")

        if playerGuss not in ["1", "2","3"]:
            print(f"{name} You must enter number between ... 1, 2, or 3")
            return playGs()
        
        player = int(playerGuss)
        computer = random.choice("123")
        # print(computer)
        
        print(f"\n{name} you choose {player}")
        print(f"Computer choose {computer}")

        def decideWinner(player, computer):
            nonlocal playerWins
            nonlocal computerWins
            nonlocal name

            if int(player) == int(computer):
                playerWins += 1
                return f"🎉 {name} you win!"
            elif int(player) != int(computer):
                computerWins += 1
                return f"computer wins"
        
        game_result = decideWinner(player,computer)
        print(game_result)     

        nonlocal gameCount
        gameCount +=1
        print(f"\nGame count: {str(gameCount)}")
        print(f"\n{name} count: {str(playerWins)}")
        print(f"\nComputer wins: {str(computerWins)}")
        
        print("\nPlay again ?")

        while True:
            playagain = input("Y for yes, Q for quite ?")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
               break

        if playagain.lower() == "y":
            return playGs()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"{name} Thank you for playing!\n")
            sys.exit("Bye! 👋")
        
        # print(name)
        # print(playerGuss)
    return playGs
if __name__ =="__main__":
    import argparse
    parser  = argparse.ArgumentParser(
        description="personalized Gussing number game"
    )

    parser.add_argument("-n","--name", metavar="name", required=True, help="Name of the player")

    args= parser.parse_args()
    gussNumber = gs(args.name)
    gussNumber()