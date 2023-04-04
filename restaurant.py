class Restaurant:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    def describe(self):
        print(f"{self.name} serves {self.type} style food.")

    def open(self):
        print(f"The resurant {self.name} is open.")

resturant = Restaurant('In and Out', 'American')

resturant.describe()
resturant.open()

resturant = Restaurant('The Crab House', "Sea Food")
resturant.describe()

resturant = Restaurant('The Olive Garden', 'Italian')
resturant.describe()
