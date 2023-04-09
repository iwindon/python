"""A set of classes that can be used to represent gas cars."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You must enter a positive number to increment the odometer.")

    def fill_gas_tank(self):
        """Print a statement describing the gas tank."""
        print("This car has a gas tank.")

