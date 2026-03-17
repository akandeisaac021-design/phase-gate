from unittest import TestCase

from level_four import *


class test_level_four_functions(TestCase):

    def test_for_sum_of_two_numbers_functions(self):
        actual =sum_of_two_numbers(5,8)
        expected =13

        self.assertEqual(actual, expected)

    def test_for_sum_of_two_numbers_functions2(self):
        actual =sum_of_two_numbers(9 ,15)
        expected =24

        self.assertEqual(actual, expected)

    def test_for_is_number_even_function(self):

        actual =is_number_even(50)

        expected ="Even" 
        self.assertEqual(actual, expected)

    def test_for_is_number_even_function2(self):

        actual =is_number_even(51)

        expected ="Odd"

        self.assertEqual(actual, expected)


    def test_for_number_squared_function(self):

        actual =number_squared(5)

        expected =25

        self.assertEqual(actual, expected)

    def test_for_number_squared_function2(self):

        actual =number_squared(35)

        self.assertTrue(actual)

    def test_for_celcius_to_farenheit_converter_function(self):
    
        actual =celcius_to_fareneit_converter(34)

        self.assertTrue(actual)

    def test_for_celcius_to_farenheit_converter_function2(self):

        actual =celcius_to_fareneit_converter(60)

        self.assertTrue(actual)

    def test_for_number_is_prime_function(self):

        actual =number_is_prime(34)

        expected ="Not a prime number"

        self.assertEqual(actual, expected)

    def test_for_number_is_prime_function2(self):

        actual =number_is_prime(317)

        expected ="Tis a prime number"

        self.assertEqual(actual, expected)



    def test_for_largest_of_three_numbers_function(self):
    
        actual =largest_of_three_numbers(32, 34, 22)

        expected =34

        self.assertEqual(actual, expected)

    def test_for_largest_of_three_numbers_function2(self):

        actual =largest_of_three_numbers(1, 2, 3)

        expected =3

        self.assertEqual(actual, expected)


    
    def test_for_simple_interest_calculator_function(self):

        actual =simple_interest_calculator(3000, 42, 50.2)

        expected =63252

        self.assertEqual(actual, expected)

    def test_for_simple_interest_calculator_function2(self):

        actual =simple_interest_calculator(7004, 30, 656.76)

        expected =1379984.112

        self.assertEqual(actual, expected)


    def test_for_area_of_a_rectangle_function(self):

        actual =area_of_a_rectangle(4, 7)

        expected =28

        self.assertEqual(actual, expected)

    def test_for_area_of_a_rectangle_function2(self):

        actual =area_of_a_rectangle(12, 3)

        expected =36

        self.assertEqual(actual, expected)


    def test_for_number_reversal_function(self):

        actual =number_reversal(46765)

        expected ="56764"

        self.assertEqual(actual, expected)

    def test_for_number_reversal_function2(self):

        actual =number_reversal(3432)

        expected ="2343"

        self.assertEqual(actual, expected)
