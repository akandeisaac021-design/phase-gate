from unittest import TestCase

from task_one import *

class TaskOneTest(TestCase):

    def test_sorted_list_of_prime_numbers_function(self):

        numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        actual =sorted_list_of_prime_numbers(numbers)

        expected =[1, 2, 3, 5, 7]

        self.assertEqual(actual, expected)

    def test_negative_numbers_remover_fuction(self):

        numbers =[-1, 2, -3, 4, -5, 6, -7, 8, 9, 10]

        actual =negative_numbers_remover(numbers)

        expected =[0, 2, 0, 4, 0, 6, 0, 8, 9, 10]

        self.assertEqual(actual, expected)

    def test_list_sorter_function(self):

        numbers =[0, 2, 0, 4, 0, 6, 0, 8, 9, 10]

        actual =list_sorter(numbers)

        expected =[10, 9, 8, 6, 4, 2, 0, 0, 0, 0]

        self.assertEqual(actual, expected)

    def test_retain_only_duplicate_values_function(self):

        numbers =[0, 2, 0, 6, 0, 6, 0, 8, 2, 10]

        actual =retain_only_duplicate_values(numbers)

        expected =[0, 6, 2]

        self.assertEqual(actual, expected)
