# lists
users = ['Dave', 'John', 'Sarah']
data = ['Dave', '42', True]
emptylist = []
print("Dave" in emptylist)
print(users[0])
print(users[-2])
print(users.index('Sarah'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])
print(len(data))
users.append('Elsa')
print(users)
users += ['Jason']
print(users)
users.extend(['Robert', 'Jimmy'])
print(users)
# users.extend(data)
# print(users)
users.insert(0, 'Bob')
print(users)
users[2:2] = ['Eddie', 'Alex']
print(users)
users[1:3] = ['Robert', 'JPJ']
print(users)
users.remove('Bob')
print(users)
print(users.pop())
print(users)
del users[0]
print(users)
# del data
data.clear()
print(data)
users[1:2] = ['dave']
users.sort()
print(users)
users.sort(key=str.lower)
print(users)
nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))
print(nums)
numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]
print(numsCopy)
print(myNums)
myCopy.sort()
print(myCopy)
print(nums)
print(type(nums))
myList = list([1, "Neil", True])
print(myList)