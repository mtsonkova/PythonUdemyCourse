# inheritance
class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def sign_in(self):
        print("User signed in")


class Wizard(User):
    def __init__(self, name, power):
        super().__init__(name + "@game.com", "defaultpassword")
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} attacks with power {self.power}")


class Archer(User):
    def __init__(self, name, arrows):
        super().__init__(name + "@game.com", "defaultpassword")
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"{self.name} attacks with {self.arrows} arrows")


# Example usage
wizard1 = Wizard("Gandalf", 50)
archer1 = Archer("Legolas", 100)
wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack()


# Check if instnace is of a class
print(isinstance(wizard1, User))  # True
print(isinstance(archer1, Wizard))  # False
# Check subclass relationship
print(issubclass(Wizard, User))  # True
print(issubclass(Archer, Wizard))  # False
print(issubclass(Archer, User))  # True
