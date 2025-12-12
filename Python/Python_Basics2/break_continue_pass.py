# break, contunue, pass
for letter in "Python":
    if letter == "h":
        break
    print("Letter:", letter)    

for letter in "Python":
    if letter == "h":
        continue # skips the current iteration, will not print the letter h
    print("Letter:", letter)    

for letter in "Python":
    if letter == "h":
        pass    # passes to the next iteration
    print("Letter:", letter)    