# constructer
mytuple = tuple(('dave',1,True))

anothertuple = (1,2,3,4,5)

print(type(mytuple))
print(type(anothertuple))

newlist=list(mytuple)

newlist.append('kasu')
newtuples=tuple(newlist)

print(newlist)
print(anothertuple)

# unpacking tupeles

(one,*two,three)=anothertuple

print(one)
print(two)
print(three)

print(newtuples.count)
print(newlist.index('kasu'))