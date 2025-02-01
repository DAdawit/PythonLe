

import random


name = "name 1"

stud ={
    "name":"kasu",
    "age":25,
    }

jocks = [
    "Tom Brady",
    "Michael Jordan",
    "Serena Williams",
    "Cristiano Ronaldo",
    "Dwayne 'The Rock' Johnson"
]

print(f"module name {__name__}")

def sayHello():
    randJock = int(random.choice("01234"))
    # print(int(randJock))
    print(jocks[randJock])


if __name__ == "__main__":
    sayHello();
