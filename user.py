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

class Admin(User):
	"""A class for admin profile attributes"""
	def __init__(self, first_name, last_name, email, title):
		"""Initializing attributes of parent class and those for Admin"""
		super().__init__(first_name, last_name, email, title)
		self.privileges = Privileges()

class Privileges():
	"""Privileges for each user account"""
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		"""Lists the administrator's set of privileges."""
		print("\nPrivileges:")
		if self.privileges:
			for privilege in self.privileges:
				print(f"- {privilege}")
		else:
			print("- This user has no privileges.")