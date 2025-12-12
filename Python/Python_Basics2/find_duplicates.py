some_list = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'c', 'g']

duplicates = []  

for value in some_list:
    if some_list.count(value) > 1 and value not in duplicates:
        duplicates.append(value)    
print(duplicates)
