class Restaurant:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        self.number_served = 0

    def describe(self):
        print(f"{self.name} serves {self.type} style food.")

    def open(self):
        print(f"The resurant {self.name} is open.")

    def read_number_served(self):
        print(f"There are {self.number_served} customers in the resturant.")

    def set_number_served(self, customers):
        if self.number_served >= customers:
            self.number_served = customers
        else:
            print("You can not reduce your total number of customers.")

    def increment_number_served(self, new_customers):
        if new_customers > 0:
            self.number_served += new_customers
        else:
            print("You need to enter a positive number.")

class IceCreamStand(Restaurant):

    def __init__(self, name, type) -> None:
        super().__init__(name, type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry']

    def display_flavors(self):
        print("The flavors we have are:")
        for flavor in self.flavors:
            print(f"\t{flavor}")

ice_cream_stand = IceCreamStand('The Ice Cream Stand', 'Ice Cream')
ice_cream_stand.describe()
ice_cream_stand.display_flavors()
