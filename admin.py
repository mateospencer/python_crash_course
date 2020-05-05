from user import User

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