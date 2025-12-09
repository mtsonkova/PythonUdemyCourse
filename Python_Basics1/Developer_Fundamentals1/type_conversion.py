print(str(100))          # Convert integer to string
print(type(str(100)))

print(type(int(str(100))))  # Convert string back to integer


birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print(f'Your age is: {age}')