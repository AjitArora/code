class Slot:
	def __init__(self, slotid):
		self.slotid = slotid
		self._is_available = True
		self.vehicle = None

	def get_id(self):
		return self.slotid

	def is_available(self):
		return self._is_available

	def occupy(self, vehicle):
		self.vehicle = vehicle
		self._is_available = False

	def release(self):
		self.vehicle = None
		self._is_available = True

	def get_vehicle(self):
		return self.vehicle