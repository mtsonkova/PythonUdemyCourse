# private variables in python
class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self._price = price  # private variable

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Price must be positive.")


# Example usage
my_car = Car("Toyota", "Camry", 2020, 24000)
# Accessing private variable via getter
print("Car Price:", my_car.get_price())

my_car.set_price(22000)  # Modifying private variable via setter
print("Updated Car Price:", my_car.get_price())
