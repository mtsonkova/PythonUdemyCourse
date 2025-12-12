def say_hello():
    print("Hello!") 

say_hello()


def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Function with parameters and return value
def perform_calculation(operation, a, b ):
    result = 0

    if(operation == "add"):
        result =  a + b    # Future operations can be added here
    elif(operation == "subtract"):
        result =  a - b
    elif(operation == "multiply"):
        result =  a * b
    elif(operation == "divide"):
        if b != 0:
            result =  a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"
    
    return result

# Example usage positional arguments because the position of the arguments matters
print(perform_calculation("add", 5, 3))        # Output: 8
print(perform_calculation("subtract", 10, 4))  # Output: 6
print(perform_calculation("multiply", 2, 3))   # Output: 6
print(perform_calculation("divide", 8, 2))     # Output: 4.0
print(perform_calculation("divide", 8, 0))     # Output: Error: Division by zero
print(perform_calculation("modulus", 8, 2))    # Output: Error: Unknown operation

# Example usage with keyword arguments
keyword_result = perform_calculation(operation="add", a=7, b=2)


# difference between functions and methods

def to_uppercase(string):
    return string.upper()
print(to_uppercase("hello"))  # Output: HELLO
my_string = "hello"
print(my_string.upper())       # Output: HELLO
print(keyword_result)          # Output: 9

# methods are functions that are associated with objects. In the example above, upper() is a method of the string object my_string. 
