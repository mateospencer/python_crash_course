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

def show_messages(unsent_messages):
	"""Prints messages from a list of messages"""
	for message in unsent_messages:
		print(message)

def send_messages(unsent_messages, sent_messages):
	"""Simulates sending a message and moving it from an unsent list to sent list."""
	while unsent_messages:
		current_message = unsent_messages.pop()
		print(current_message)
		sent_messages.append(current_message)

unsent_messages = ["On my way!", "No worries.", "I love you.", "Take care."]
sent_messages = []

show_messages(unsent_messages)
send_messages(unsent_messages, sent_messages)

print("The following messages failed to send:")
print(unsent_messages)

print("The following messages were successfuly sent:")
print(sent_messages)


#	Section 8-11: Archived Messages
#	Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the 
#	list of messages. After calling the function, print both of your lists to show that the original
#	list retained its messages. 

def show_messages(unsent_messages):
	"""Prints messages from a list of messages"""
	for message in unsent_messages:
		print(message)

def send_messages(unsent_messages, sent_messages):
	"""Simulates sending a message and moving it from an unsent list to sent list."""
	while unsent_messages:
		current_message = unsent_messages.pop()
		print(current_message)
		sent_messages.append(current_message)

unsent_messages = ["On my way!", "No worries.", "I love you.", "Take care."]
sent_messages = []

show_messages(unsent_messages)
send_messages(unsent_messages[:], sent_messages)

print("The original list of messages to send:")
print(unsent_messages)

print("The following messages were successfuly sent:")
print(sent_messages)