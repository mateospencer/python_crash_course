#	Python Crash Course 2nd Edition
#	Page 173 (Inheritance part 2)

#	Section 9-8: Privileges
#	Write a separate Privileges class. The class should have one attribute, privileges, that stores
#	a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class.
#	Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin 
#	and use your method to show its privileges.

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

admin2 = Admin('Admin', 'Istrator 2', 'admin2@website.co.nz', 'Admin2')
admin2.privileges = ['backup volume', 'create volume', 'delete volume']

admin2.describe_user()
admin2.privileges.show_privileges()