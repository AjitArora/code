
class Role(object):
	def __init__(self, role_name):
		if type(role_name) is not str:
			raise Exception("role name should be string")
		self.name = role_name

	def get_name(self):
		return self.name
