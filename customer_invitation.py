import sys
import math
import json

class Coordinates:
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def get_latitude(self):
		return self.latitude

	def get_longitude(self):
		return self.longitude

class Customer:
	def __init__(self, user_id, name, coordinates):
		self.id = user_id
		self.name = name
		self.coordinates = coordinates

	def get_name(self):
		return self.name

	def get_coordinates(self):
		return self.coordinates

class CustomerInvitation:
	def __init__(self, input_file, output_file):
		self.customers_data = {}
		self.max_distance = 100
		self.input_file = input_file
		self.output_file = output_file
		self.intercom_latitude = 53.3381985
		self.intercom_longitude = -6.2592576

	def parse_input(self, input_file):
		'''
		parse customers file into dictionary as below format:
			customers_data[user_id] = <Customer object>
		'''
		customers_data = {}
		fin = open(input_file, "r")
		for line in fin:
			line = json.loads(line)

			try:
				# validating customer dictionary
				user_id = line['user_id']
				name = line['name']
				latitude = float(line['latitude'])
				longitude = float(line['longitude'])
			except Exception, fault:
				print "Invalid Customer Entry found %s, Error: %s"%(line, str(fault))
				continue

			coordinates = Coordinates(latitude, longitude)
			customers_data[user_id] = Customer(user_id, name, coordinates)

		return customers_data

	def degree_to_radion(self, degree):
		return degree * (math.pi/180)

	def calculate_coordinates_distance(self, first_coordinates, second_coordinates):
		earth_radius = 6371 # Radius of the earth in km
		latitute_diff = self.degree_to_radion(second_coordinates.get_latitude() \
			-first_coordinates.get_latitude())
		longitude_diff = self.degree_to_radion(second_coordinates.get_longitude() \
			-first_coordinates.get_longitude())
		formula = math.sin(latitute_diff/2) * math.sin(latitute_diff/2)
		formula += math.cos(self.degree_to_radion(second_coordinates.get_latitude())) \
				* math.cos(self.degree_to_radion(first_coordinates.get_latitude())) \
				* math.sin(longitude_diff/2) * math.sin(longitude_diff/2)
		central_angle = 2 * math.atan2(math.sqrt(formula), math.sqrt(1-formula))
		distance = earth_radius * central_angle;
		return distance

	def write_output_into_file(self, customers_data, output_file):
		'''
			writes customer user_id and name in csv format(in ascending order)
		'''
		fout = open(output_file, "w+")
		fout.write("user_id,")
		fout.write("name \n")
		sorted_userids = sorted(customers_data.keys())
		for user_id in sorted_userids:
			customer = customers_data[user_id]
			name = customer.get_name()
			fout.write(str(user_id)+",")
			fout.write(name+"\n")

	def main(self):
		intercom_coordinates = Coordinates(self.intercom_latitude, self.intercom_longitude)
		self.customers_data = self.parse_input(self.input_file)
		for user_id in self.customers_data.keys():
			customer = self.customers_data[user_id]
			customer_coordinates = customer.get_coordinates()
			distance = self.calculate_coordinates_distance(intercom_coordinates, customer_coordinates)
			#if distance is more than maximum distance(100 Kms), remove customer from dictionary
			if distance > self.max_distance:
				del self.customers_data[user_id]
		self.write_output_into_file(self.customers_data, self.output_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "<Usage> python customer_invitation.py <input_file_name> <output_file_name>"
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    customer_invitation = CustomerInvitation(input_file, output_file)
    customer_invitation.main()
