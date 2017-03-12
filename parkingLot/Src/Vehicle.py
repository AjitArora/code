import Params
class Vehicle:
	def __init__(self, registration_number, color, vehicle_type):
		self.registration_number = registration_number
		self.color = color
		self.vehicle_type = vehicle_type

	def get_reg_number(self):
		return self.registration_number

	def get_color(self):
		return self.color

	def get_vehicle_type(self):
		return self.vehicle_type

class Car(Vehicle):
	def __init__(self, registration_number, color):
		Vehicle.__init__(self, registration_number, color, Params.CAR)