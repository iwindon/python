days = input("How many days ago have you purchased the item? ")
if int(days) > 10:
    defect = input("Has the item broken down on its own [y/n]? ")
    if defect == 'y':
        print("You can get a refund.")
    else:
        print("You cannot get a refund.")
else:
    used = input("Have you used the item at all [y/n]? ")
    if used == 'y':
        print("You cannot get a refund.")
    else:
        print("You can get a refund.")