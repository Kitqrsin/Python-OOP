from project.railway_station import RailwayStation
from unittest import TestCase, main
from collections import deque


class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.railway_station = RailwayStation('test_station')

    def test_if_init_is_correct(self):
        self.assertEqual(self.railway_station.name, "test_station")
        self.assertEqual(self.railway_station.arrival_trains, deque())
        self.assertEqual(self.railway_station.departure_trains, deque())

    def test_if_it_would_raise_a_value_error_if_the_name_is_less_or_equal_3_symbols(self):
        with self.assertRaises(ValueError) as ex:
            self.railway_station.name = 'tes'

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.railway_station.name = 'te'

        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_if_new_train_info_would_be_appended_to_the_arrival_trains_deque_from_new_arrival_on_board(self):
        expected_result = deque(["some_train_info_1"])

        self.railway_station.new_arrival_on_board('some_train_info_1')
        self.assertEqual(expected_result, self.railway_station.arrival_trains)

    def test_train_has_arrived_method_if_there_arent_other_trains_to_arrive_before_the_given_one(self):
        self.railway_station.new_arrival_on_board('some_train_info_2')

        expected_result = "some_train_info_2 is on the platform and will leave in 5 minutes."
        expected_arrival_trains_deque = deque([])
        expected_departure_trains_deque = deque(['some_train_info_2'])
        result = self.railway_station.train_has_arrived('some_train_info_2')

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_arrival_trains_deque, self.railway_station.arrival_trains)
        self.assertEqual(expected_departure_trains_deque, self.railway_station.departure_trains)

    def test_train_has_arrived_method_if_there_are_other_trains_to_arrive(self):
        self.railway_station.new_arrival_on_board('some_train_info_1')
        self.railway_station.new_arrival_on_board('some_train_info_2')

        result = self.railway_station.train_has_arrived('some_train_info_2')
        expected_result = "There are other trains to arrive before some_train_info_2."
        expected_arrival_trains_deque = deque(['some_train_info_1', 'some_train_info_2'])
        expected_departure_trains_deque = deque([])

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_arrival_trains_deque, self.railway_station.arrival_trains)
        self.assertEqual(expected_departure_trains_deque, self.railway_station.departure_trains)

    def test_train_has_left_method_if_the_train_leaves(self):
        self.railway_station.departure_trains = deque(["some_train_info_1", "some_train_info_2"])

        result = self.railway_station.train_has_left('some_train_info_1')
        expected_result = True
        expected_departure_trains_deque = deque(["some_train_info_2"])

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_departure_trains_deque, self.railway_station.departure_trains)

    def test_train_has_left_method_if_the_train_doesnt_leave(self):
        self.railway_station.departure_trains = deque(['some_train_info_1', 'some_train_info_2'])

        result = self.railway_station.train_has_left('some_train_info_2')
        expected_result = False
        expected_departure_trains_deque = deque(['some_train_info_1', 'some_train_info_2'])

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_departure_trains_deque, self.railway_station.departure_trains)


if __name__ == '__main__':
    main()