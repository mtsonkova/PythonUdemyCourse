class PlayerCharacter:
    def __init__(self, name="anonymous", health=30, strength=50):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, other):
        if not isinstance(other, PlayerCharacter):
            raise ValueError("Can only attack another PlayerCharacter")
        damage = self.strength
        other.health -= damage
        return f"{self.name} attacks {other.name} for {damage} damage!"

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"PlayerCharacter(name={self.name}, health={self.health}, strength={self.strength})"

# Class Method Example -> it can be called without creating instance of the class
    @classmethod
    def from_dict(cls, info):
        return cls(name=info.get("name", "anonymous"),
                   health=info.get("health", 30),
                   strength=info.get("strength", 50))

# static method example -> it does not access or modify class or instance state
    @staticmethod
    def game_rules():
        return "Players can attack each other until one player's health drops to zero."


# OOP Concepts Demonstration
# We can create objects that have their own methods and attributes
player1 = PlayerCharacter("Hero", 100, 15)
player2 = PlayerCharacter("Villain", 80, 10)
print(player1)
print(player2)
print(player1.attack(player2))
print(f"Is {player2.name} alive? {'Yes' if player2.is_alive() else 'No'}")

# OOP allows us to write efficient and reusable code by encapsulating data and behavior within classes.

# Attributes are pieces of data that are dynamic and they are unique to each object.
# Methods are functions that belong to the object and can manipulate its attributes or perform actions.
# Objects are instances of classes that encapsulate both data (attributes) and behavior (methods).
# Classes are blueprints for creating objects, defining their attributes and methods.
# Encapsulation is the concept of bundling data and methods that operate on that data within one unit, i.e., a class.
# Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.
# Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.
# Abstraction is the concept of hiding complex implementation details and showing only the necessary parts of an object.
# These concepts help in organizing code, making it more modular, maintainable, and scalable.
# OOP (Object-Oriented Programming) is a programming paradigm that uses "objects" to represent data and methods to manipulate that data.
# It focuses on the principles of encapsulation, inheritance, polymorphism, and abstraction to create modular and reusable code.
# This allows for better organization of code, easier maintenance, and the ability to model real-world entities more effectively.


# Class Object Attributes and Methods:
print(f"Class Name: {PlayerCharacter.__name__}")
print(f"Class Documentation: {PlayerCharacter.__doc__}")
print(f"Class Module: {PlayerCharacter.__module__}")
print(f"Class Bases: {PlayerCharacter.__bases__}")
print(f"Class Dictionary: {PlayerCharacter.__dict__}")
# These attributes and methods provide metadata about the class itself, such as its name, documentation, module, base classes, and the class's namespace dictionary.
# Class Object Attributes are static properties that belong to the class itself rather than any instance of the class.
# They provide metadata about the class, such as its name, documentation, module, base classes, and the class's namespace dictionary.
# Class Object Methods are functions that are defined within the class and can be called on the class itself rather than on instances of the class.
# They often provide functionality related to the class as a whole, such as creating instances or performing operations that are not specific to any single instance.
# Examples of Class Object Methods include class methods (defined with @classmethod) and static methods (defined with @staticmethod).
