# Example of a for loop in Python

for i in range(5):
    print("Iteration:", i)


for letter in "Python":
    print("Letter:", letter)

for item in ["apple", "banana", "cherry"]:
    print("Fruit:", item)

for number in (1, 2, 3, 4, 5): # tuple
    print("Number:", number)    

for data in {10, 20, 30}: # set
    print("set data", data)    


user = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

for key in user:
    print(f"{key}: {user[key]}")


for key, value in user.items():
    print(f"{key}: {value}")    
