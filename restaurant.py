"""A class that can be used to represent a restaurant."""

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

