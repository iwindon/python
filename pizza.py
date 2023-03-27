# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Sumaraize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping.title()}")

