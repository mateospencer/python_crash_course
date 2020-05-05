#	Note: This is named user2.py because user.py which also contained User, Admin, and Privilege 
#	methods was necessary for a previous exercise. If I removed Admin and Privilege from that module
#	then those exercise files would no longer work. Hence, another user.py was created with just the
#	user method included. 

class User:
	"""A class for simulated user profile details"""
	def __init__(self, first_name, last_name, email, title):
		"""Initializing attributes"""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.email = email
		self.title = title.title()
		self.login_attempts = 0

	def describe_user(self):
		print(f"\nUser's Name: {self.first_name} {self.last_name}")
		print(f"Email: {self.email}")
		print(f"Title: {self.title}")

	def greet_user(self):
		"""Greets user by username"""
		print(f"\nKia ora, {self.first_name}!")

	def increment_login_attempts(self):
		"""Enables incrementing the number of login attempts by the user via a method"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Resets login attempts back to zero"""
		self.login_attempts = 0