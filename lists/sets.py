nums={1,2,3,4,5,6,6,8,8 }
nums2 = set((5,6,7))

print(nums)
print(nums2)

print(type(nums))
print(type(nums2))

# Truu is a dupe of 1, False is a dup of 0

nums3={1,True, 2, False,3,4, 0}
print(nums3)

# check if a value is in a set

print(2 in nums3)
# but you can't refer to an element in he sett with an index position or a key

# Add a new element to the set

nums.add(10)
print(nums)

# Adddd elementt form on set another 

moreNums={11,12,13,14,15,16,17,18}
nums.update(moreNums)

print(nums)

# merge to set to create a new set 

one ={1,2,3}
two={5,6,7,8,9}
myNewset=one.union(two)
print(myNewset)

# keep only the duplicates
one ={1,2,3,5,6,7}
two={5,6,7,8}
one.intersection_update(two)
print(one)

# keep except the duplicates
one ={1,2,3,5,6,7}
two={5,6,7,8}
one.symmetric_difference_update(two)
print(one)


data1={1,2,3}
data2={2,3,4}

intersection=data1.intersection(data2) 
symmetric_diff=data1.symmetric_difference(data2) 

print(intersection)
print(symmetric_diff)
