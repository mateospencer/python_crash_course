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
			'method': "an action performed ona  piece of data.",
			'key value pair': "a set of values associated with each other.",
			'pop()': "a method that removes the last item in a list.",
			'append()': "a method that adds a new element to the end of a list.",
			'list': "a collection of items in a particular order.",
			'constant': "like a variable whose value stays the same through the life of a program.",
			}

for term in glossary.keys():
	definition = glossary[term]
	print("A " + term + " is " + definition)
