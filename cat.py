class Cat:
    """A simple attempt to model a cat."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a cat sitting in reponse to a command"""
        print(f"{self.name} glared at you with contempt and then turned and walked away.")
    
    def treat(self):
        """Simulate response to the word treat!"""
        print(f"{self.name} runs up to you meowing loudly.")

    def sleep(self):
        """Simulate the cat sleeping."""
        print(f"{self.name} is sleeping.")

my_cat = Cat('Daphene', 6)
your_cat = Cat('Calvin', 14)

my_cat.sit()
my_cat.treat()
my_cat.sleep()

print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")

print(f"Your cat's name is {your_cat.name}.")
print(f"Your cat is {your_cat.age} years old.")

your_cat.sit()
your_cat.treat()
your_cat.sleep()
