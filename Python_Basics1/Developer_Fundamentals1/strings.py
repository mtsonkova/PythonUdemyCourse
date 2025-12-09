text1 = 'hi'
text2 = "hello"
print(text1)
print(type(text2))

long_text = '''This is a long text that spans multiple lines.
It can contain 'single quotes' and "double quotes" without any issues.'''
print(long_text)
print(type(long_text))

# String concatenation
greeting = text1 + ' ' + text2 + '!'
print(greeting)     

text = "The quick brown fox jumps over the lazy dog."
print(text)
print(len(text))  # Length of the string    
print(text[10])    # Character at index 10
print(text[4:9])   # Substring from index 4 to 8
print(text.lower())  # Convert to lowercase
print(text.upper())  # Convert to uppercase
print(text.replace('fox', 'cat'))  # Replace 'fox' with 'cat'
print('fox' in text)  # Check if 'fox' is in the string 
print(text.split(' '))  # Split the string into a list of words
print(text.find('brown'))  # Find the index of substring 'brown'
print(text.count('o'))  # Count occurrences of 'o'
print(text.startswith('The'))  # Check if text starts with 'The'
print(text.endswith('dog.'))  # Check if text ends with 'dog.'
print(text.index('jumps'))  # Get index of substring 'jumps'
print(text.isalpha())  # Check if all characters are alphabetic
print(text.isdigit())  # Check if all characters are digits
print(text.isspace())  # Check if all characters are whitespace
print(text.capitalize())  # Capitalize the first character
print(text.title())  # Title case the string
print(text.center(50))  # Center the text within 50 characters
print(text.ljust(50))  # Left justify the text within 50 characters
print(text.rjust(50))  # Right justify the text within 50 characters   
print(text.strip())  # Remove leading and trailing whitespace   

print(text[0:8:2])  # Slicing with step of 2 also called step over
print(text[::-1])  # Reverse the string  In python negative index means start from end
print(text.replace(' ', '_').upper())  # Replace spaces with underscores and convert to uppercase   
print(f'The length of the text is {len(text)} characters.')  # Using f-strings to include variable in string
print("The length of the text is {} characters.".format(len(text)))  # Using format method to include variable in string
print("The length of the text is %d characters." % len(text))  # Using old-style formatting to include variable in string
print(text.encode('utf-8'))  # Encode the string to bytes using UTF-8
print(text.partition('jumps'))  # Partition the string at the first occurrence of 'jumps'
print(text.rpartition('the'))  # Partition the string at the last occurrence of 'the'
print(text.zfill(60))  # Pad the string with zeros on the left to make it 60 characters long

# Strings in Python are immutable, so the following line would raise an error
# text[0] = 'T'  # Uncommenting this line will cause an error

