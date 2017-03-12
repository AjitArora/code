# Worker States
ideal
processing
stop

class Worker:
	def __init__(self):
		self.state = ideal

class Node:
	def __init__(self):
		self.workers = []

	def set_workers_state(self):
		pass

class Cluster:
	def __init__(self):
		self.nodes = []

class DB:
	def __init__(self):
		self.Q = Queue.Queue()

	def add_db_query(self, table_name, query):
		self.Q.put((table_name, query))

	def execute_db_query(self):
		pass

'''
	DB Schema:
		table: table_name same as company name
		columns:
			id, reciever_addr, sender_addr, user_contact_number, timestamp
		table: Others(if company table doesn't found)
		columns:
			same as above + company name
'''