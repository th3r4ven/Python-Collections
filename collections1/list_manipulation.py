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
