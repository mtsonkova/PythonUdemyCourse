# *args and **kwargs
def perform_calculation(operation, a, b):
    result = 0

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b != 0:
            result = a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"

    return result   

# Example usage with *args
args = ("multiply", 4, 5)
print(perform_calculation(*args))  # Output: 20 

# Example usage with **kwargs
kwargs = {"operation": "subtract", "a": 15, "b": 5
}
print(perform_calculation(**kwargs))  # Output: 10  
