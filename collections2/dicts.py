# Dicts is build by key and value, like a list but with keys
# and different from tuples, it can have its values changed

random_dict = {
    "key1": 1212,
    "key2": 1938,
    "key3": 'asdasd',
    "key4": 19283,
}

# To access dict values, you can use the function .get("key", 0)
# this 0 is what will return if the key was not found

print(random_dict.get("key4", 0))

# or you can access directly by key

print(random_dict["key1"])

# You can validate if the keys exists using in

print("key2" in random_dict)  # True
print("key20" in random_dict)  # False

# You can use for too, and you have a lot of other functions with it
# .keys(), .values(), .items()

print("########")

for element in random_dict.keys():
    print(element)

print("########")

for element in random_dict.values():
    print(element)

print("########")

for element in random_dict.keys():
    print(f'Key: {element}, value: {random_dict[element]}')

print("########")

for element in random_dict.items():
    print(element)  # Return tuple

print("########")