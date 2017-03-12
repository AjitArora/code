import re
from Params import USER_ID_COUNTER

class User(object):
	'''
	User have user_id, user_name, email_id, access_methods={role_name1: resource1, role_name2: resource2}
	'''
	def __init__(self, user_name, email_id):
		if not re.search(r'[\w.-]+@[\w.-]+.\w+', email_id):
			raise Exception("Incorrect email id")
		self.user_name = user_name
		self.email_id = email_id
		self.roles = [] # list with role names

		global USER_ID_COUNTER
		self.user_id = USER_ID_COUNTER # it would be incremental id given by DB.
		USER_ID_COUNTER += 1	

	def get_name(self):
		return self.user_name

	def get_id(self):
		return self.user_id

	def get_roles(self):
		return self.roles

	def has_role(self, role):
		if role in self.roles:
			return True
		return False

	def add_role(self, role):
		if self.has_role(role):
			# return, if user already has role
			return
		self.roles.append(role)

	def remove_role(self, role):
		'''
		Not Raises exception, if role is not present
		'''
		if self.has_role(role):
			self.roles.remove(role)