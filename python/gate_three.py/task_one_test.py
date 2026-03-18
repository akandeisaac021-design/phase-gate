from unittest import TestCase

from task_one import *

class test_new_list_functions(TestCase):
#
#    def test_that_new_list_functions_is_accurate_if_new_list_length_is_excess(self):
#
#        length_of_expected_list =7
#
#        list_of_numbers =[1, 21, 3, 32, 54]
#
#        actual =new_list_functions(list_of_numbers, length_of_expected_list)
#
#        expected =[1, 21, 3, 32, 54, -1, -1]
#
#        self.assertEqual(actual, expected)
#
#    def test_that_new_list_functions_is_accurate_if_new_list_length_is_not_enough(self):
#
#        length_of_expected_list =2
#
#        list_of_numbers =[1, 21, 3, 32, 54]
#
#        actual =new_list_functions(list_of_numbers, length_of_expected_list)
#
#        expected =[1, 21]
#
#        self.assertEqual(actual, expected)
#
#    def test_that_new_list_functions_is_accurate(self):
#        
#        length_of_expected_list =5
#
#        list_of_numbers =[1, 21, 3, 32, 54]
#
#        actual =new_list_functions(list_of_numbers, length_of_expected_list)
#
#        expected =[1, 21, 3, 32, 54]
#
#        self.assertEqual(actual, expected)
#
#
    def test_that_case_sensitive_word_counter_accurate(self):

        name ="Isaac"

        actual =case_sensitive_word_counter(name)

        expected =" a2 c1 s1 I1"

        self.assertEqual(actual, expected)
