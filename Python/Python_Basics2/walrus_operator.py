# walrus operator example   :=
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []   
for n in numbers:
    if (half := n / 2) > 4:
        even_numbers.append(n)  
print("Even numbers greater than 8 when halved:", even_numbers)  # Output: [9, 10]
print("Halved values greater than 4:", [n / 2 for n in even_numbers])  # Output: [4.5, 5.0]
