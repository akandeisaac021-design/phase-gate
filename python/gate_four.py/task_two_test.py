from unittest import TestCase

from task_two import *

class task_two_test(TestCase):

    def test_how_many_even_numbers_are_in_a_list_function(self):

        numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        actual =how_many_even_numbers_are_in_a_list(numbers)

        expected =5

        self.assertEqual(actual, expected)

    def test_linear_search_function(self):

        numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        target =5

        actual =linear_search(numbers, target)

        expected =4

        self.assertEqual(actual, expected)


    def test_linear_search_function_when_target_is_not_available(self):

        numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        target =14

        actual =linear_search(numbers, target)

        expected =-1

        self.assertEqual(actual, expected)


    def test_squares_function(self):

        target =4

        actual =squares(target)

        expected =[4, 9, 16, 25]

        self.assertEqual(actual, expected)


    def test_list_equals_function_is_true(self):

        numbers =[1, 2, 3, 4]

        numbers2 =[1, 2, 3, 4]

        actual =list_equals(numbers, numbers2)

        expected =True

        self.assertEqual(actual, expected)

    def test_list_equals_function_false(self):

        numbers =[1, 2, 3, 4]

        numbers2 =[1, 3, 3, 4]

        actual =list_equals(numbers, numbers2)

        expected =False

        self.assertEqual(actual, expected)


    def test_remove_duplicate_values_function(self):

        numbers=[1, 3, 3, 4]

        actual =remove_duplicate_values(numbers)
    
        expected =[1, 4]

        self.assertEqual(actual, expected)

