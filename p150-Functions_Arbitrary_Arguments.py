#	Python Crash Course 2nd Edition
#	Page 150 (Arbitrary Number of Arguments)

#	Section 8-12: Sandwiches
#	Write a function that accepts a list of items a person wants on a sandwich. The function should
#	have one parameter that collects as many items as the function call provides, and it should
#	print a summary of the sandwich that's being ordered. Call the function three times, using a 
#	different number of arguments each time. 

def make_sandwich(*toppings):
	print(toppings)

make_sandwich('bacon', 'lettuce', 'tomato',)
make_sandwich('peanut butter', 'jelly',)
make_sandwich('cheese')


#	Section 8-13: User Profiles
#	Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling
#	build_profile(), using your first and last names and three other key-value pairs that describe
#	you. 

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('mateo', 'spencer', city='wellington', country='new zealand', 
	title='lead data scientist')
print(user_profile)