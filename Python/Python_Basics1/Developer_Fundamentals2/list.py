numbers = [1, 2, 3, 4, 5]
mixedValues = [1, "two", 3.0, True, None]   
print("Numbers List:", numbers)
print("Mixed Values List:", mixedValues)

# lists are like arrays in other programming languages
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)   

# Accessing elements
first_fruit = fruits[0]
print("First Fruit:", first_fruit)      

# Modifying elements
fruits[1] = "blueberry"
print("Modified Fruits List:", fruits)  
# Adding elements
fruits.append("date")
print("Fruits List after append:", fruits)      
fruits.insert(1, "avocado")
print("Fruits List after insert:", fruits)  
# Removing elements
fruits.remove("cherry")
print("Fruits List after remove:", fruits)
popped_fruit = fruits.pop()
print("Popped Fruit:", popped_fruit)
print("Fruits List after pop:", fruits)
# List operations
more_fruits = ["elderberry", "fig", "grape"]
all_fruits = fruits + more_fruits
print("All Fruits List:", all_fruits)
repeated_fruits = fruits * 2
print("Repeated Fruits List:", repeated_fruits)
# List methods
fruits.sort()
print("Sorted Fruits List:", fruits)
fruits.reverse()
print("Reversed Fruits List:", fruits)
count_apples = fruits.count("apple")
print("Count of Apples:", count_apples)
index_of_avocado = fruits.index("avocado")
print("Index of Avocado:", index_of_avocado)
# Slicing -> it creates a new list from the existing list
some_fruits = all_fruits[1:4]
print("Sliced Fruits List (1 to 4):", some_fruits)
first_three_fruits = all_fruits[:3]
print("First Three Fruits:", first_three_fruits)
last_two_fruits = all_fruits[-2:]
print("Last Two Fruits:", last_two_fruits)
# List comprehension
squared_numbers = [x**2 for x in numbers]
print("Squared Numbers:", squared_numbers)
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

fruits.extend(["kiwi", "lemon", "mango"])
print("Fruits List after extend:", fruits)


print("banana" in fruits)  # True
print("orange" not in fruits)  # True

list_unpacking = ["red", "green", "blue", "yellow", "purple"]
r, g, b, *other = list_unpacking
print("Red:", r)
print("Green:", g)
print("Blue:", b)
print("Other Colors:", other)
# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("First Row of Matrix:", matrix[0])
print("Element at Row 0, Column 2:", matrix[0][2])  
