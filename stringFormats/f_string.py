

person  ="Dave"
coins = 3

print("\n" + person + " has "  + str(coins) + "coins left.")

format1 = "\n%s has %s coins left." %(person, coins)
print(format1)

format2 = "\n{} has {} coins left.".format(person, coins)
print(format2)

format3 = "\n{1} has {0} coins left.".format(coins, person)
print(format3)

format4 = "\n{person} has {coins} coins left.".format(coins =coins, person =person)
print(format4)


player ={
    "person": "Dave",
    "coins": 3
}

format5 = "\n{person} has {coins} coins left.".format(**player)
print(format5)











print("\n##### By using f-strings! This is the way #####")
#############################
# f-strings! This is the way

message = f"\n{person} has {coins} coins left."
print(message)


message = f"\n{person} has {coins*5} coins left."
print(message)


message = f"\n{person.lower()} has {coins} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

# you can pass formating options 
num = 10
print(f"\n2.58 times {num} is equal to {2.58 * num:.2f}")

for num in range(1,11):
    print(f"\n2.58 times {num} is equal to {2.58 * num:.2f}")

for num in range(1,11):
    print(f"\n{num} divided by 2.58 is equal to {2.58 / num:.2%}")


number = 1
print(f"\n{number} percent of by 1 is equal to {number / 1/100:.2%}")