def describe_pet(pet_name, animal_type='cat'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

type = input("What type of pet do you have? ")
name = input("What is your pet's name? ")

describe_pet(animal_type = type, pet_name = name)
