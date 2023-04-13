from pathlib import Path

guest = input("What is your name? ")
path = Path('guest.txt')
path.write_text(guest)
