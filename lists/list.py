users = ['foo', 'bar', 'baz']
data =['magna', 'break', 'gite']
print(users.index('bar'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])
print(len(users))

print('foo' in users)


# addin item to  list

users+= ['girma', 'kasu', 'gite']

print(users)

users.extend(data)
print(users)

users.insert(0,"david")

print(users)


users[2:2]=['master','girma']

# doesn't touch the last index
print(users)
users[1:3] =['faraw','melata']

print(users)


users.remove("david")

print(users)

users.pop()

print(users)

del users[1:3]

print(users)

data.clear()

print(data)

users[1:2]='john'
users.sort(key=str.lower)

# users.sort(reverse=True)
print(users)


nums =[4,84,36,1,25,5,19]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)



# copying lists

numcopy= nums.copy()
mynums= list(nums)
mycopy =nums[:]

print(numcopy)
mycopy.sort()
print(mynums)
print(mycopy)
print(type(numcopy))