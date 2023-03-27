# Programming terms

terms = {
    'integer': 'A whole number',
    'float': 'A decimal number',
    'list': 'A "container" that can store any kind of values',
    'tuple': 'A similar "container" as a list with a difference that you cannot update the values in a tuple.',
}

for key, value in terms.items():
    print(f"\nTerm: {key.title()}")
    print(f"Definition: {value}")

