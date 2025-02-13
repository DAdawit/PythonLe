def hello(name, lang):
    languages ={
        "english":"Hello",
        "spanish":"Holla",
        "germany":"Hallo"
    }
    msg =f"{languages[lang] } {name}"
    print(msg)



if __name__ =="__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )


    parser.add_argument("-n", "--name", metavar="name",required=True, help="The name of the person to greet")
    parser.add_argument("-l", "--lang", metavar="language", choices=["english","spanish","germany"],required=True, help="The language of greeting")

    args = parser.parse_args()
    hello(name=args.name, lang=args.lang)
