import printing

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing.print_models(unprinted_designs, completed_models)
printing.show_completed_models(completed_models)