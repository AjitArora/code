class Resource(object):
	def __init__(self, resource_name):
		if type(resource_name) is not str:
			raise Exception("resource name should be string")
		self.name = resource_name
		self.access_role_actions = {} # {role: [Permitted Actions], ...}

	def get_name(self):
		return self.name

	def has_access_roles_action(self, role, action):
		if role not in self.access_role_actions.keys():
			self.access_role_actions[role] = []
			return False
		role_actions = self.access_role_actions[role]
		if action in role_actions:
			return True
		return False

	def add_access_roles_action(self, role, action):
		if not self.has_access_roles_action(role, action):
			self.access_role_actions[role].append(action)

	def remove_access_role_action(self, role, action):
		if not self.has_access_roles_action(role, action):
			self.access_role_actions[role].remove(action)

	def get_access_role_actions(self):
		return self.access_role_actions