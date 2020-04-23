#	Python Crash Course 2nd Edition
#	Page 105 (Dictionaries)

#	Section 6-4: Glossary 2
#	Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3
#	(page 99) by replacing your series of print() calls with a loop that runs through the
#	dictionary's keys and values. When you're sure that your loop works, add five more Python terms 
#	to your glossary. When you run your progam again, these new words and meanings should
#	automatically be included in the output. 

glossary = {'dictionary': "a collection of key-value pairs.",
			'string': "a series of characters.",
			'method': "an action performed on a piece of data.",
			'key value pair': "a set of values associated with each other.",
			'pop()': "a method that removes the last item in a list.",
			'append()': "a method that adds a new element to the end of a list.",
			'list': "a collection of items in a particular order.",
			'constant': "like a variable whose value stays the same through the life of a program.",
			}

for term in glossary.keys():
	definition = glossary[term]
	print("A " + term + " is " + definition)


#	Section 6-5: Rivers
#	Make a dictionary containing three major rivers and the country each river runs through. One
#	key-value pair might be 'nile': 'egypt'
#	*	Use a loop to print a sentence about each river, such as The Nile runs through Egypt
#	*	Use a loop to print the name of each river included in the dictionary. 
#	*	Use a loop to print the name of each country included in the dictionary. 

rivers = {'whanganui': 'aotearoa',
			'cacapon': 'america',
			'monongahela': 'america',
			}

for river in rivers.keys():
	country = rivers[river]
	print("The " + river.title() + " River runs through " + country.title() + ".")

print("The rivers in the list are:")
for river in rivers.keys():
	print(river.title())

#	Using set here removes duplicate listings. 
print("The countries in the list are:")
for country in set(rivers.values()):
	print(country.title())


#	Section 6-6: Polling
#	Use the code in favorite_languages.py (page 97).
#	*	Make a list of people who should take the favorite languages poll. Include some names that
#		are already in the dictionary and some that are not.
#	*	Loop through the list of people who should take the poll. If they have already taken the
#		poll, print a message thanking them for responding. If they have not yet taken the poll, 
#		print a message inviting them to take the poll. 

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',}

people = {'kelen', 'lisa', 'jen', 'sarah', 'bella', 'sid'}

for person in people:
	if person in favorite_languages.keys():
		print(person.title() + ", thank you for responding to the poll.")
	else: 
		print(person.title() + ", you are invited to take our favorite dev language poll.")