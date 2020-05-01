#	Python Crash Course 2nd Edition
#	Page 155 (Functions in Modules)

#	Section 8-15: Printing Models
#	Put the functions for the example printing_models.py in a separate file called
#	printing_functions.py. Write an import statement at the top of printing_models.py, and modify
#	the file to use the imported functions. 

#	Per instructions, I've created a printing_models.py and printing_functions.py. Also, placed
#	code here to group it with the exercise. 

import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)