import time

class Application(object):
	def __init__(self, token_number):
		self.token_number = token_number
		self.last_processed_time = time.time()
		self.waiting_time = 0
		self.processing_stime = time.time()
		self.processing_etime = 0

	def __cmp__(self, other):
		return cmp(self.token_number, other.token_number)

	def get_token_number(self):
		return self.token_number

	def get_waiting_time(self):
		return self.waiting_time

	def set_last_processed_time(self):
		self.last_processed_time = time.time()

	def update_waiting_time(self):
		self.waiting_time += time.time() - self.last_processed_time

	def set_processing_etime(self):
		self.processing_etime = time.time()

	def get_processing_time(self):
		return self.processing_etime - self.processing_stime
