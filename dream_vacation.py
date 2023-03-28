responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where would you like to visit? ")
    responses[name] = response

    repeat = input("Would someone else like to answer? (y/n) ")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}, {response}")
