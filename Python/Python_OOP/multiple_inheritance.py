# multiple inheritance.py
class Flyer:
    def fly(self):
        print("Flying")


class Swimmer:
    def swim(self):
        print("Swimming")


class FlyingFish(Flyer, Swimmer):
    def glide(self):
        print("Gliding above water")


# Example usage
flying_fish = FlyingFish()
flying_fish.fly()      # Output: Flying
flying_fish.swim()     # Output: Swimming
flying_fish.glide()    # Output: Gliding above water
# Checking isinstance
print(isinstance(flying_fish, Flyer))   # True
print(isinstance(flying_fish, Swimmer))  # True
print(isinstance(flying_fish, FlyingFish))  # True
# Checking subclass relationship
print(issubclass(FlyingFish, Flyer))    # True
print(issubclass(FlyingFish, Swimmer))   # True
print(issubclass(Flyer, Swimmer))        # False
print(issubclass(Swimmer, Flyer))        # False
