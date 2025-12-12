# abstraction
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Demonstration of Abstraction
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!

# Abstraction is the concept of hiding complex implementation details and showing only the necessary parts of an
# object. It allows us to focus on interactions at a higher level without needing to understand all the underlying complexities.
# In this example, the Animal class is an abstract base class that defines an abstract method make_sound.
# The Dog and Cat classes inherit from Animal and provide concrete implementations of the make_sound method
# without exposing the details of how the sound is produced.
# This allows users of the Dog and Cat classes to interact with them through the make_sound method without needing to know the specifics of each animal's sound production mechanism.
# Abstraction helps in reducing complexity and increasing efficiency by allowing programmers to work at a higher level of understanding. object. It allows us to focus on interactions at a higher level without needing to understand all the underlying complexities.
# In this example, the Animal class is an abstract base class that defines an abstract method make_sound.
# The Dog and Cat classes inherit from Animal and provide concrete implementations of the make_sound method
# without exposing the details of how the sound is produced.
# This allows users of the Dog and Cat classes to interact with them through the make_sound method without needing to know the specifics of each animal's sound production mechanism.
# Abstraction helps in reducing complexity and increasing efficiency by allowing programmers to work at a higher level of understanding.
