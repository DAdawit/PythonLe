# Closure is a function having accesss to the scope of its parent function after the parent function has returned


def paren_function(person, coins):
    # coins = 3

    def play_game():
        # The nonlocal keyword is used in nested functions to declare that a variable refers to a variable in the nearest enclosing scope that is not global. This allows you to modify a variable defined in an outer function from within an inner function.
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n " + person +" has " + str(coins) + " coins left")
        elif coins == 1:
            print("\n " + person +" has " + str(coins) + " coins left")
        else:
            print("\n" + person +" is out of coins")
    return play_game

tommy  = paren_function("Tommy", 2)
jerry  = paren_function("Jerry", 5)
tommy()
tommy()

jerry()
jerry()
jerry()
jerry()
