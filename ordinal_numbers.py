ordinals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in ordinals:
    if num > 3:
        print(f"{num}th.")
    elif num == 1:
        print(f"{num}st.")
    elif num == 2:
        print(f"{num}nd.")
    else:
        print(f"{num}rd.")
    