#	Python Crash Course 2nd Edition
#	Page 146 (Functions Passing Lists)

#	Section 8-9: Messages
#	Make a list containing a series of short text messages. Pass the list to a function called
#	show_messages(), which prints each text message. 

def show_messages(messages):
	"""Prints messages from a list"""
	for message in messages:
		print(message)

messages = ["On my way!", "No worries.", "I love you.", "Take care."]
show_messages(messages)


#	Section 8-10: Sending Messages
#	Start with a copy of your program from Exercise 8-9. Write a function called send_messages()
#	that prints each text message and moves each message to a new list called sent_messages as it's 
#	printed. After calling the function, print both of your lists to make sure the messages were 
#	moved correctly. 