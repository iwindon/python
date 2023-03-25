guest_list = ['Christina Ricci', 'Jay Leno', 'Katee Sackhoff']

for name in guest_list:
    print(f"{name}, you are invited to a dinner party at my home.")

print(f"\n\nSadly, {guest_list[1]} is unable to attend the dinner party.\n\n")

guest_list[1] = 'Patrick Stewart'

for name in guest_list:
    print(f"{name}, you are invited to a dinner party at my home.")

print("\nI have found a bigger table, so I can invite 3 more people to the dinner party.")
guest_list.insert(0, 'Evan')
guest_list.insert(2, 'Micah')
guest_list.append('Michele')

for name in guest_list:
    print(f"{name}, you are invited to a dinner party at my home.")

print("\nSorry, I just found out the table will not arrive in time, I am only able to invite two people.\n\n")

num = 4
for i in range(1,5,1):
    guest_list.pop()

for name in guest_list:
    print(f"{name}, you are invited to a dinner party at my home.")

guests = len(guest_list)
print(f"We have {guests} guests invited.")

