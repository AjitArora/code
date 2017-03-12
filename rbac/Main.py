from AuthController import AuthController

if __name__ == '__main__':
	controller = AuthController()
	#Created users
	user1 = controller.create_user('Ms. Teacher', 'a@b.com')
	user2 = controller.create_user('Mr. Student','b@b.com')

	#defined roles
	role1 = controller.add_role('admin')
	role2 = controller.add_role('teacher')
	role3 = controller.add_role('student')

	# defined resources
	res1 = controller.add_resource('Paper')
	res2 = controller.add_resource('marksheet')

	# Actions
	action1 = controller.add_action('create')
	action2 = controller.add_action('write')
	action3 = controller.add_action('read')
	action4 = controller.add_action('delete')

	# user1 has admin & teacher role
	# user2 has student role
	controller.assign_user_role(user1.get_id(), role1.get_name())
	controller.assign_user_role(user1.get_id(), role2.get_name())
	controller.assign_user_role(user2.get_id(), role3.get_name())

	# Assign role and action type to resources
	controller.add_rule(role1.get_name(), action1.get_name(), res1.get_name()) # admin can create exam paper
	controller.add_rule(role2.get_name(), action2.get_name(), res1.get_name()) # teacher can write questions on paper
	controller.add_rule(role3.get_name(), action3.get_name(), res1.get_name()) # students can read from paper

	print "Users: "+str(controller.list_all_user_roles())
	print "Resources: "+str(controller.list_resource_access_roles())

	# verify user access
	print controller.verify_user_access(user1.get_id(), action1.get_name(), res1.get_name()) # True
	print controller.verify_user_access(user2.get_id(), action3.get_name(), res1.get_name()) # True

	# user2 pass out, user2 doesn't have access to student role
	print "----- Removed student role from user2 -----"
	controller.remove_user_role(user2.get_id(), role3.get_name())
	print controller.verify_user_access(user2.get_id(), action3.get_name(), res1.get_name()) # False

	print controller.list_all_user_roles()