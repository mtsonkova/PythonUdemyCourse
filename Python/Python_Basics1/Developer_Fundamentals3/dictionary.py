# Dictionary Example => unordered key-value pairs
# Dictionaries are mutable and can store various data types
# We can have dictionaries within dictionaries or dictionaries within lists
# Dictionaries look similar to JSON objects
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Dictionary's keys must be unique and immutable (strings, numbers, tuples)
# Values can be of any data type and can be duplicated
data["email"] = "randomuseremail@example.com"  # Adding a new key-value pair
data["age"] = 31  # Updating an existing key's value    
print(data)  # Output the entire dictionary
print(data["name"])  # Accessing a value by its key
# Removing a key-value pair
del data["city"]
print(data) 

# dictionary methods
data.clear()  # Clears all items in the dictionary
print(data)  # Output: {}   
data2 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(data2.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(data2.values())  # Output: dict_values(['Alice', 30, 'New York
print(data2.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])])
print(data2.get("age"), 32)  # Output: 30 (default value not used)
print(data2.pop("city"))  # Output: New York
print(data2)  # Output: {'name': 'Alice', 'age': 30}
print(data2.update({"city": "Washington"}))  # (updates a value)


data3 = dict(name="Bob", age=25, city="Los Angeles")  # Creating a dictionary using dict()
print(data3)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}   
print(len(data3))  # Output: 2 (number of key-value pairs)

print("name" in data3)  # Output: True (checking if key exists)
print("age" in data3.keys())  # Output: True (checking if key exists using keys() method)
print(25 in data3.values())  # Output: True (checking if value exists using values() method)

print(data3.items())  # Output: dict_items([('name', 'Bob'), ('age', 25), ('city', 'Los Angeles')]) Prints a tuple of key-value pairs

data4 = data3.copy()  # Creating a shallow copy of the dictionary, points to the same memory location
print(data4)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
data4["age"] = 26  # Modifying the copy
print(data3)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'} Original remains unchanged
print(data4)  # Output: {'name': 'Bob', 'age': 26, 'city': 'Los Angeles'} Copy reflects the change