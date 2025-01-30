import sys
import challenge1
import rockPaperScissors

def PlayGame(name="playerOne"):
    # print(name)
    wellcomeBack= True
    
    while True:

        if wellcomeBack:
            print(f"\n{name}, welcome back to the Arcade menu.")

        userInput = input(f"what game do you want to play ? \n press 1 for Paper_Rock_Scissors \n press 2 for Guss the number \n Q for exit \n Your input : ")
       
        if userInput not in ["1","2","q"]:
            print("\nIncorrect input. choose from 1, 2, or Q")
            PlayGame(name)
    

        wellcomeBack = True

        if userInput =="1":
            rpsg= rockPaperScissors.rps(name)
            rpsg()
        elif userInput =="2":
            gussNumber= challenge1.gs(name)
            gussNumber()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"{name} Thank you for playing!\n")
            sys.exit("Bye! 👋")

 
if __name__ == "__main__":
    import argparse

    parser= argparse.ArgumentParser(description="Games archives")

    parser.add_argument("-n", "--name", metavar="name", required=True, help="Games archive enter your name to start e.g -n 'your name here'")

    args= parser.parse_args()
    
    PlayGame(args.name)