class JustNotCoolError(Exception):
    pass


x=5

try:
    raise JustNotCoolError("I just raised an exception")
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("only strings are allowed")
except NameError:
    print("Something went wrong")
except ZeroDivisionError:
    print("You can't divide by zero")
except Exception as error:
    print(error)
else:
    print("Everything is fine")
finally:
    print("I always run")