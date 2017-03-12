import threading
from Queue import Queue
from Queue import PriorityQueue

import Utils
from Verification import DocumentVerification
from Verification import PoliceVerification
from Verification import BiometricVerification
from Application import Application

class Algorithm(threading.Thread):
	def __init__(self):
		self.__create_applications()
		self.__start_verification_process()

	def __create_applications(self):
		for i in xrange(0, self.applicants_per_hr):
			self.applications.append(Application(i))

	def __start_verification_process(self):
		self.docs_verification = DocumentVerification(self.docs_queue, self, "doc_verification_start", "doc_verification_done")
		self.police_verification = PoliceVerification(self.police_queue, self, "police_verification_start", "police_verification_done")
		self.biometric_verification = BiometricVerification(self.biometric_queue, self, "biometric_verification_start", "biometric_verification_done")
		self.docs_outgoing_applicants = 0
		self.police_outgoing_applicants = 0
		self.biometric_outgoing_applicants = 0
		for application in self.applications:
			self.docs_queue.put(application)

	def doc_verification_start(self, application):
		application.update_waiting_time()

	def doc_verification_done(self, application):
		#print "doc verification done %s"%application.get_token_number()
		application.set_last_processed_time()
		self.docs_outgoing_applicants += 1
		self.police_queue.put(application)
		if self.docs_outgoing_applicants == self.applicants_per_hr:
			self.docs_verification.stop()

	def police_verification_start(self, application):
		application.update_waiting_time()

	def police_verification_done(self, application):
		#print "police verification done %s"%application.get_token_number()
		application.set_last_processed_time()
		self.police_outgoing_applicants += 1
		self.biometric_queue.put(application)
		if self.police_outgoing_applicants == self.applicants_per_hr:
			self.police_verification.stop()

	def biometric_verification_start(self, application):
		application.update_waiting_time()

	def biometric_verification_done(self, application):
		#print "biometric verification done %s"%application.get_token_number()
		with self.lock:
			application.set_processing_etime()
			self.biometric_outgoing_applicants += 1
		if self.biometric_outgoing_applicants == self.applicants_per_hr:
			self.biometric_verification.stop()

	def get_avg_waiting_time(self):
		sum = 0
		for application in self.applications:
			sum += application.get_waiting_time()
		return (sum/self.applicants_per_hr) if self.applicants_per_hr else 0

	def get_avg_processing_time_and_applications(self):
		sum = 0
		count = 0
		with self.lock:
			for application in self.applications:
				ptime = application.get_processing_time()
				if ptime > 0:
					sum += ptime
					count += 1
			avg_ptime = (sum/count) if count else 0
		return avg_ptime, count

	def get_processed_applications_count(self):
		return self.biometric_outgoing_applicants

class GlobalFCFS(Algorithm):
	def __init__(self, applicants_per_hr):
		self.docs_queue = PriorityQueue()
		self.police_queue = PriorityQueue()
		self.biometric_queue = PriorityQueue()
		self.lock = threading.Lock()
		self.applicants_per_hr = applicants_per_hr
		self.applications = []
		Algorithm.__init__(self)

class StagewiseFCFS(Algorithm):
	def __init__(self, applicants_per_hr):
		self.docs_queue = Queue()
		self.police_queue = Queue()
		self.biometric_queue = Queue()
		self.lock = threading.Lock()
		self.applicants_per_hr = applicants_per_hr
		self.applications = []
		Algorithm.__init__(self)

class Random(Algorithm):
	def __init__(self, applicants_per_hr):
		self.docs_queue = Utils.CutomRandomQueue()
		self.police_queue = Utils.CutomRandomQueue()
		self.biometric_queue = Utils.CutomRandomQueue()
		self.lock = threading.Lock()
		self.applicants_per_hr = applicants_per_hr
		self.applications = []
		Algorithm.__init__(self)