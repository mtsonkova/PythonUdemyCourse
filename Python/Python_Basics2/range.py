# range
# The range() function generates a sequence of numbers. 
# It is commonly used in for loops to iterate over a sequence of numbers.
# Syntax: range(start, stop, step)
# - start: The starting value of the sequence (inclusive). Default is 0.
# - stop: The ending value of the sequence (exclusive).
# - step: The difference between each number in the sequence. Default is 1.
# Examples:
# Generate numbers from 0 to 4
for i in range(5):
    print(i)
# Generate numbers from 2 to 6
for i in range(2, 7):
    print(i)
# Generate even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Generate numbers from 10 to 1 in reverse order
for i in range(10, 0, -1):
    print(i)
# Generate numbers from 1 to 10