responses = {}
# Set a flag to indicate that polling is active
polling_active = True
while polling_active:
    # Prompt for the person's name and response:
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain would you like to climb? ")

    #Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("\nWould anyone else like to take this poll? (y/n)")
    if repeat == 'n':
        polling_active = False

# Polling is complete.  Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")