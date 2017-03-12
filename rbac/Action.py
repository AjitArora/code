
class Action(object):
	def __init__(self, action_name):
		if type(action_name) is not str:
			raise Exception("action name should be string")
		self.name = action_name

	def get_name(self):
		return self.name
