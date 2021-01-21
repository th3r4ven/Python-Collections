
data_science_users = [21, 90, 88, 66]
machine_learning_users = [90, 56, 34, 88]

# To "join" this 2 lists in one, we can use set() function,
# and the values will not be duplicated

new_list = data_science_users.copy()
new_list.extend(machine_learning_users)

# Note that, at this momento the values are duplicated, so use set()

new_list = set(new_list)
print(new_list)  # Output {66, 56, 34, 21, 88, 90}

# Other option is already using {},
# if you do print(type({1,4,6,88,9,45})), this will output "set"


# Other example, join sets using pipe

data_science_users = {21, 90, 88, 66}
machine_learning_users = {90, 56, 34, 88}

new_list = data_science_users | machine_learning_users

print(new_list)  # Output {66, 56, 34, 21, 88, 90}

# Now we can get only the results that is on both lists using &

print(data_science_users & machine_learning_users)  # Output {88, 90}

# Other option: remove values from data_science_users
# that is in machine_learning_users

print(data_science_users - machine_learning_users)  # Output {66, 21}


