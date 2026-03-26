from unittest import TestCase

from task_one import *

class task_one_test(TestCase):

    def test_that_non_duplicate_numbers_will_be_added(self):

        collection_of_phone_numbers =[]

        actual =function_to_add_phone_number(collection_of_phone_numbers,"070")
 
        expected =["070"]
        print(collection_of_phone_numbers)

        self.assertEqual(actual, expected)


    def test_that_duplicate_numbers_will_throw_an_error(self):

        collection_of_phone_numbers =["070"]

        actual =function_to_add_phone_number(collection_of_phone_numbers, "070")

        expected ="Error 419 -->The number already exists"

        self.assertEqual(actual, expected)        
        
    
