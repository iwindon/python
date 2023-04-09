import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
    def roll_die(self, rolls):
        for roll in range(rolls):
            print(self.roll())

dice = Dice()

dice.roll_die(10)
