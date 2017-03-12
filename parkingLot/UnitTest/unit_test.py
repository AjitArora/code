import unittest
from ddt import ddt, data, file_data

from ParkingLot import ParkingLot
from Vehicle import Car

@ddt
class UnitTest(unittest.TestCase):

    @file_data("unit_test_cases.json")
    def test(self, **kwargs):
        func = kwargs['function']
        if func == 'create_parking_lot':
            get_parking_lot(kwargs["slot_count"])
            return
        elif func == 'assign_vehicle_slot':
            lot = get_parking_lot(3)
            ret = lot.assign_vehicle_slot(Car(kwargs["vehicle_reg_no"], kwargs["vehicle_color"]))
        elif func == 'release_vehicle':
            lot = get_parking_lot(3)
            ret = lot.release_vehicle(kwargs['slot_number'])
        elif func == 'slot_numbers_for_cars_with_colour':
            lot = get_parking_lot(3)
            ret = lot.slot_numbers_for_cars_with_colour(kwargs['vehicle_color'])
            print "success output:%s"%ret
            return
        elif func == 'slot_number_for_registration_number':
            lot = get_parking_lot(3)
            ret = lot.slot_number_for_registration_number(kwargs['vehicle_reg_no'])
            print "success output:%s"%ret
            return
        elif func == 'registration_numbers_for_cars_with_colour':
            lot = get_parking_lot(3)
            ret = lot.registration_numbers_for_cars_with_colour(kwargs['vehicle_color'])
            print "success output:%s"%ret
            return
        if ret != kwargs['Expected Answer']:
            print "Expected Answer is %s, got %s"%(kwargs['Expected Answer'], ret)
        else:
            print "success"

lot = None
def get_parking_lot(slots_count):
	global lot
	if not lot:
		lot = ParkingLot(slots_count)
	return lot

if __name__ == "__main__":
    unittest.main()