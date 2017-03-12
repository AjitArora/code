from ParkingLot import ParkingLot
from Vehicle import Car

class Controller:
	def __init__(self):
		self.lot = None

	def run_cmd(self, line):
		args = line.split(" ")
		cmd = args[0]
		if cmd == "create_parking_lot":
			self.lot = ParkingLot(args[1])
			return "Created a parking lot with %s slots"%args[1]
		if not self.lot:
			raise Exception("Parking Lot is not created")

		if cmd == "park":
			return self.lot.assign_vehicle_slot(Car(args[1], args[2]))

		if cmd == "leave":
			return self.lot.release_vehicle(args[1])
		if cmd == "status":
			return self.lot.get_status()
		if cmd == "registration_numbers_for_cars_with_colour":
			return self.lot.registration_numbers_for_cars_with_colour(args[1])

		if cmd == "slot_number_for_registration_number":
			return self.lot.slot_number_for_registration_number(args[1])
		if cmd == "slot_numbers_for_cars_with_colour":
			return self.lot.slot_numbers_for_cars_with_colour(args[1])
		return "cmd %s is not valid"%cmd