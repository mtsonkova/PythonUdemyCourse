# docstrings
def greet(name):
    """Greets a person with their name.
    
    Args:
        name (str): The name of the person to greet.
        
    Returns:
        None
    """
    print(f"Hello, {name}!")    
greet("Bob")
print(greet.__doc__)  # Accessing the docstring of the function 
