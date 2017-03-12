import threading
from Slot import Slot

class ParkingLot():
	def __init__(self, slots_count):
		self.slots_count = int(slots_count)
		self.allocated_slots_count = 0
		self.slots = {}
		self._lock = threading.Lock()
		self.vehicle_slot_map = {} #vehicle registartion number and slot mapping
		self.vehicle_color_reg_numbers_map = {} # vehicle color and reg. number list mapping
		self.vehicle_color_slots_map = {} # vehicle color and slot list map
		self.__create_slots()

	def __create_slots(self):
		for slot_id in xrange(1, self.slots_count+1):
			self.slots[slot_id] = Slot(slot_id)

	def __find_available_slot(self):
		if self.allocated_slots_count == self.slots_count:
			raise Exception("Sorry, parking lot is full")

		for slot_id in xrange(1, self.slots_count+1):
			slot = self.slots[slot_id]
			if slot.is_available():
				return slot

	def assign_vehicle_slot(self, vehicle):
		with self._lock:
			vehicle_reg_number = vehicle.get_reg_number().lower()
			if self.vehicle_slot_map.get(vehicle_reg_number, None):
				return "Vehicle is already in parking lot"
			try:
				slot = self.__find_available_slot()
			except Exception, fault:
				return str(fault)

			slot.occupy(vehicle)
			vehicle_color = vehicle.get_color().lower()
			self.vehicle_slot_map[vehicle_reg_number] = slot.get_id()
			self.allocated_slots_count += 1
			self.vehicle_color_reg_numbers_map[vehicle_color] = self.vehicle_color_reg_numbers_map.get(vehicle_color, [])
			self.vehicle_color_reg_numbers_map[vehicle_color].append(vehicle_reg_number)
			self.vehicle_color_slots_map[vehicle_color] = self.vehicle_color_slots_map.get(vehicle_color, [])
			self.vehicle_color_slots_map[vehicle_color].append(slot.get_id())
			return "Allocated slot number: %s"%slot.get_id()

	def release_vehicle(self, slot_id):
		with self._lock:
			slot = self.slots.get(int(slot_id), None)
			if not slot:
				return "Slot number %s is not valid"%slot_id
			vehicle = slot.get_vehicle()
			slot.release()
			vehicle_reg_number = vehicle.get_reg_number().lower()
			vehicle_color = vehicle.get_color().lower()
			self.allocated_slots_count -= 1
			self.vehicle_color_reg_numbers_map[vehicle_color] = self.vehicle_color_reg_numbers_map.get(vehicle_color, [])
			self.vehicle_color_reg_numbers_map[vehicle_color].remove(vehicle_reg_number)
			self.vehicle_color_slots_map[vehicle_color] = self.vehicle_color_slots_map.get(vehicle_color, [])
			self.vehicle_color_slots_map[vehicle_color].remove(slot.get_id())
			del self.vehicle_slot_map[vehicle_reg_number]
			return "Slot number %s is free"%slot_id

	def registration_numbers_for_cars_with_colour(self, color):
		return self.vehicle_color_reg_numbers_map.get(color.lower(), [])

	def slot_numbers_for_cars_with_colour(self, color):
		return self.vehicle_color_slots_map.get(color.lower(), [])

	def slot_number_for_registration_number(self, reg_number):
		return self.vehicle_slot_map.get(reg_number.lower(), "Not found")

	def get_status(self):
		msg = "Slot No.    Registration No    Colour \n"
		with self._lock:
			for slot_id in xrange(1, self.slots_count+1):
				slot = self.slots[slot_id] 
				if not slot.is_available():
					vehicle = slot.get_vehicle()
					msg += str(slot_id)+"    "+vehicle.get_reg_number()+"    "+vehicle.get_color()+"\n"
		return msg
