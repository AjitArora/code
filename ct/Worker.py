import threading
import Queue
import time
from random import randrange
#from Algorithm import StagewiseFCFS

class Worker(threading.Thread):
	def __init__(self, queue, workerid, min_durtion, max_durtion, caller, pre_callback, post_callback):
		threading.Thread.__init__(self)
		self.workerid = workerid
		self.queue = queue
		self.min_duration = min_durtion
		self.max_durtion = max_durtion
		self.caller = caller
		self.pre_callback = pre_callback
		self.post_callback = post_callback

	def process(self, item):
		method = getattr(self.caller, self.pre_callback)
		method(item)

		duration = randrange(self.min_duration, self.max_durtion)
		time.sleep(duration)
		
		method = getattr(self.caller, self.post_callback)
		method(item)

	def run(self):
		while(True):
			item = self.queue.get()
			if item is None:
				self.queue.task_done()
				break
			self.process(item)
			self.queue.task_done()