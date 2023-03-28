sandwitch_orders = ['italian', 'pastrami', 'meat ball', 'pastrami', 'tuna', 'pastrami']
finished_sandwitches = []

print("\nSorry, however the deli has run out of Pastrami.")

while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')

while sandwitch_orders:
    current_sandwitch = sandwitch_orders.pop()
    print(f"\nCurrently making the {current_sandwitch.title()} sandwitch.")
    finished_sandwitches.append(current_sandwitch)

print("\n--- Orders ready ---")
for order in finished_sandwitches:
    print(f"{order.title()} sandwitch is ready.")
    