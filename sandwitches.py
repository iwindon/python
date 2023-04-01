def make_sandwitch(*toppings):
    print("\nMaking Sandwitch")
    for topping in toppings:
        print(f"- {topping}")

make_sandwitch("roast beef", "onions", "tomatoes", "lettuce")
make_sandwitch("ham", "mustard")
make_sandwitch("peanut butter", "jelly")