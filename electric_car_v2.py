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

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75) -> None:
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year) -> None:
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def self_driving(self):
        """Print a statement describing the self driving capabilities."""
        print("This car can drive itself!")

    def fill_gas_tank(self):
        """Print a statement describing the gas tank."""
        print("This car does not have a gas tank!")


print("Make a car, and check the odometer:")
my_kia = Car('kia', 'sorento', 2017)
print(my_kia.get_descriptive_name())
my_kia.read_odometer()
my_kia.update_odometer(23_500)
my_kia.read_odometer()
my_kia.increment_odometer(100)
my_kia.read_odometer()
my_kia.increment_odometer(-50)
my_kia.read_odometer()
my_kia.fill_gas_tank()


print("\nMake an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.self_driving()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.update_odometer(100)
my_tesla.read_odometer()


