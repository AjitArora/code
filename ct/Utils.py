import threading
from random import randrange

class CutomRandomQueue(object):
	def __init__(self):
		self.__lock = threading.Lock()
		self.__cond = threading.Condition(self.__lock)
		self.q_items = []
		self.q_len = 0

	def get(self):
		while True:
			with self.__lock:
				if self.q_len > 0:
					index = randrange(0, self.q_len)
					item = self.q_items.pop(index)
					self.q_len -= 1
					return item
				else:
					self.__cond.wait(3) # waits for 3 seconds

	def put(self, item):
		with self.__lock:
			self.q_items.append(item)
			self.q_len += 1
			self.__cond.notify()

	def task_done(self):
		pass

	def join(self):
		pass
