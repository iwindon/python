answer = int(input("When was Python 1.0 released? "))



while answer != 1994:
    if answer < 1994:
        print("It was later than that!")
        answer = int(input("When was Python 1.0 released? "))
    elif answer > 1994:
        print("It was earlier than that!")
        answer = int(input("When was Python 1.0 released? "))

if answer == 1994:
    print("Correct!")
