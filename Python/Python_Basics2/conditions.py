is_old = True
is_licensed = True

if(is_licensed and is_old):
    print("You can drive a car")
elif(not is_old):
        print("You cannot drive a car")
elif(not is_licensed):
    print("You cannot drive a car")


# ternary operator
age = 22
is_adult = True if age >= 18 else False
print(is_adult)


is_friend = True
can_message = "Message allowed" if is_friend else "Message not allowed"
print(can_message)

# short circuiting
is_magician = False
is_expert = True    
if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You are a beginner magician")
else:
    print("You are not a magician") 


#  == vs is
a = [1, 2, 3]
b = a
print(a == b)  # True, because the values are the same => checks equality of values
print(a is b)  # True, because both refer to the same object in memory  => checks if it is the same object

