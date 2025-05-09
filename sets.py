# sets
nums = {1, 2, 3, 4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
# no duplicates allowed
nums = {1, 2, 2, 3}
print(nums)
# true is a dupe of 1, false is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)
# check if a value is in a set
print(2 in nums)
# but you cannot refer to an element in the set with an index position or a key
# add a new element to a set
nums.add(8)
print(nums)
# add elements from one set to another
moreNums = {5, 6, 7}
nums.update(moreNums)
print(nums)
# you can use update with lists, tuples and dictionaries too
# merge two sets to create a  new set
one = {1, 2, 3}
two = {5, 6, 7}
myNewSet = one.union(two)
print(myNewSet)
# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)
# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)