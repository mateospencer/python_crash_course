#	Python Crash Course 2nd Edition
#	Page 180 (Importing Classes)

#	Section 9-10: Imported Restaurant
#	Using your latest Restaurant class, store it in a module. Make a separate file that imports
#	Restaurant. Make a Restaurant instance, and call one of Restaurant's methods to show that the
#	import statement is working properly.

from restaurant import *

restaurant = Restaurant('Mercury', 'Tapas')
restaurant.describe_restaurant()


#	Section 9-11: Imported Admin
#	Start with your wok from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin
#	in one module. Create a separate file, make an Admin instance, and call show_privileges() to 
#	show that everything is working correctly.

from user import *

admin = Admin('Admin', 'Istrator', 'admin@website.co.nz', 'Administrator')
admin.privileges.privileges = ['backup volume', 'create volume', 'delete volume']

admin.describe_user()
admin.privileges.show_privileges()


#	Section 9-12: Multiple Modules
#	Store the User class in one module, and store the Privileges and Admin classes in a separate
#	module. In a separate file, create an Admin instance and call show_privileges() to show that
#	everything is still working correctly.

from admin import Admin

backupadmin = Admin('Backup', 'Admin', 'backupadmin@website.co.nz', 'Backup Administrator')
backupadmin.privileges.privileges = ['backup volume', 'create volume']

backupadmin.describe_user()
backupadmin.privileges.show_privileges()
