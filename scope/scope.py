


name = 	"kasu"
count = 2

def another():
    color =	"blue"
    # this count will be a new count variable that will not affect the global count
    global count
    count = count + 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("David")

another()