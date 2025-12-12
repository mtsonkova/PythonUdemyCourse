# polymorphizm.py
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def animal_sound(animal):
    print(animal.speak())


# Example usage
dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
# Demonstrating polymorphism with a list of animals
animals = [Dog(), Cat()]
for animal in animals:
    animal_sound(animal)
# Output:
# Woof!
# Meow!
# Checking isinstance
print(isinstance(dog, Animal))  # True
print(isinstance(cat, Dog))     # False
# Checking subclass relationship
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))     # False
print(issubclass(Cat, Animal))   # True
