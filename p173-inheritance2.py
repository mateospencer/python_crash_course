#	Python Crash Course 2nd Edition
#	Page 173 (Inheritance part 2)

#	Section 9-8: Privileges
#	Write a separate Privileges class. The class should have one attribute, privileges, that stores
#	a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class.
#	Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin 
#	and use your method to show its privileges.

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

admin = Admin('Admin', 'Istrator', 'admin@website.co.nz', 'Administrator')

admin.describe_user()
admin.privileges.show_privileges()

admin_privileges = ['backup volume', 'create volume', 'delete volume',]

admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()


#	Section 9-9: Battery Upgrade
#	Use the final version of electric_car.py from this section. Add a method to the Battery class
#	called upgrade_battery(). This method should check the battery size and set the capacity to 100
#	if it isn't already. Make an electric car with a default battery size, call get_range() once,
#	and then call get_range() a second time after upgrading the battery. You should see an increase
#	in the car's range. 

class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery:
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
			
		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""Method to change the battery size."""
		print("Attempting to upgrade battery capacity.")
		if self.battery_size < 100:
			print("Battery capacity upgraded!")
			self.battery_size = 100
		else:
			print("Battery is already fully upgraded.")

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

