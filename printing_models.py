def print_models(unprinted_designs, completed_models):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''Show all the models that were printed.'''
    print(f"\nThe follwing models have been printed:")
    for model in completed_models:
        print(model)

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
