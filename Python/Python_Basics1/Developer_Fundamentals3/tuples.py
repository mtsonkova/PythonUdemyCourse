# tuple -> like lists but immutable (cannot be changed after creation)
# faster than lists due to immutability
# tuples use parentheses () instead of square brackets []
# tuples can store multiple data types
# tuples are ordered and allow duplicate values

my_tuple = (1, "Hello", 3.14, True, "Hello")
print(my_tuple)  # Output the entire tuple
print(my_tuple[1])  # Accessing an element by index (Output: Hello)
print(my_tuple.count("Hello"))  # Count occurrences of a value (Output: 2)
print(my_tuple.index(3.14))  # Find index of a value (Output: 2)

new_tuple = my_tuple[1:4]  # Slicing a tuple
print(new_tuple)  # Output: ('Hello', 3.14, True)   

x, y, z, *others = my_tuple  # Unpacking a tuple
print(x)  # Output: 1
print(y)  # Output: Hello
print(others)  # Output: [3.14, True, 'Hello']  
print(my_tuple.count("Hello"))  # Output: 2
print (len(my_tuple))  # Output: 5 (number of elements in the tuple)
print("Hello" in my_tuple)  # Output: True (checking if value exists)
print(my_tuple.index("Hello")) 