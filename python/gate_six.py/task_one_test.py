from unittest import TestCase

from task_one import *

class task_one_test(TestCase):

    def test_create_parking_slots_function_creates_the_right_amount_of_empty_slots(self):

        actual =create_parking_slots()

        expected =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        self.assertEqual(actual, expected)

    def test_parking_function(self):
        parking_slots =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        desired_parking_slot =5

        actual_value =parking(parking_slots, desired_parking_slot)

        expected_value =[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        
        self.assertEqual(actual_value, expected_value)

    def test_parking_function_if_is_occupied(self):
        parking_slots =[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        desired_parking_slot =5

        actual_value =parking(parking_slots, desired_parking_slot)

        expected_value =[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        
        self.assertEqual(actual_value, expected_value)

    def test_unparking_function(self):

        parking_slots =[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        alloted_parking_slot =5

        actual_value =unparking(parking_slots, alloted_parking_slot)

        expected_value =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]


        self.assertEqual(actual_value, expected_value)


    def test_unparking_function_if_is_empty(self):
        parking_slots =[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        desired_parking_slot =5

        actual_value =parking(parking_slots, desired_parking_slot)

        expected_value =[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        
        self.assertEqual(actual_value, expected_value)


    def test_check_slots_statuses_function(self):

        parking_slots =[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

        actual =check_slots_statuses(parking_slots)

        expected ="It works"

        self.assertEqual(actual, expected)





































