user={
    "name":"kasu",
    "age":30,
    "married":False,
}

user2= dict(name="girma", age=30,married=True)

print(user)
print(user2)
print(type(user2))
print(len(user2))

# print
print(user['age'])
print(user.get('name'))
# list of keys
print(user.keys())
print(user.values())


# list of key/value pairs as tuples

print(user.items())

print("name" in user)
print("sex" in user)

# change values 

user["age"]=25
user.update({"name":"Girma"})

print(user)

# remove items 

print(user.pop("age"))

print(user)

user["position"]="ceo"
print(user.popitem())
print(user)

# delete item
user["position"]="ceo"
del user["position"]

print(user)

# clear
user2.clear()
print(user2)
del user2

# print(user2)

# copy dictionaries

user3= user # create a reference bad copy 

user3["name"]="david"
print(user3)
print(user)

user4= user.copy()
user5 =dict(user)
print(user5)




































