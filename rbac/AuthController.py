from Action import Action
from User import User
from Resource import Resource
from Role import Role
from Params import actions, users, roles, resources

def validate_user_id(func):
	def wrapper(self, *args, **kwargs):
		user_id = args[0]
		user = users.get(user_id, None)
		if not user:
			raise Exception("Incorrect user id")
		return func(self, *args, **kwargs)
	return wrapper

def validate_rule(func):
	'''
		validate role, action, resource
	'''
	def wrapper(self, *args, **kwargs):
		role_name, action_name, resource_name = args[0], args[1], args[2]
		role = roles.get(role_name, None)
		action = actions.get(action_name, None)
		resource = resources.get(resource_name, None)
		if not (role and action and resource):
			raise Exception("Incorrect rule")
		return func(self, *args, **kwargs)
	return wrapper

class AuthController(object):

	def create_user(self, user_name, email_id):
		user = User(user_name, email_id)
		users[user.get_id()] = user
		return user

	def add_role(self, role_name):
		role = Role(role_name)
		roles[role_name] = role
		return role

	def add_resource(self, resource_name):
		resource = Resource(resource_name)
		resources[resource_name] = resource
		return resource

	def add_action(self, action_name):
		action = Action(action_name)
		actions[action_name] = action
		return action

	@validate_user_id
	def assign_user_role(self, user_id, role_name):
		user = users[user_id]
		user.add_role(role_name)

	@validate_user_id
	def remove_user_role(self, user_id, role_name):
		user = users[user_id]
		user.remove_role(role_name)

	@validate_rule
	def add_rule(self, role_name, action_name, resource_name):
		resource = resources[resource_name]
		resource.add_access_roles_action(role_name, action_name)

	@validate_rule
	def remove_rule(self, role_name, action_name, resource_name):
		resource = resources[resource_name]
		resource.remove_access_roles_action(role_name, action_name)

	@validate_user_id
	def verify_user_access(self, user_id, action_name, resource_name):
		user = users[user_id]
		resource = resources.get(resource_name, None)
		if not resource:
			raise Exception("Invalid resource")
		user_roles = user.get_roles()
		for user_role in user_roles:
			return resource.has_access_roles_action(user_role, action_name)
		return False

	def list_all_user_roles(self):
		user_roles = {} # user_name: roles
		for user_id in users.keys():
			user = users[user_id]
			user_roles[user.get_name()] = user.get_roles()
		return user_roles

	@validate_user_id
	def list_user_roles(self, user_id):
		user = users[user_id]
		return user.get_roles()

	def list_resource_access_roles(self):
		resource_roles = {} # { resource_name: {role:actions,...} ...}
		for resource_name in resources.keys():
			resource = resources[resource_name]
			resource_roles[resource.get_name()] = resource.get_access_role_actions()
		return resource_roles