import threading
import time
from Worker import Worker

import Params

class Verification(object):
	def __init__(self, queue, agents_count, min_durtion, max_durtion, caller, pre_callback, post_callback):
		self.agents_count = agents_count
		self.queue = queue
		self.workers = []
		t = threading.Thread(target = self.__start, args=(min_durtion, max_durtion, caller, pre_callback, post_callback))
		t.start()

	def __start(self,min_durtion, max_durtion, caller, pre_callback, post_callback):
		for i in xrange(0, self.agents_count):
			w = Worker(self.queue, i, min_durtion, max_durtion, caller, pre_callback, post_callback)
			self.workers.append(w)
			w.start()

	def stop(self):
		for i in xrange(0, self.agents_count):
			self.queue.put(None)
		self.queue.join()
		for w in self.workers:
			w.join()
			

class DocumentVerification(Verification):
	def __init__(self, queue,caller, pre_callback, post_callback):
		Verification.__init__(self, queue, Params.DOC_AGENTS_COUNT, Params.DOCS_VERIFICATION_MIN_DURATION,
		 Params.DOCS_VERIFICATION_MAX_DURATION, caller, pre_callback, post_callback)
		
class PoliceVerification(Verification):
	def __init__(self, queue,caller, pre_callback, post_callback):
		Verification.__init__(self, queue, Params.POLICE_AGENTS_COUNT,Params.POLICE_VERIFICATION_MIN_DURATION,
		 Params.POLICE_VERIFICATION_MAX_DURATION, caller, pre_callback, post_callback)

class BiometricVerification(Verification):
	def __init__(self, queue,caller, pre_callback, post_callback):
		Verification.__init__(self, queue, Params.BIOMETRIC_AGENTS_COUNT,Params.BIOMETRIC_VERIFICATION_MIN_DURATION,
		 Params.BIOMETRIC_VERIFICATION_MAX_DURATION, caller, pre_callback, post_callback)
