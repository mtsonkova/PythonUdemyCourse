# gobal scope
x = "global x"


def outer_function():
    # enclosing scope
    x = "enclosing x"

    def inner_function():
        # local scope
        x = "local x"
        print(x)  # This will print "local x"
    inner_function()
    print(x)  # This will print "enclosing x"


outer_function()
print(x)  # This will print "global x"

# Using 'nonlocal' to modify enclosing scope variable


def outer_function_nonlocal():
    x = "enclosing x"

    def inner_function():
        nonlocal x
        x = "modified enclosing x"
        print(x)  # This will print "modified enclosing x"
    inner_function()
    print(x)  # This will print "modified enclosing x"


outer_function_nonlocal()

# Using 'global' to modify global scope variable


def modify_global():
    global x
    x = "modified global x"
    print(x)  # This will print "modified global x"


modify_global()
print(x)  # This will print "modified global x"
# Using 'global' to modify global scope variable
y = "global y"


def modify_global_y():
    global y
    y = "modified global y"
    print(y)  # This will print "modified global y"


modify_global_y()
print(y)  # This will print "modified global y"
