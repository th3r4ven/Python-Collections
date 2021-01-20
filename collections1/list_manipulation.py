# intro in lists

littleList = [23, 66, 454, 89, 2, 1, 45, 78, 10, 88]

# adding items at the end of the list
littleList.append(90)
littleList.append(66)
print(littleList)

# removing first time that the item appears (.remove)
littleList.remove(66)
print(littleList)

# inverting all list order
littleList.reverse()
print(littleList)

# check if and value is in the list and remove it

if 454 in littleList:  # this return True or False
    littleList.remove(454)

# remove all values from the list using .clear
littleList.clear()

# you can add a lot of values at the same time using .extends
littleList.extend([10, 11, 12, 13, 14, 15])
print(littleList)

# Adding values from littleList to another list
littleList2 = [(values + 1) for values in littleList]
print(littleList2)

newList = []
# using for with if on the same line
# [ (operation inside for) for values in littlelist2 (if validator) ]
[newList.append(values) for values in littleList2 if values > 14]
print(newList)


def function(List=None):
    if List is None:
        List = []
    print(len(List))
    List.append(13)


function()

# Other build-in function, starting with enumerate()

# Not using enumerate()

for i in range(len(littleList)):
    print(f'Index: {i} and Content: {littleList[i]}')

print(list(enumerate(littleList)))  # generate a list with tuples inside

for index, value in enumerate(littleList):  # Unpack tuples automatic
    print(index, value)

# Other example Unpacking tuples

users = [("Raven", 20, 2000), ("R4ven", 30, 1990), ("R4v3n", 40, 1980)]

for name, age, birth_year in users:
    print(name)

for _, _, birth_year in users:  # Unpacking and ignoring values that is not going to be used
    print(birth_year)

# sort and sorted build-in fuctions

print(sorted(littleList))  # This sorted your list but don't change permanently

# But if you use .sort(), this WILL change your list


# reversed function will reverse the list order,
# so you can combine with sort or sorted to get the reverse value
print(reversed(sorted(littleList)))
