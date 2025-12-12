# set is unordered collection of unique items
# sets are mutable, but items in a set must be immutable (strings, numbers, tuples)
# sets are defined using curly braces {} or the set() function  
my_set = {1, 2, 3, "Hello", 3.14}
print(my_set)  # Output the entire set (order may vary)
print(2 in my_set)  # Checking if an item exists in the set (Output) : True
my_set.add("World")  # Adding an item to the set
print(my_set)  # Output the updated set
my_set.remove(2)  # Removing an item from the set (raises KeyError if item not found)
print(my_set)  # Output the updated set
my_set.discard(10)  # Removing an item that may not exist (no error if item not found)
print(my_set)  # Output the updated set
# set methods
another_set = {3, 4, 5, "Hello"}
print(my_set.union(another_set))  # Output: union of two sets
print(my_set.intersection(another_set))  # Output: intersection of two sets
print(my_set.difference(another_set))  # Output: items in my_set but not in another_set
print(my_set.symmetric_difference(another_set))  # Output: items in either set but not in both
my_set.clear()  # Clears all items in the set
print(my_set)  # Output: set() (empty set)
my_set2 = set([1, 2, 2, 3, 4, 4])  # Creating a set from a list (duplicates removed)
print(my_set2)  # Output: {1, 2, 3, 4}
print(len(my_set2))  # Output: 4 (number of unique items in the set)    


my_list = [1, 2, 2, 3, 4, 4]
unique_set = set(my_list)  # Converting list to set to remove duplicates
print(unique_set)  # Output: {1, 2, 3, 4}
print(1 in unique_set)  # Output: True (checking if value exists)
unique_set.add(5)  # Adding a new item
print(my_set.difference(unique_set))  # Output: items in my_set but not in unique_set
my_set.update([6, 7, 8])  # Adding multiple items to the set
print(my_set)  # Output the updated set 
my_set.discard(8) # Removing an item 
print(my_set)  # Output the updated set

print(my_set.isdisjoint(unique_set))  # Output: True if sets have no items in common
print(my_set.issubset(unique_set))  # Output: True if my_set is a subset of unique_set
print(my_set.issuperset(unique_set))  # Output: True if my_set is a superset of unique_set      
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.intersection_update(set_b)  # Updates set_a to the intersection of set_a and set_b
print(set_a)  # Output: {3}
set_b.difference_update({3})  # Removes items in the given set from set_b
print(set_b)  # Output: {4, 5}      
set_c = {1, 2, 3}
set_d = {4, 5, 6}
set_c.update(set_d)  # Adds items from set_d to set_c
print(set_c)  # Output: {1, 2, 3, 4