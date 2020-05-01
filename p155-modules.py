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


#	Section 8-16: Imports
#	Using a program you wrote that has one function in it, store that function in a separate file.
#	Import the function into your main program file, and call the function using each of these
#	approaches:
#		*	import module_name
#		*	from module_name import function_name
#		*	from module_name import function_name as fn
#		*	import module_name as mn
#		*	from module_name import *

import cars
tesla = cars.car_info('Tesla', 'Model S', color='Black', package='Long Range')
print(tesla)

from cars import car_info
polestar = car_info('Polestar', '1', color='Silver', package='Performance')
print(polestar)

from cars import car_info as ci
roadster = ci('Tesla', 'Roadster', color='Red', package='SpaceX')
print(roadster)

import cars as c
taycan = c.car_info('Porsche', 'Taycan', color='Silver', package='4S')
print(taycan)

from cars import car_info
etron = car_info('Audi', 'e-Tron', color='Blue', package='A3')
print(etron)


#	Section 8-17: Styling Functions
#	Choose any three programs you wrote for this chapter, and make sure they follow the styling 
#	guidelines described in this section.

Complete.


