#	Python Crash Course 2nd Edition
#	Page 99 (Dictionaries)

#	Section 6-1: Person
#	Use a dictionary to store information about a person you know. Store their first name, last
#	name, age, and the city in which tye live. You should have keys such as first_name, 
#	last_name, age, and city. Print each piece of information stored in your dictionary

person_0 = {'first_name': 'Jacinda', 'last_name': 'Ardern', 'age': '39', 'city': 'Wellington',}

print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])


#	Section 6-2: Favorite Numbers
#	Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys
#	in your dictionary. Think of a favorite number for each person, and store each as a value in
#	your dictionary. Print each person's name and their favorite number.

fav_numbers = {'Bella': '5', 'Sid': '2', 'Lisa': '6', 'Matt': '11', 'Kelen': '14',}

print("Bella's favorite number is " + fav_numbers['Bella'] + ".")
print("Sid's favorite number is " + fav_numbers['Sid'] + ".")
print("Lisa's favorite number is " + fav_numbers['Lisa'] + ".")
print("Matt's favorite number is " + fav_numbers['Matt'] + ".")
print("Kelen's favorite number is " + fav_numbers['Kelen'] + ".")


#	Section 6-3: Glossary
#	A Python dictionary can be used to model an actual dictionary. However, to avoid confusion let's
#	call it a glossary. 
#	*	Think of five programming words you've learned about in the previous chapters. Use three words
#		at the keys in your glossary, and store their meanins as values. 
#	* 	Print each word and its meaning as neatly formatted output. You might print the word followed 
#		by a colon and then its meaning, or print the word on one line and then print tis meaning 
#		indented on a second line. Use the newline character (\n) to insert a blank line between
#		each word-meaning pair in your output. 

glossary = {'dictionary': "a collection of key-value pairs.",
			'string': "a series of characters.",
			'method': "an action performed ona  piece of data.",
			}

print("A dictionary is " + glossary['dictionary'])
print("A string is " + glossary['string'])
print("A method is " + glossary['method'])