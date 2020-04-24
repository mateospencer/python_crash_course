#	Python Crash Course 2nd Edition
#	Page 112 (Nesting)

#	Section 6-7: People
#	Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries
#	representing different people, and store all three dictionaries in a list called people. Loop
#	through your list of people. As you loop through the list, print everything you know about each
#	person. 

person_0 = {'first_name': 'Jacinda', 'last_name': 'Ardern', 'age': '39', 'city': 'Wellington',}
person_1 = {'first_name': 'Barack', 'last_name': 'Obama', 'age': '58', 'city': 'Washington',}
person_2 = {'first_name': 'Justin', 'last_name': 'Trudeau', 'age': '48', 'city': 'Ottawa',}

people = [person_0, person_1, person_2]

for person in people:
	print("\nFull Name: " + person['first_name'] + " " + person['last_name'])
	print("Age: " + person['age'])
	print("City: " + person['city'])


#	Section 6-8: Pets
#	Make several dictionaries, where each dictionary respresents a differentpet. In each dictionary,
#	include the kind of animal and the owner's name. Store these dictionaries in a list called pets.
#	Next, loop through your list and as you do, print everything you know about each pet. 

