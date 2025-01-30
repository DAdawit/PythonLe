
def gs(name):
    print(name)

if __name =="__main__":
    import argparse
    parser  = argparse.ArgumentParser(
        description="personalized Gussing number game"
    )

    parser.add_argument("-","-name", metavar="name", required=True, help="Name of the player")

    args= parser.parse_args()
    gussNumber = gs(args.name)
    gussNumber()