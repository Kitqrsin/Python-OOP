from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 100)

    def test_class_vehicle_attributes(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_if_fuel_is_enough_decrease_fuel_by_given_kilometers(self):
        expected_fuel_after_drive = 100 - 2.5
        self.vehicle.drive(1)
        self.vehicle.drive(1)
        self.assertEqual(expected_fuel_after_drive, self.vehicle.fuel)

    def test_drive_when_fuel_needed_is_more_than_current_vehicle_fuel_raise_an_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_when_the_fuel_given_does_not_exceed_the_capacity(self):
        self.vehicle.fuel = 90
        expected_result_for_fuel = 92
        self.vehicle.refuel(1)
        self.vehicle.refuel(1)
        self.assertEqual(expected_result_for_fuel, self.vehicle.fuel)

    def test_refuel_when_the_sum_of_the_current_fuel_and_the_given_fuel_exceeds_the_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)  # currently self.fuel and self.capacity both equal 100

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if__str__returns_the_correct_string(self):
        self.vehicle.horse_power = 55
        self.vehicle.fuel = 24
        expected_result = f"The vehicle has 55 " \
                          f"horse power with 24 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_result, self.vehicle.__str__())


if __name__ == "__main__":
    main()